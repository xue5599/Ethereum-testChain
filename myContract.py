from web3 import Web3, HTTPProvider

import config

w3 = Web3(HTTPProvider(config.url))

myEth = w3.eth

myPersonal = w3.personal


contract = w3.eth.contract(address=Web3.toChecksumAddress(config.address), abi=config.abi)

allAccounts = myEth.accounts


def balanceOf(_address):
    if _address not in allAccounts:
        return False
    return contract.functions.balanceOf(_address).call()


def transfer(_to, _value, _key="12345"):
    if _to not in allAccounts:
        return {}
    if not (w3.personal.unlockAccount(w3.eth.coinbase, _key)):
        return {}
    tx_hash = contract.functions.transfer(_to, _value).transact({'from': myEth.coinbase})
    if not tx_hash:
        return {}
    w3.miner.start(1)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    w3.miner.stop()
    if not receipt:
        return {}

    return {'toAddress': _to, 'fromAddress': myEth.coinbase, 'fromValue': balanceOf(myEth.coinbase),
            'toValue': balanceOf(_to), 'transferValue': _value}


def transferFrom(_from, _to, _value, _key="12345"):
    if _to not in allAccounts:
        return {}
    if _from not in allAccounts:
        return {}
    w3.personal.unlockAccount(_from, _key)
    tx_hash = contract.functions.transferFrom(_from, _to, _value).transact({'from': _from, 'to': _to})
    w3.miner.start(1)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    w3.miner.stop()
    if not receipt:
        return {}

    return {'toAddress': _to, 'fromAddress': _from, 'fromValue': balanceOf(_from),
            'toValue': balanceOf(_to), 'transferValue': _value}


def newAccount(_key = "12345"):
    return w3.personal.newAccount(_key)
