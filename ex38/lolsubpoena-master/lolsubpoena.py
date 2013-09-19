import sys
import oauth2 as oauth
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import base64
import json

# get your own Twitter oAuth information: http://dev.twitter.com/apps/new
# store it in file called application.oauth. first line is key, second line is secret
def oauthLoad(filePrefix):
	f = open(filePrefix + '.oauth', 'r')
	key = f.readline().rstrip()
	secret = f.readline().rstrip()
	f.close()
	return key, secret

def dumpUsage():
	print 'Usage:'
	print sys.argv[0] + ' your_twitter_username --get-token'
	print sys.argv[0] + ' your_twitter_username --send-dm other_twitter_username'
	print sys.argv[0] + ' your_twitter_username --list-dm [other_twitter_username]'
	sys.exit()

def encodeBase64(text):
	return base64.b64encode(text, '!@')
	
def decodeBase64(text):
	return base64.b64decode(text.encode('ascii'), '!@')

def sendDM(token, secret, toUser, message):
	response, content = oauthRequest(token, secret, twitterBaseAPI + "/direct_messages/new.json", "POST", None, "user=" + toUser + "&text=_" + message)
	return response

def getDM(token, secret, fromUser = None):
	response, content = oauthRequest(token, secret, twitterBaseAPI + "/direct_messages.json", "GET")
	data = json.loads(content)
	
	filteredData = []
	for i in data:
		if i['text'][0] == '_' and (i['sender_screen_name'] == fromUser or fromUser == None):
			i['text'] = i['text'][1:len(i['text'])]
			filteredData.append(i)
	return filteredData

def decryptAndPrintDM(dmObj):
	sender = dmObj['sender_screen_name']
	if sender in keys:
		encryptionKey = keys[sender]
	else:
		encryptionKey = loadKey(twitterUser + '.' + sender, 'private', True)
		keys[sender] = encryptionKey
	plaintext = decrypt(decodeBase64(dmObj['text']), encryptionKey)
	print dmObj['created_at'] + ' from ' + sender + ':'
	print plaintext
	print '-----------------------------'

def pad(text, blocksize):
	padded = text
	while len(padded) % blocksize != 0:
		padded += chr(30)
	return padded
	
def loadKey(twitterUser, which, returnHash = False):
	f = open(twitterUser + '.' + which)
	raw = f.read()
	f.close()
	
	if returnHash == True:
		sha = SHA256.new(raw)
		return sha.digest()
	else:
		return raw

def encrypt(plaintext, key):
	rand = Random.new()
	iv = rand.read(16)
	aes = AES.new(key, AES.MODE_CBC, iv)
	return iv + aes.encrypt(pad(plaintext, 16))

def decrypt(ciphertext, key):
	iv = ciphertext[0:16]
	ciphertext = ciphertext[16:len(ciphertext)]
	aes = AES.new(key, AES.MODE_CBC, iv)
	return aes.decrypt(ciphertext)
	
def oauthParseToken(content):
	token = content.split('&')[0].split('=')[1]
	secret = content.split('&')[1].split('=')[1]
	
	return token, secret

def oauthRequest(key, secret, url, method = 'GET', headers = {'Content-type': 'application/x-www-form-urlencoded'}, body = None):
	consumer = oauth.Consumer(key = oauthConsumerKey, secret = oauthConsumerSecret)
	token = oauth.Token(key = key, secret = secret)
	client = oauth.Client(consumer, token)

	response, content = client.request(url, method = method, body = body, headers = headers, force_auth_header = True)
	# todo: read the response and make sure status is 200. json lib doesn't want to loads() it for some reason
	return response, content
	
def oauthRequestToken():
	consumer = oauth.Consumer(key = oauthConsumerKey, secret = oauthConsumerSecret)
	client = oauth.Client(consumer)
	
	resp, content = client.request(oauthTokenRequest, 'GET')
	token, secret = oauthParseToken(content)
	
	print 'Visit the following URL in your browser and retrieve the authorization PIN: http://twitter.com/oauth/authorize?oauth_token=' + token
	
	return token, secret
	
def oauthAccessToken(requestToken, requestSecret, pin, twitterUser):
	consumer = oauth.Consumer(key = oauthConsumerKey, secret = oauthConsumerSecret)
	token = oauth.Token(requestToken, requestSecret)
	token.set_verifier(pin)
	client = oauth.Client(consumer, token)
	
	response, content = client.request(oauthTokenAccess)
	accessToken, accessSecret = oauthParseToken(content)
	
	f = open(twitterUser + '.oauth', 'w')
	f.write(accessToken + "\n")
	f.write(accessSecret + "\n")
	f.close()
	
	return accessToken, accessSecret

if len(sys.argv) <= 2:
	dumpUsage()

# config stuff
oauthTokenRequest = 'http://twitter.com/oauth/request_token'
oauthTokenAccess = 'http://twitter.com/oauth/access_token'
oauthTokenAuth = 'http://twitter.com/oauth/authorize'
twitterBaseAPI = 'http://api.twitter.com/1'

oauthConsumerKey, oauthConsumerSecret = oauthLoad('application')

keys = {}
twitterUser = sys.argv[1]
accessToken, accessSecret = oauthLoad(twitterUser)

if sys.argv[2] == '--get-token':
    requestToken, requestSecret = oauthRequestToken()
    pin = raw_input('Enter the authorization PIN: ')
    accessToken, accessSecret = oauthAccessToken(requestToken, requestSecret, pin, twitterUser)
    print 'Access token retrieved, stored in ' + twitterUser + '.oauth'
elif sys.argv[2] == '--send-dm':
    if len(sys.argv) < 4:
    	dumpUsage()
    
    toUser = sys.argv[3]
    message = raw_input("Type your message (keep it short, the actual message will be longer):\n")
    encryptionKey = loadKey(twitterUser + '.' + toUser, 'private', True)
    encrypted = encodeBase64(encrypt(message, encryptionKey))

    if len(encrypted) <= 140:
		sendDM(accessToken, accessSecret, toUser, encrypted)
		print
		print 'Message sent!'
    else:
		print 'Error: the encrypted message was too long'
		sys.exit()
    
elif sys.argv[2] == '--list-dm':
    print 'Here are your DMs:'
    print
    
    filterUser = None
    
    if len(sys.argv) >= 4:
    	filterUser = sys.argv[3]
    
    dmList = getDM(accessToken, accessSecret, filterUser)
    for d in dmList:
    	decryptAndPrintDM(d)
	