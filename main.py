import myContract
from myContract import myEth

print(myContract.balanceOf(myEth.accounts[0]))

print(myContract.myEth.accounts)

print(myContract.w3.personal.unlockAccount(myEth.coinbase, "12345"))

print(myContract.transferFrom(myEth.accounts[0], myEth.accounts[1], 100))




