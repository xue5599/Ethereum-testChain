import myContract
from myContract import myEth


print(myContract.balanceOf(myEth.accounts[0]))

print(myContract.transfer(myEth.accounts[1], 100))

print(myContract.transferFrom(myEth.accounts[0], myEth.accounts[1], 100))

print(myContract.newAccount())
