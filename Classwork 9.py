#Task 1
'''
import urllib.request

opener = urllib.request.build_opener()
response = opener.open('https://httpbin.org/get')
print(response.read())
'''
#Task 2
'''
import requests

response = requests.get('https://httpbin.org/get')
print(response.content)
print(f"Datatype: {type(response.content)}")
print(response.text)
'''
#Task 3
'''
import requests

response = requests.post('https://httpbin.org/post', data="TEST DATA", headers={"h1" : "TEST TITLE"})
print(response.text)
'''
#Task 4

import requests
response = requests.get('https://coinmarketcap.com/')
responce_text = response.text
#print(responce_text)
responce_parse = response.text.split("<span>")
for parse_element in responce_parse:
    if parse_element.startswith("$"):
        for p_e in parse_element.split("</span>"):
            if parse_element.startswith("$") and p_e[2].isdigit():
                print(p_e[2])
