import json

from py_etherscan.api.blocks import (
    BlockReward,
)
from py_etherscan.client import Client


with open('api.json', 'r') as f:
    data = json.load(f)

client = Client()


def test_block_reward() -> None:
    endpoint = client.get(BlockReward(address=data['address'], blockno=0,
                                      key=data['key']))
