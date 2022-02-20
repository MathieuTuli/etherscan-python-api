from .endpoint import Endpoint

from .. import data_processing


class Balance(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=account
       &action=balance
       &address={address}
       &tag={tag}
       &apikey={key}
    """
    result_mapping = [data_processing.wei_to_eth]


class BalanceMultiple(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=account
       &action=balancemulti
       &address={address}
       &tag={tag}
       &apikey={key}
    """


class TransactionList(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=account
       &action=txlist
       &address={address}
       &startblock={startblock}
       &endblock={endblock}
       &page={page}
       &offset={offset}
       &sort={sort}
       &apikey={key}
    """


class InternalTransactionList(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=account
       &action=txlistinternal
       &address={address}
       &startblock={startblock}
       &endblock={endblock}
       &page={page}
       &offset={offset}
       &sort={sort}
       &apikey={key}
    """


class InternalTransactionListByHash(InternalTransactionList):
    url = """
    https://api.etherscan.io/api
       ?module=account
       &action=txlistinternal
       &txhash={txhash}
       &apikey={key}
    """


class InternalTransactionListByBlock(InternalTransactionList):
    url = """
    https://api.etherscan.io/api
       ?module=account
       &action=txlistinternal
       &startblock={startblock}
       &endblock={endblock}
       &page={page}
       &offset={offset}
       &sort={sort}
       &apikey={key}
    """


class ERC20TokenTransferEvents(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=account
       &action=tokentx
       &contractaddress={contractaddress}
       &address={address}
       &page={page}
       &offset={offset}
       &startblock={startblock}
       &endblock={endblock}
       &sort={sort}
       &apikey={key}
    """


class ERC721TokenTransferEvents(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=account
       &action=tokennfttx
       &contractaddress={contractaddress}
       &address={address}
       &page={page}
       &offset={offset}
       &startblock={startblock}
       &endblock={endblock}
       &sort={sort}
       &apikey={key}
    """


class BlocksMined(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=account
       &action=getminedblocks
       &address={address}
       &blocktype={blocktype}
       &page={page}
       &offset={offset}
       &apikey={key}
    """


class HistoricalEtherBalance(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=account
       &action=balancehistory
       &address={address}
       &blockno={blockno}
       &apikey={key}
    """
    result_mapping = [data_processing.wei_to_eth]
