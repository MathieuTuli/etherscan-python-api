# Etherscan API in Python
This is a mininal API written in Python for the [Etherscan](https://etherscan.io/) API.

Unlike other APIs, returned data is processed and converted to expected units, rather than as a string.

## Status


## Endpoints Supported
<details><summary>Accounts<a href="src/py_etherscan/api/accounts.py"> (source)</a></summary>
<p>

* `Balance`
* `BalanceMultiple`
* `TransactionList`
* `InternalTransactionList`
* `InternalTransactionListByHash`
* `InternalTransactionListByBlock`
* `ERC20TokenTransferEvents`
* `ERC721TokenTransferEvents`
* `BlocksMined`
* `HistoricalEtherBalance`

</details>

<details><summary>Contracts<a href="src/py_etherscan/api/contracts.py"> (source)</a></summary>
<p>

* `ContractABI`
* `ContractSourceCode`

</details>

<details><summary>Transactions<a href="src/py_etherscan/api/transactions.py"> (source)</a></summary>
<p>

* `ContractExecutionStatus`
* `TransactionReceiptStatus`

</details>

<details><summary>Blocks<a href="src/py_etherscan/api/blocks.py"> (source)</a></summary>
<p>

* `BlockReward`
* `BlockCountdown`
* `BlockNoByTime`

</details>


<details><summary>Proxies<a href="src/py_etherscan/api/proxies.py"> (source)</a></summary>
<p>

* `BlockNumber`
* `BlockByNumber`
* `UncleByBlockNumberAndIndex`
* `BlockTransactionCountByNumber`
* `TransactionByHash`
* `TransactionByBlockNumberAndIndex`
* `TransactionCount`
* `SendRawTransaction`
* `TransactionReceipt`
* `Call`
* `Code`
* `GasPrice`
* `EstimateGas`

</details>

<details><summary>Tokens<a href="src/py_etherscan/api/tokens.py"> (source)</a></summary>
<p>

* `TotalTokenSupply`
* `TokenBalance`

</details>

<details><summary>Gas_tracker<a href="src/py_etherscan/api/gas_tracker.py"> (source)</a></summary>
<p>

* `EstimateConfirmationTime`
* `GasOracle`

</details>

<details><summary>Stats<a href="src/py_etherscan/api/stats.py"> (source)</a></summary>
<p>

* `TotalEtherSupply`
* `TotalEther2Supply`
* `EthPrice`
* `EthNodeSize`
* `NodeCount`

</details>

<details><summary>Logs<a href="src/py_etherscan/api/logs.py"> (source)</a></summary>
<p>

* `Logs`

</details>



## Installation
Firstly you'll need an [Etherscan](https://etherscan.io/) API key.

After, you can pip-install
```
git clone https://github.com/MathieuTuli/etherscan-python-api.git
cd etherscan-python-api
pip install .
```
*PyPi coming soon*

## TODO
1. Add PRO endpoints
2. Add add optional formattings to accounts urls
3. Default url formats for certain options
