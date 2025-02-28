import json
from web3 import Web3
from django.conf import settings

web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))

with open("voting/contract_abi.json") as f:
    contract_abi = json.load(f)["abi"]

contract = web3.eth.contract(
    address=settings.CONTRACT_ADDRESS, abi=contract_abi
)

def add_candidate(name, sender):
    tx = contract.functions.addCandidate(name).transact({"from": sender, "value": web3.to_wei(0.01, "ether")})
    web3.eth.wait_for_transaction_receipt(tx)

def vote(name, sender):
    tx = contract.functions.vote(name).transact({"from": sender})
    web3.eth.wait_for_transaction_receipt(tx)

def get_winner():
    return contract.functions.getWinner().call()

def get_balance():
    return web3.eth.get_balance(settings.CONTRACT_ADDRESS)





