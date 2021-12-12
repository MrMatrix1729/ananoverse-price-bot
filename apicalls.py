import time
import requests
import json

ananos = "https://horizon.stellar.org/order_book?buying_asset_type=credit_alphanum12&buying_asset_code=Ananos&buying_asset_issuer=GAB4YW6ZBV73IFQDSVYGKOXTLWX67LUDXRAXHUW2U5EXIFCMAWYHEHL7&selling_asset_type=native" 
manangos = "https://horizon.stellar.org/order_book?buying_asset_type=credit_alphanum12&buying_asset_code=Manangos&buying_asset_issuer=GCAD56MX3VL4YE3KIXPOWOMHTQYJOPYP7UQUQ2CAJQV4NYZ3566CAGKM&selling_asset_type=native"

tokens = [ananos, manangos]

file1 = open(r"./test.txt", "w") 
for x in range(len(tokens)):
	tokenused = tokens[x]
	price = (requests.get(tokenused).json())['asks'][0]['price']
	file1.write(price)
	file1.write("\n")
file1.close()

