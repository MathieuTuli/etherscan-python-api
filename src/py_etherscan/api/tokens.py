from .endpoint import Endpoint

from .. import data_processing


class TotalTokenSupply(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=stats
       &action=tokensuply
       &contractaddress={contractaddress}
       &apikey={key}
    """
    result_mapping = [data_processing.smart_int]


class TokenBalance(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=stats
       &action=tokenbalance
       &contractaddress={contractaddress}
       &address={address}
       &apikey={key}
    """
    result_mapping = [data_processing.smart_int]
