from .endpoint import Endpoint

from .. import data_processing


class EstimateConfirmationTime(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=gastracker
       &action=gasestimate
       &gasprice={gasprice}
       &apikey={key}
    """
    result_mapping = [data_processing.smart_float]


class GasOracle(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=gastracker
       &action=gasoracle
       &apikey={key}
    """
