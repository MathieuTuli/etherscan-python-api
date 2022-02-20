from typing import Dict
from enum import Enum

from .. import data_processing


class EndpointStatus(Enum):
    OK = 1
    NOTOK = 0


URL_DEFAULTS = {
    'page': [1],
    'offset': [10],
    'startblock': [0],
    'endblock': [99999999],
    'sort': ['asc', 'desc'],
    'boolean': ['true', 'false'],
    'topic0_1_opr': ['and', 'or'],
    'closest': ['before', 'after'],
    'clienttype': ['geth', 'parity'],
    'blocktype': ['blocks', 'uncles'],
    'syncmode': ['default', 'archive'],
    'tag': ['latest', 'earliest', 'pending'],
}


class Endpoint:
    """APIRequest"""
    url = None
    result = None
    message = None
    result_mapping = None

    def __init__(self, *args, **kwargs) -> None:
        if args or not isinstance(kwargs, dict):
            raise ValueError(
                "Endpoints must be called with named arguments. " +
                "For Example, 'Endpoint(address=0x..., key=999..)'")
        for default, values in URL_DEFAULTS.items():
            if default not in kwargs:
                kwargs[default] = values[0]
            else:
                if kwargs[default] not in values:
                    raise ValueError(
                        f"{default} option must be one of {values}")
        self.url = self.url.replace('\n', '').replace(' ', '').format(**kwargs)

    def process(self, response: Dict) -> None:
        self.status = EndpointStatus.OK if response.get('status') == '1' or \
            all(k in response for k in ('jsonrpc', 'id', 'result')) else \
            EndpointStatus.NOTOK
        self.message = response.get('message', 'No message.')
        if self.status == EndpointStatus.NOTOK:
            self.result = self.message
        else:
            self.result = data_processing.map_result(
                response.get('result'), self.result_mapping)
