from atproto import Client
import json

file = open('credentials.json', 'r+').read()
credentials = json.loads(file)

client = Client()
client.login(credentials['username'], 
             credentials['password'])

client.send_post(text=f'hello')
