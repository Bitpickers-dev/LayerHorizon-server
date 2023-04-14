import requests
from apscheduler.schedulers.background import BackgroundScheduler


def cache_blocks(base_url: str, chain: str):
    print(requests.get(f'{base_url}/{chain}block/cache_blocks/').json())


def auto_chache_blocks():
    base_url = 'http://127.0.0.1:8000'
    scheduler = BackgroundScheduler()
    scheduler.add_job(cache_blocks, 'interval', [base_url, 'eth'], seconds=20)
    scheduler.add_job(cache_blocks, 'interval', [base_url, 'arb'], seconds=10)
    scheduler.start()
