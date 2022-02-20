import json
import time

from py_etherscan.api.blocks import (
    BlockReward,
    BlockCountdown,
    BlockNoByTime
)
from py_etherscan.client import Client


with open('tests/api.json', 'r') as f:
    data = json.load(f)

client = Client()


def test_block_reward() -> None:
    time.sleep(1)
    endpoint = client.get(BlockReward(blockno=2165403,
                                      key=data['key']))


def test_block_countdown() -> None:
    time.sleep(1)
    endpoint = client.get(BlockCountdown(blockno=16701588,
                                         key=data['key']))


def test_block_by_time() -> None:
    time.sleep(1)
    endpoint = client.get(BlockNoByTime(timestamp=1578638524,
                                        closest='before',
                                        key=data['key']))
