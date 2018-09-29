import random
import string
import sys

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getUsername():
	word = ""
	length = random.randint(5,9)
	for i in range(length):
		if i % 2 == 0:
			word += random.choice(CONSONANTS)
		else:
			word += random.choice(VOWELS)
	return word.capitalize() + str(random.randint(0, 999))
	
def getPassword():
	password = ""
	length = random.randint(5, 20)
	for i in range(length):
		password += random.choice(chars)
	return password
	
def getEmail(email, username):
	email = email.lower().split("@")
	if (email[1] != "gmail.com"):
		raise Exception("Email must be a GMail account.")
	username = username.lower()
	return email[0] + "+" + username + "@" + email[1]
	