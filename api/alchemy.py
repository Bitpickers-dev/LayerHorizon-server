import requests
import environ

env = environ.Env()
env.read_env('.env')


def request_alchemy(chain: str, method: str, params: list):
    url = f"https://{chain}-mainnet.g.alchemy.com/v2/{env('ALCHEMY_KEY')}"
    payload = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": method,
        "params": params
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    return requests.post(url, json=payload, headers=headers).json()


def eth_blockNumber():
    return request_alchemy('eth', 'eth_blockNumber', [])


def eth_block(number: str):
    return request_alchemy('eth', 'eth_getBlockByNumber', [number, False])


def eth_blockTransaction(number: str):
    return request_alchemy('eth', 'eth_getBlockByNumber', [number, True])
