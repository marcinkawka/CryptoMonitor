#!/usr/bin/env python
# -*- coding: latin-1 -*-

from coinbase.wallet.client import Client
from credentials import *
from pprint import pprint
from decimal import *
import json
import urllib2

class Currency_pair(object):
	"""docstrstock)or currency_pair"""
	def __init__(self, stock):
		self.stock=stock

	def set_buy_price(self,price):
		self.buyPrice=Decimal(price)
	
	def set_sell_price(self,price):
		self.sellPrice=Decimal(price)

	def get_buy_price(self):
		return self.buyPrice
	
	def get_sell_price(self):
		return self.sellPrice
			

client = Client(
    api_key,
    api_secret,
    api_version='2017-11-30 ')

getcontext().prec =4

cb_eth_eur=Currency_pair("ETHEUR")
cb_eth_eur.set_buy_price(client.get_buy_price(currency_pair='ETH-EUR')['amount'])
cb_eth_eur.set_sell_price(client.get_sell_price(currency_pair='ETH-EUR')['amount'])

cb_btc_eur=Currency_pair("BTCEUR")
cb_btc_eur.set_buy_price(client.get_buy_price(currency_pair='BTC-EUR')['amount'])
cb_btc_eur.set_sell_price(client.get_sell_price(currency_pair='BTC-EUR')['amount'])

cb_ltc_eur=Currency_pair("LTCEUR")
cb_ltc_eur.set_buy_price(client.get_buy_price(currency_pair='LTC-EUR')['amount'])
cb_ltc_eur.set_sell_price(client.get_sell_price(currency_pair='LTC-EUR')['amount'])

j = urllib2.urlopen('https://bitbay.net/API/Public/ETHEUR/ticker.json')
j_obj = json.load(j)
bb_eth_eur=Currency_pair("ETHEUR")
bb_eth_eur.set_buy_price(j_obj['ask'])
bb_eth_eur.set_sell_price(j_obj['bid'])

j = urllib2.urlopen('https://bitbay.net/API/Public/BTCEUR/ticker.json')
j_obj = json.load(j)
bb_btc_eur=Currency_pair("BTCEUR")
bb_btc_eur.set_buy_price(j_obj['ask'])
bb_btc_eur.set_sell_price(j_obj['bid'])

j = urllib2.urlopen('https://bitbay.net/API/Public/LTCEUR/ticker.json')
j_obj = json.load(j)
bb_ltc_eur=Currency_pair("LTCEUR")
bb_ltc_eur.set_buy_price(j_obj['ask'])
bb_ltc_eur.set_sell_price(j_obj['bid'])


print("\t\t|ETHEUR \t| BTCEUR \t| LTCEUR")
print('-' * 100)
print("CoinBase\t %5.2f \t %5.2f \t %5.2f" %(cb_eth_eur.get_buy_price(),	cb_btc_eur.get_buy_price(),		cb_ltc_eur.get_buy_price() ))
print("\t\t %5.2f \t %5.2f \t %5.2f" % (cb_eth_eur.get_sell_price(),	cb_btc_eur.get_sell_price(),		cb_ltc_eur.get_sell_price() ))
print('-' * 100)
print("BitBay \t\t %5.2f \t %5.2f \t %5.2f" %(bb_eth_eur.get_buy_price(),	bb_btc_eur.get_buy_price(),		bb_ltc_eur.get_buy_price()))
print("\t\t %5.2f" %(bb_eth_eur.get_buy_price()))
print('-' * 100)
print("Sp_buy\t\t %5.2f" %(cb_eth_eur.get_buy_price()-(bb_eth_eur.get_buy_price())) )
print("Sp_sell\t\t %5.2f" %(cb_eth_eur.get_sell_price()-(bb_eth_eur.get_sell_price())))

print("")