import requests
from requests_ntlm import HttpNtlmAuth

url="http://vsc/"



r = requests.get(url, auth=HttpNtlmAuth('CKLu0','Ss12312345'))
