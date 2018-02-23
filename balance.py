#encoding:utf-8
import requests
import json

address = "1Briu3soMHr9xygcnm81V66XDvMXnJwnbJ"

def bitflyer(address):
        r = requests.get("https://chainflyer.bitflyer.jp/v1/address/" + address)
        b = json.loads(r.text)
        return b['unconfirmed_balance']

def spectro(address):
        r = requests.get("https://explorer.spectrocoin.com/api/addr/" + address)
        b = json.loads(r.text)
        return b['totalReceived']

def blockchain(address):
        r = requests.get("https://blockchain.info/ja/q/getreceivedbyaddress/" + address)
        return r.text

def chainz(address):
        r = requests.get("https://chainz.cryptoid.info/btc/api.dws?q=getreceivedbyaddress&a=" + address)
        return r.text

def chainso(address):
        r = requests.get("https://chain.so/api/v2/get_address_balance/BTC/" + address)
        b = json.loads(r.text)
        return b['data']['confirmed_balance']

def btccom(address):
        r = requests.get("https://chain.api.btc.com/v3/address/" + address)
        b = json.loads(r.text)
        return b['data']['received']

print(bitflyer(address))
print(spectro(address))
print(blockchain(address))
print(chainz(address))
print(chainso(address))
print(btccom(address))
