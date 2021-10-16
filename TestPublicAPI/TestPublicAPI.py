import requests
import json

files = {'file': open('TestImage.png','rb')}
q = requests.post('https://fcff-178-67-199-150.ngrok.io', files=files).text
print(q)

