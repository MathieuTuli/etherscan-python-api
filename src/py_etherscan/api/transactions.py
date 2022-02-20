from .endpoint import Endpoint


class ContractExecutionStatus(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=transaction
       &action=getstatus
       &txhash={txhash}
       &apikey={key}
    """


class TransactionReceiptStatus(Endpoint):
    url = """
    https://api.etherscan.io/api
       ?module=transaction
       &action=gettxreceiptstatus
       &txhash={txhash}
       &apikey={key}
    """
