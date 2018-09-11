# Ethereum-testChain
以太坊测试链

## 本程序要运行于python3.6（低版本不支持）， 需要安装web3
## 一共三个文件 config.py myContract.py main.py
## 主账户发行了 99999999999999999999700 个token, 若需要奖励token从主账户转出就可（直接用下文的transfer）

## config.py
config记录了合约的abi，地址，私链的地址

## myContract.py 
封装了一些函数

### def newAccount(_key = "12345")
新建一个账户，密码默认13245，返回账户的地址

### def balanceOf(address)
该函数参数为账户地址，返回的是token的数量

### def transfer(_to, _value, _key="12345")
1. 该函数是转账函数,默认从基础账户（主账户）转出
2. 参数 _to  是要转到的账户
3. 参数 _value 是要转账的token
4. 参数 _key 主账户的密码，默认为“12345”
若发生错误，返回一个空的dic
正常返回一个dic 各属性及意义为下表

| 属性        | 类型   |  意义  |
| --------   | -----:   | :----: |
| toAddress        | 字符串     |   转出地址    |
| fromAddress        | 字符串      |   转入地址    |
| toValue        | 整数      |   转出账户剩余token    |
| fromValue        | 整数      |   转入账户剩余token    |
| transferValue        | 整数      |   交易的金额    |

### def transferFrom(_from, _to, _value, _key="12345")
该函数是转账函数
1. 参数 _from  是要转到的账户
2. 参数 _to  是要转到的账户
3. 参数 _value 是要转账的token
4. 参数 _key 主账户的密码，默认为“12345”

若发生错误，返回一个空的dic
正常返回一个dic 各属性及意义为下表

| 属性        | 类型   |  意义  |
| --------   | -----:   | :----: |
| toAddress        | 字符串     |   转出地址    |
| fromAddress        | 字符串      |   转入地址    |
| toValue        | 整数      |   转出账户剩余token    |
| fromValue        | 整数      |   转入账户剩余token    |
| transferValue        | 整数      |   交易的金额    |


## main.py
该文件有一些实例，使用时可以根据示例使用
