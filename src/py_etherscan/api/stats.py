from .endpoint import Endpoint

from .. import data_processing


class TotalEtherSupply(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=stats
       &action=ethsupply
       &apikey={key}
    """
    result_mapping = [data_processing.smart_int]


class TotalEther2Supply(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=stats
       &action=ethsupply2
       &apikey={key}
    """


class EthPrice(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=stats
       &action=ethprice
       &apikey={key}
    """


class EthNodeSize(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=stats
       &action=chainsize
       &startdate={start_date}
       &enddate={end_date}
       &clienttype={client_type}
       &syncmode={syncmode}
       &sort={sort}
       &apikey={key}
    """


class NodeCount(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=stats
       &action=nodecount
       &apikey={key}
    """
