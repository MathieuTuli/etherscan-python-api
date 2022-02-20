from .endpoint import Endpoint

from .. import data_processing


class BlockNumber(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_blockNumber
       &apikey={key}
    """


class BlockByNumber(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_getBlockByNumber
       &tag={tag}
       &boolean={boolean}
       &apikey={key}
    """


class UncleByBlockNumberAndIndex(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_getUncleByBlockNumberAndIndex
       &tag={tag}
       &index={index}
       &apikey={key}
    """


class BlockTransactionCountByNumber(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_getBlockTransactionCountByNumber
       &tag={tag}
       &apikey={key}
    """
    result_mapping = [data_processing.hex_to_int]


class TransactionByHash(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_getTransactionByHash
       &txhash={txhash}
       &apikey={key}
    """


class TransactionByBlockNumberAndIndex(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_getTransactionByBlockNumberAndIndex
       &tag={tag}
       &index={index}
       &apikey={key}
    """


class TransactionCount(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_getTransactionCount
       &address={address}
       &tag={tag}
       &apikey={key}
    """
    result_mapping = [data_processing.hex_to_int]


class SendRawTransaction(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_sendRawTransaction
       &hex={hex}
       &apikey={key}
    """


class TransactionReceipt(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_getTransactionReceipt
       &txhash={txhash}
       &apikey={key}
    """


class Call(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_call
       &to={to}
       &data={data}
       &tag={tag}
       &apikey={key}
    """


class Code(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_getCode
       &address={address}
       &tag={tag}
       &apikey={key}
    """


class GasPrice(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_gasPrice
       &apikey={key}
    """
    result_mapping = [data_processing.hexwei_to_eth]


class EstimateGas(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=proxy
       &action=eth_estimateGas
       &data={data}
       &to={to}
       &value={value}
       &gasPrice={gasprice}
       &gas={gas}
       &apikey={key}
    """
    result_mapping = [data_processing.smart_int]
