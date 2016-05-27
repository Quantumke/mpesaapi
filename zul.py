# -*- coding: utf-8 -*-

import requests
url="https://safaricom.co.ke/mpesa_online/lnmo_checkout_server.php?wsdl"
call_back_url="http://127.0.0.1"
METHOD="POST"
MERCHANT_ID="1"
MERCHANT_TRANSACATION_ID='1'
MERCHANT_TRANSACTION_ID='1'
PRODUCT_ID='1'
CALL_BACK_METHOD="POST"
PASSKEY="1"
TIMESTAMP="1461164700"
PASSWORD="1"
AMOUNT="100"
NUMBER="0721799582"
xml='<?xml version="1.0" encoding="UTF-8"?><soapenv:Envelopexmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:tns="tns:ns" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"><soapenv:Header><tns:CheckOutHeader><MERCHANT_ID>%s</MERCHANT_ID><PASSWORD>%s</PASSWORD><TIMESTAMP>%s</TIMESTAMP></tns:CheckOutHeader></soapenv:Header><soapenv:Body><tns:processCheckOutRequest><MERCHANT_TRANSACTION_ID>%s</MERCHANT_TRANSACTION_ID><REFERENCE_ID>%s</REFERENCE_ID><AMOUNT>%s</AMOUNT><MSISDN>%s</MSISDN><ENC_PARAMS></ENC_PARAMS><CALL_BACK_URL>%s</CALL_BACK_URL><CALL_BACK_METHOD>%s</CALL_BACK_METHOD><TIMESTAMP>%s</TIMESTAMP></tns:processCheckOutRequest></soapenv:Body></soapenv:Envelope>' %(MERCHANT_ID,PASSWORD, TIMESTAMP, MERCHANT_TRANSACTION_ID, PRODUCT_ID,AMOUNT,NUMBER, call_back_url,CALL_BACK_METHOD,TIMESTAMP,)

headers = {'Content-Type': 'application/xml'} # set what your server accepts
print (requests.post(url, data=xml, headers=headers, verify=False).text, )
