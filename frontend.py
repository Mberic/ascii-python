from art import tprint
from web3 import Web3, AsyncWeb3
import json

HARDHAT_DEFAULT_RPC_URL = 'https://8545-cartesi-rollupsexamples-kpajxxo360p.ws-eu104.gitpod.io'
INPUT_BOX = '0x5a723220579C0DCb8C9253E6b4c62e572E379945'
ASCII_CARTESI_DAPP = '0x142105FC8dA71191b3a13C738Ba0cF4BC33325e2'

HARDHAT_WALLET_ADDRESS = '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266'
PRIVATE_KEY = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'
 
w3 = Web3(Web3.HTTPProvider(HARDHAT_DEFAULT_RPC_URL))

with open("InputBox.json") as f:  # load InputBox ABI
    info_json = json.load(f)
ABI = info_json

contract = w3.eth.contract(address = INPUT_BOX, abi = ABI) # Instantiate smart contract 
nonce = w3.eth.get_transaction_count(HARDHAT_WALLET_ADDRESS)  

my_name = input("Enter text you want to convert to ASCII art : ")
tprint(my_name)

byte_value = my_name.encode() # Convert the string to a byte-like object
hex_value = '0x' + byte_value.hex() # Convert to a hex string

transaction = contract.functions.addInput(ASCII_CARTESI_DAPP, hex_value).build_transaction( {
    "gasPrice": w3.eth.gas_price, 
    "chainId": 31337, 
    "from": HARDHAT_WALLET_ADDRESS, 
    "nonce": nonce, 
})

signed_txn = w3.eth.account.sign_transaction(transaction, private_key = PRIVATE_KEY) # sign the transaction
result = w3.eth.send_raw_transaction(signed_txn.rawTransaction)  

print(result.hex())