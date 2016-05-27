import urllib.parse
import urllib.request
import ssl
def invoke_server():
	url="https://safaricom.co.ke/mpesa_online/lnmo_checkout_server.php?wsdl"
	values = ({
			"MERCHANT_TRANSACTION_ID": "1",
			"PASSWORD": "1",
            "REFERENCE_ID" :'1',
            "TIMESTAMP":'1461164700'
	})
	find_a_better_way = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	#data = urllib.parse.urlencode(values)
	#data = data.encode('utf-8')
	data = urllib.urlencode({'MERCHANT_TRANSACTION_ID': '1', 'PASSWORD': '10', 'REFERENCE_ID':'10','TIMESTAMP':'1461164700'})
	req = urllib.request.Request(url , data, headers={'User-Agent': 'Mozilla/5.0'})
	resp = urllib.request.urlopen(req, context=find_a_better_way)
	respData = resp.read()
	print(respData)
if __name__ == "__main__":
	invoke_server()


