from creator import createAccount

API_KEY = ''
site_key = '6LccFA0TAAAAAHEwUJx_c1TfTBWMTAOIphwTtd1b'
url = 'https://secure.runescape.com/m=account-creation/create_account'
proxy = ''
# proxy -> ip:port or user:pass@ip:port

gmailAccount  = ''

response, username, password = createAccount(API_KEY, site_key, proxy, gmailAccount)
print(response)
print(username + ":" + password)