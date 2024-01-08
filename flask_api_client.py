from flask import Flask, request, jsonify
import requests
import uuid
from abstract_blockchain import RPCBridge
from abstract_utilities import get_time_stamp
client_app = Flask(__name__)

# Server details
SERVER_HOST = '157.245.250.32'  # Change to your server's host
SERVER_PORT = '1546'           # Change to your server's port
rpc_mgr = RPCBridge()
def clean_rpc_js(rpc_mgr):
    rpc_js = rpc_mgr.rpc_js
    if rpc_js.get('user_settings',rpc_js).get('w3'):
        del rpc_js['user_settings']['w3']
    return rpc_js
def server_url(endpoint):
    """ Helper function to generate server URL for a given endpoint """
    return f"http://{SERVER_HOST}:{SERVER_PORT}/{endpoint}"

def get_abi_call(contract_address):
        response = requests.post(server_url('get_abi_call'), json={"contract_address": contract_address, 'network': None})
        response = response.json()
        abi=response.get('ABI')
        rpc_mgr.update_rpc_js(rpc_js=response.get('rpc_js'))
        return abi
def get_api_call(*args,**kwargs):
        response = requests.post(server_url('get_api_call'),
                                 json={"network":clean_rpc_js(rpc_mgr),
                                       'args':args,
                                       'kwargs':kwargs})
        return response.text
def get_token_transfer_events_by_contract_address(contract_address=None,start_block="earliest",end_block="latest",rpc_mgr=None):

    args = {
            "selected_api":"GetalistofERC20-TokenTransferEventsbyAddress",
            "module":"account",
            "action":"tokentx",
            "contractaddress":contract_address,
            "startblock":start_block,
            "endblock":end_block}
    return get_api_call(**args)
def get_account_balance_for_contract_address(contract_address=None,pair_address=None,tag="latest",rpc_mgr=None):

    args = {
            "selected_api":"GetErc20-TokenAccountBalanceforTokenContractAddress",
            "module":"account",
            "action":"tokenbalance",
            "contractaddress":contract_address,
            "address":pair_address,
            "tag":tag}
    
    return get_api_call(**args)
def get_token_transfer_events_by_address(address=None,start_block="earliest",end_block="latest",sort="asc",rpc_mgr=None):

    args = {
            "selected_api":"GetalistofERC20-TokenTransferEventsbyAddress",
            "module":"account",
            "action":"tokentx",
            "address":address,
            "startblock":start_block,
            "endblock":end_block,
            "sort":sort}
    return get_api_call(**args)
def total_token_supply_by_contract_address(contract_address=None,start_block="earliest",end_block="latest",sort=None,rpc_mgr=None):

    args = {
            "selected_api":"Erc20-TokenTotalSupplybyContractAddress",
            "module":"stats",
            "action":"tokensupply",
            "contractaddress":contract_address,
            "startblock":start_block,
            "endblock":end_block,
            "sort":sort}
    return get_api_call(**args)
def get_block_by_time(timestamp=int(get_time_stamp()),closest="before",rpc_mgr=None):

    args = {"module":"block",
            "action":"getblocknobytime",
            "timestamp":timestamp,
            "closest":closest}
    return get_api_call(**args)
   
contract_address = '0xcc5353d1a8aab6c229d0363b2ccfbe386fa0699e'
print(total_token_supply_by_contract_address())
