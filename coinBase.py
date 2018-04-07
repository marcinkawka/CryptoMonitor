#!/usr/bin/env python
# -*- coding: latin-1 -*-

from coinbase.wallet.client import Client
from credentials import *
from pprint import pprint
from decimal import *
import json
import urllib2
'''
1. dodac taimestamp i source
2. zapis do pgSQL
'''

class Currency_pair(object):
	"""docstrstock)or currency_pair"""
	def __init__(self, stock, source='Unknown'):
		self.stock=stock
		self.source=source

	def set_buy_price(self,price):
		self.buyPrice=Decimal(price)
	
	def set_sell_price(self,price):
		self.sellPrice=Decimal(price)

	def get_buy_price(self):
		return self.buyPrice
	
	def get_sell_price(self):
		return self.sellPrice
	def str(self):
		return self.source+" "+self.stock+" "+str(self.buyPrice)+" "+str(self.sellPrice)	

client = Client(
    api_key,
    api_secret,
    api_version='2017-11-30 ')

getcontext().prec =4

tickers=[]

t1=Currency_pair("ETHEUR",'Coinbase')
t1.set_buy_price(client.get_buy_price(currency_pair='ETH-EUR')['amount'])
t1.set_sell_price(client.get_sell_price(currency_pair='ETH-EUR')['amount'])

tickers.append(t1)

t2=Currency_pair("BTCEUR")
t2.set_buy_price(client.get_buy_price(currency_pair='BTC-EUR')['amount'])
t2.set_sell_price(client.get_sell_price(currency_pair='BTC-EUR')['amount'])

tickers.append(t2)

print([ticker.str() for ticker in tickers])

'''
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

#PLNY
j = urllib2.urlopen('https://bitbay.net/API/Public/ETHPLN/ticker.json')
j_obj = json.load(j)
bb_eth_pln=Currency_pair("ETHPLN")
bb_eth_pln.set_buy_price(j_obj['ask'])
bb_eth_pln.set_sell_price(j_obj['bid'])


j = urllib2.urlopen('https://bitbay.net/API/Public/BTCPLN/ticker.json')
j_obj = json.load(j)
bb_btc_pln=Currency_pair("BTCPLN")
bb_btc_pln.set_buy_price(j_obj['ask'])
bb_btc_pln.set_sell_price(j_obj['bid'])

j = urllib2.urlopen('https://bitbay.net/API/Public/LTCPLN/ticker.json')
j_obj = json.load(j)
bb_ltc_pln=Currency_pair("LTCPLN")
bb_ltc_pln.set_buy_price(j_obj['ask'])
bb_ltc_pln.set_sell_price(j_obj['bid'])


print("\t\t|ETHEUR \t| BTCEUR \t| LTCEUR")
print('-' * 100)
print("CoinBase\t %5.2f \t %5.2f \t %5.2f" %(cb_eth_eur.get_buy_price(),	cb_btc_eur.get_buy_price(),		cb_ltc_eur.get_buy_price() ))
print("\t\t %5.2f \t %5.2f \t %5.2f" % (cb_eth_eur.get_sell_price(),	cb_btc_eur.get_sell_price(),		cb_ltc_eur.get_sell_price() ))
print('-' * 100)
print("BitBay \t\t %5.2f \t %5.2f \t %5.2f" %(bb_eth_eur.get_buy_price(),	bb_btc_eur.get_buy_price(),		bb_ltc_eur.get_buy_price()))
print("\t\t %5.2f \t %5.2f \t %5.2f" % (bb_eth_eur.get_sell_price(),	bb_btc_eur.get_sell_price(),		bb_ltc_eur.get_sell_price()))
print('-' * 100)
print("BitBay -PLNY \t\t %5.2f \t %5.2f \t %5.2f" %(bb_eth_pln.get_buy_price(),	bb_btc_eur.get_buy_price(),		bb_ltc_eur.get_buy_price()))
print("\t\t %5.2f \t %5.2f \t %5.2f" % (bb_eth_pln.get_sell_price(),	bb_btc_eur.get_sell_price(),		bb_ltc_eur.get_sell_price()))
print('-' * 100)
print("Sp_buy\t\t %5.2f\t\t %5.2f\t \t %5.2f" %(	cb_eth_eur.get_buy_price()-bb_eth_eur.get_buy_price(),
											cb_btc_eur.get_buy_price()-bb_btc_eur.get_buy_price(), 
											cb_ltc_eur.get_buy_price()-bb_ltc_eur.get_buy_price() 	)) 

print("Sp_sell\t\t %5.2f\t\t %5.2f\t\t %5.2f" %(	cb_eth_eur.get_sell_price()-bb_eth_eur.get_sell_price(),
												cb_btc_eur.get_sell_price()-bb_btc_eur.get_sell_price(), 
												cb_ltc_eur.get_sell_price()-bb_ltc_eur.get_sell_price() )) 

print("")'''