#encoding:utf-8
from multiprocessing import Pool
import random
import requests
import json

address = ["1Briu3soMHr9xygcnm81V66XDvMXnJwnbJ","3Cbq7aT1tY8kMxWLbitaG7yT6bPbKChq64","3D2oetdNuZUqQHPJmcMDDHYoqkyNVsFk9r","16rCmCmbuWDhPjWTrpQGaU3EPdZF7MTdUk","32ixB1aXiwgpHGHo27SMRSULajCdc7jq9Q","1KjcmwEJ2iNkjanGzN4jWauN2Rsdk65GGu","12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr","12tdYFDZ2kAtaHTiJwScYpAEah3bWrXFwr","1f1miYFQWTzdLiCBxtHHnNiW7WAWPUccr","1P1iThxBH542Gmk1kZNXyji4E4iwpvSbrt","1K5pv63rag715mN2REYcfMbQs7RyukPuSK","1JevQLpYsKAt2STFZWmQ8TTAfjSC8RTGdJ"]

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

def balance(address):
        rand = random.randint(0,6)
        if rand == 0:
                return bitflyer(address)
        elif rand == 1:
                return spectro(address)
        elif rand == 2:
                return blockchain(address)
        elif rand == 3:
                return chainz(address)
        elif rand == 4:
                return chainso(address)
        elif rand == 5:
                return btccom(address)
if __name__ == '__main__':
        p = Pool(4)
        print(p.map(balance,address))
