from algosdk import account, mnemonic
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))



[
{'address1': 'HX3RMROXTJUDESH5JZASAWBSZITBJJ2LOU32TURCXRVNANY6FSCSJWIUUQ'
'private key1': '8frmdw3YFL8MQo6STGvMOLCt2yx2vSbYQ/Df8ZPr8C499xZF15poMkj9TkEgWDLKJhSnS3U3qdIivGrQNx4shQ=='
'passphrase1': 'funny orbit room liar claim cool away mixture myself pudding great adjust fork dad ramp runway age author wealth bulb child depend jealous ability bamboo'
}

{
'address2': 'LC5EV4VG54YZ3Y6ZQ7PY57CMWYHZE7C5MCO4USHE75BNFKI5K4JRILXL3Y'
'private key2': 'kRq+q8veTB3IDA3gppL1JPBsJk7LQ7Mf6c0ZjwUbb6BYukrypu8xnePZh9+O/Ey2D5J8XWCdykjk/0LSqR1XEw=='
'passphrase2': 'fall wear still uncover often also green artist swing enhance kiss across supreme maze foil duck wait piece tragic various arch short address absent coast'
}

]

# 


