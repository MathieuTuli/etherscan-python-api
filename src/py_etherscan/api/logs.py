from .endpoint import Endpoint


class Logs(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=logs
       &action=getLogs
       &fromBlock={fromblock}
       &toBlock={toblock}
       &address={address}
       &topic0={topic0}
       &topic0_1_opr=and
       &topic1={topic1}
       &apikey={key}
    """
