import requests

headers = {}
headers['Authorization'] = 'Bearer'

r = requests.get('http://127.0.0.1.8000/paradigms', headers=headers)

print(r.text)