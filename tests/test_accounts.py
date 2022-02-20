from typing import Dict

import json

from py_etherscan.api.accounts import (
    Balance,
    BalanceMultiple,
    TransactionList,
    InternalTransactionList,
    InternalTransactionListByHash,
    InternalTransactionListByBlock,
    ERC20TokenTransferEvents,
    ERC721TokenTransferEvents,
    BlocksMined,
    HistoricalEtherBalance
)
from py_etherscan.client import Client


with open('api.json', 'r') as f:
    data = json.load(f)

client = Client()


def test_balance() -> None:
    endpoint = client.get(Balance(address=data['address'], key=data['key']))
    assert isinstance(endpoint.result, float)


def test_balance_multiple() -> None:
    address = ','.join([data['address']] * 10)
    endpoint = client.get(BalanceMultiple(address=address, key=data['key']))
    assert isinstance(endpoint.result, list)
    for res in endpoint.result:
        assert 'account' in res.keys()
        assert 'balance' in res.keys()
        assert isinstance(res['account'], str)
        assert isinstance(res['balance'], float)


def test_transaction_list() -> None:
    endpoint = client.get(
        TransactionList(address=data['address'],
                        key=data['key']))


def test_internal_transaction_list() -> None:
    endpoint = client.get(
        InternalTransactionList(address=data['address'],
                                key=data['key']))


def test_internal_transaction_list_by_block() -> None:
    txhash_ = \
        "0x07a39be252fce51c439c284315e92d0db05e7e9eafc1d1ca6588b245fb4e86e9"
    endpoint = client.get(
        InternalTransactionListByHash(
            txhash=txhash_,
            key=data['key']))


def test_internal_transaction_list_by_hash() -> None:
    endpoint = client.get(
        InternalTransactionListByBlock(address=data['address'],
                                       key=data['key']))


def test_erc20_token_transfer_events() -> None:
    cont = "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2"
    endpoint = client.get(
        ERC20TokenTransferEvents(
            contractaddress=cont,
            address=data['address'],
            key=data['key']))


def test_erc721_token_transfer_events() -> None:
    cont = "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2"
    endpoint = client.get(
        ERC721TokenTransferEvents(
            contractaddress=cont,
            address=data['address'],
            key=data['key']))


def BlocksMined() -> None:
    endpoint = client.get(
        BlocksMined(
            address=data['address'],
            key=data['key']))


def BlocksMined() -> None:
    endpoint = client.get(
        HistoricalEtherBalance(
            address=data['address'],
            key=data['key']))
