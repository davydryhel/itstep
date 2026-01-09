import requests

response = requests.get("https://books.toscrape.com/")
response_text = response.text
response_parse = response_text.split('title="')

for element in response_parse[1:]:

    book_title = element.split('"')[0]
    print(book_title)