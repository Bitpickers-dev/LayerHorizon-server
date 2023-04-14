import requests
from apscheduler.schedulers.background import BackgroundScheduler


def eth_cache_blocks(base_url: str):
    print(requests.get(f'{base_url}/ethblock/cache_blocks/').json())


def auto_chache_blocks():
    base_url = 'http://127.0.0.1:8000'
    scheduler = BackgroundScheduler()
    scheduler.add_job(eth_cache_blocks, 'interval', [base_url], seconds=20)
    scheduler.start()
