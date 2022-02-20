from typing import Dict

import json
import time

from py_etherscan.api.proxies import (
)
from py_etherscan.client import Client


with open('tests/api.json', 'r') as f:
    data = json.load(f)

client = Client()


def test_balance() -> None:
    time.sleep(1)
    endpoint = client.get((address=data['address'], key=data['key']))
