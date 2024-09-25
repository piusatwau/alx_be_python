import requests

x = requests.get('https://packaging.python.org/en/latest/tutorials/installing-packages/')

print(x.text)