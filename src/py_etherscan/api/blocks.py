from .endpoint import Endpoint

from .. import data_processing


class BlockReward(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=block
       &action=getblockreward
       &address={address}
       &blockno={blockno}
       &apikey={key}
    """


class BlockCountdown(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=block
       &action=getblockcountdown
       &address={address}
       &blockno={blockno}
       &apikey={key}
    """


class BlockNoByTime(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=block
       &action=getblocknobytime
       &timestamp={timestamp}
       &closest={closest}
       &apikey={key}
    """
    result_mapping = [data_processing.smart_int]
