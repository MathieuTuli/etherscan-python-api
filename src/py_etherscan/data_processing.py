from typing import Union, List, Dict, Tuple
from datetime import datetime


def smart_int(x):
    if x:
        if 'x' in x:
            return int(x, base=16)
        return int(x)
    return None


def smart_float(x): return float(x) if x else None


def listed_ints(x): return [smart_int(val) for val in x.split(',')]


def unix_to_datetime(x): return datetime.fromtimestamp(int(x))


def str_to_datetime(x): return datetime.strptime(x, '%Y-%m-%d')


def wei_to_eth(val: Union[str, float, int]) -> float:
    return float(smart_int(val)) / 1000000000000000000


def map_result(
    result: Union[str, List[Dict]],
        mapping: Union[None, List[Tuple[List[str], callable]]] = None) -> Dict:
    unwrap = False
    if isinstance(result, dict):
        result = [result]
        unwrap = True
    if isinstance(result, list):
        for i, data in enumerate(result):
            for key, call in RESULT_MAPPING.items():
                if key in data:
                    if result[i][key] == 'null':
                        result[i][key] = None
                        continue
                    # specific overriding if need be
                    if mapping and key in mapping:
                        call = mapping[key]
                    result[i][key] = call(result[i][key])
        if unwrap:
            return result[0]
        return result
    elif isinstance(result, str):
        if mapping:
            return mapping[0](result)
        return result


RESULT_MAPPING = {
    # date
    'timestamp': unix_to_datetime,
    'ethbtc_timestamp': unix_to_datetime,
    'ethusd_timestamp': unix_to_datetime,
    'chainTimeStamp': str_to_datetime,
    'UTCDate': str_to_datetime,
    # smart int
    'gas': smart_int,
    'transactionIndex': smart_int,
    # 'type': smart_int,
    'BlockNumber': smart_int,
    'v': smart_int,
    'chainId': smart_int,
    'gasLimit': smart_int,
    'status': smart_int,
    'cumulativeGasUsed': smart_int,
    'gasUsed': smart_int,
    'size': smart_int,
    'CurrentBlock': smart_int,
    'CountdownBlock': smart_int,
    'RemainingBlock': smart_int,
    'nonce': smart_int,
    'isError': smart_int,
    'confirmations': smart_int,
    'traceId': smart_int,
    'errCode': smart_int,
    'tokenDecimal': smart_int,
    'unclePosition': smart_int,
    'TotalNodeCount': smart_int,
    'Runs': smart_int,
    'Proxy': smart_int,
    'OptimizationUsed': smart_int,
    'FastGasPrice': smart_int,
    'ProposeGasPrice': smart_int,
    'SafeGasPrice': smart_int,
    'LastBlock': smart_int,
    'EthSupply': smart_int,
    'Eth2Staking': smart_int,
    'BurntFees': smart_int,
    'chainSize': smart_int,
    # smart float
    'EstiamteTimeInSec': smart_float,
    'suggestBaseFee': smart_float,
    'ethbtc': smart_float,
    'ethusd': smart_float,
    # wei to eth
    'maxFeePerGas': wei_to_eth,
    'gasPrice': wei_to_eth,
    'blockreward': wei_to_eth,
    'maxPriorityFeePerGas': wei_to_eth,
    'blockReward': wei_to_eth,
    'uncleInclusionReward': wei_to_eth,
    'baseFeePerGas': wei_to_eth,
    'value': wei_to_eth,
    'balance': wei_to_eth,
    # listed operation
    'gasUsedRatio': listed_ints,
    # recursion
    'uncles': map_result,
}
