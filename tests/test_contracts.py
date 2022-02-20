from typing import Dict

import json
import time

from py_etherscan.api.contracts import (
    ContractABI,
    ContractSourceCode
)
from py_etherscan.client import Client


with open('tests/api.json', 'r') as f:
    data = json.load(f)

client = Client()


def test_contract_abi() -> None:
    time.sleep(1)
    address = "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"
    endpoint = client.get(ContractABI(
        address=address, key=data['key']))


def test_contract_source_code() -> None:
    time.sleep(1)
    address = "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"
    endpoint = client.get(ContractABI(
        address=address, key=data['key']))
