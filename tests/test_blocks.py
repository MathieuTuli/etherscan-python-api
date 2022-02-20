import json
import time

from py_etherscan.api.blocks import (
    BlockReward,
)
from py_etherscan.client import Client


with open('tests/api.json', 'r') as f:
    data = json.load(f)

client = Client()


def test_block_reward() -> None:
    time.sleep(1)
    endpoint = client.get(BlockReward(blockno=2165403,
                                      key=data['key']))
