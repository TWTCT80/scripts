import requests
import sys

def loop():
    for word in sys.stdin:
        res = requests.get(url=f"http://10.10.103.11/{word}")
        if res.status_code == 404:
        print(res)
        data = res.json()
        print(data)