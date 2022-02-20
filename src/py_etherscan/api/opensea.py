from .endpoint import Endpoint


class Asset(Endpoint):
    url = """
    https://api.opensea.io/api/v1/asset/{contractaddress}/{tokenid}/
    """
