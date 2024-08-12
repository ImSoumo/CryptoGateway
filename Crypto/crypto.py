import requests

async def check_transaction_ethereum(TxId):
    ERC_API_KEY = "QHTC1CRQUJF743SHY1UDZ82HTJGS74ENB4"
    check = f"https://api.etherscan.io/api?module=transaction&action=gettxreceiptstatus&txhash={TxId}&apikey={ERC_API_KEY}"
    response = requests.get(check).json()
    return response

async def check_transaction_tron(TxId):
    check = f"https://api.trongrid.io/v1/transaction/{TxId}"
    response = requests.get(check).json()
    return response

async def check_transaction_bsc(TxId):
    BNB_API_KEY = "3AIXQKWXE9FH4TZJAJEDNQK2VRCBJ4UMV1"
    check = f"https://api.bscscan.io/api?module=transaction&action=gettxreceiptstatus&txhash={TxId}&apikey={BNB_API_KEY}"
    response = requests.get(check).json()
    return response

async def format_ethereum_response(response):
    if response['status'] == '1':
        details = f"Transaction Status: Success\nTransaction Details: {response['result']}"
    else:
        details = f"Transaction Status: Fail\nTransaction Details: {response['result']}"
    return details

async def format_tron_response(response):
    if response['success']:
        details = f"Transaction Status: Success\nTransaction Details: {response['data']}"
    else:
        details = f"Transaction Status: Fail\nTransaction Details: {response['data']}"
    return details

async def format_bsc_response(response):
    if response['status'] == '1':
        details = f"Transaction Status: Success\nTransaction Details: {response['result']}"
    else:
        details = f"Transaction Status: Fail\nTransaction Details: {response['result']}"
    return details

async def check_transaction_bitcoin(TxId):
    check = f"https://blockchain.info/rawtx/{TxId}"
    response = requests.get(check).json()
    return response
