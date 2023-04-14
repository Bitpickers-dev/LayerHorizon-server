from api import funcs
import pprint
import requests
import environ

env = environ.Env()
env.read_env('.env')


def requestAlchemy(chain: str, method: str, params: list):
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


class EthApiClass():
    def requestAlchemy(self, method: str, params: list):
        return requestAlchemy('eth', method, params)

    def getNumber(self):
        return self.requestAlchemy('eth_blockNumber', [])['result']

    def getBlock(self, number: str, detail: bool):
        return self.requestAlchemy('eth_getBlockByNumber', [number, detail])['result']

    def getFormatBlock(self, number: str, detail: bool):
        result = self.getBlock(number, detail)

        if detail:
            transactions = []
            for transaction in result['transactions']:
                transactions.append({
                    'hash': transaction.get('hash', 'null'),
                    'from': transaction.get('from', 'null'),
                    'to': transaction.get('to', 'null'),
                    'value': funcs.hex_to_eth(transaction.get('value', '0')),
                    'gasPrice': funcs.hex_to_gwei(transaction.get('gasPrice', '0')),
                    'transactionIndex': transaction.get('transactionIndex', 'null'),
                })
        else:
            transactions = 'null'

        return {
            'number': result['number'],
            'hash': result['hash'],
            'timestamp': int(result['timestamp'], 16),
            'transactions': transactions
        }


class ArbApiClass(EthApiClass):
    def requestAlchemy(self, method: str, params: list):
        return requestAlchemy('arb', method, params)

    def getFormatBlock(self, number: str, detail: bool):
        result = self.getBlock(number, detail)

        if detail:
            transactions = []
            for transaction in result['transactions']:
                transactions.append({
                    'hash': transaction.get('hash', 'null'),
                    'from': transaction.get('from', 'null'),
                    'to': transaction.get('to', 'null'),
                    'value': funcs.hex_to_eth(transaction.get('value', '0')),
                    'gasPrice': funcs.hex_to_gwei(transaction.get('gasPrice', '0')),
                    'transactionIndex': transaction.get('transactionIndex', 'null'),
                })
        else:
            transactions = 'null'

        return {
            'number': result['number'],
            'hash': result['hash'],
            'timestamp': int(result['timestamp'], 16),
            'l1BlockNumber': result['l1BlockNumber'],
            'transactions': transactions
        }
