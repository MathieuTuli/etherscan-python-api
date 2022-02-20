import json
import time

from py_etherscan.api.accounts import BalanceMultiple
from py_etherscan.client import Client, EmptyResponse, InvalidAPIKey


def test_client():
    with open('tests/api.json', 'r') as f:
        data = json.load(f)

    client = Client()
    key = data['key']

    addresses = [data['address']] * 2
    try:
        time.sleep(1)
        client.get(BalanceMultiple(address=addresses, key=key))
    except EmptyResponse:
        pass

    addresses = ','.join([data['address']] * 2)
    time.sleep(1)
    client.get(BalanceMultiple(address=addresses, key=key))

    addresses = ','.join([data['address']] * 2)
    try:
        time.sleep(1)
        client.get(BalanceMultiple(address=addresses, key=''))
    except InvalidAPIKey:
        pass
