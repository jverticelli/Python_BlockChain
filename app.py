import json
from web3 import Web3

# Imposto connessione con rete di blockchain utilizzando INFURA:
infura_url = "https://rinkeby.infura.io/v3/bb6aa09fa6224043938ded3d2e6b45ef"
web3 = Web3(Web3.HTTPProvider(infura_url))
print("Connessione stabilita?", web3.isConnected())

# Derivo le properties del nodo e della rete a cui sono collegata
print("node N:" , web3.eth.block_number)
print("chain ID:", web3.eth.chain_id)
print("gas fee:", Web3.fromWei(web3.eth.gas_price, 'ether'), "ETH")

# Collegamento al Wallet Metamask
metamask_wallet = "0x8B7Ca5d128d3109abBB1588e16e4608fA163A21D"
balance = web3.eth.get_balance(metamask_wallet)
balance_eth = Web3.fromWei(balance, 'ether')
print("Balance MataMask Wallet:", balance_eth, "ETH")

# Interazione con Smart Contract (example: OBK token)
abi = json.loads('[{"constant":true,"inputs":[],"name":"proxyOwner","outputs":[{"name":"owner","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"implementation","type":"address"}],"name":"upgradeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"implementation","type":"address"},{"name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"implementation","outputs":[{"name":"impl","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferProxyOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"previousOwner","type":"address"},{"indexed":false,"name":"newOwner","type":"address"}],"name":"ProxyOwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"implementation","type":"address"}],"name":"Upgraded","type":"event"}]')
address = "0x75231F58b43240C9718Dd58B4967c5114342a86c"
contract = web3.eth.contract(address=address,abi=abi)
print("contract:", contract)