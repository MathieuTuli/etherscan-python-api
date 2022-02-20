from .endpoint import Endpoint


class ContractABI(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=contract
       &action=getabi
       &address={address}
       &apikey={key}
    """


class ContractSourceCode(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=contract
       &action=getsourcecode
       &address={address}
       &apikey={key}
    """
