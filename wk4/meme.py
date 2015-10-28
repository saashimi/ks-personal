import requests
import json
import secrets

def meme():
	url = 'http://version1.api.memegenerator.net/Instance_Create'
	payload = { 'username': USERNAME, 
				'password' : PASSWORD, 
				'languageCode' : 'en', 'imageID' : '42', 
				'text0' : 'Wherefore art thou', 
				'text 1' : 'Thunder?', 'generatorID' : '54',  }
	r = requests.get(url, params = payload)
	data = json.loads(r.text)
	print(data)

if __name__ == "__main__":
	meme()
