import requests
from time import sleep

from accinfo import *

url = 'https://secure.runescape.com/m=account-creation/create_account'

def createAccount(API_KEY, site_key, proxy, email):
	
	username = getUsername()
	password = getPassword()
	email = getEmail(email, username)

	proxy = {'http': 'socks5://' + proxy, 'https': 'socks5://' + proxy}
	s = requests.Session()
	captcha_id = s.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, site_key, url), proxies=proxy).text.split('|')[1]
	recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id), proxies=proxy).text
	print("solving ref captcha...")
	while 'CAPCHA_NOT_READY' in recaptcha_answer:
		sleep(5)
		recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id), proxies=proxy).text
	recaptcha_answer = recaptcha_answer.split('|')[1]
	payload = {
		'theme': 'dual',
		'email1': email,
		'onlyOneEmail': '1',
		'password1': password,
		'displayname': username,
		'day': str(random.randint(1,30)),
		'month': str(random.randint(1,12)),
		'year': str(random.randint(1950, 2005)),
		'g-recaptcha-response': recaptcha_answer,
		'submit': 'Play Now'
	}
	response = s.post(url, payload, proxies=proxy)
	return response, email, password