import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url='https://safaricom.co.ke/mpesa_online/lnmo_checkout_server.php?wsdl'
results = requests.get(url,
              params={
                  "MERCHANT_ID": "safaricom",
                  "passkey": "saf",
                  "TIMESTAMP": '1461164700'
              },
              headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
print(results.text)
