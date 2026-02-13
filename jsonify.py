import sys 
import requests
import json


if len(sys.argv) < 2:
    print("Too few arguments")


response = requests.get("https://httpbin.org" +  sys.argv[1])

print(response.json())