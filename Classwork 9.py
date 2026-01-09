import requests

response = requests.get("https://books.toscrape.com/")
response_text = response.text

# 1) Ріжемо HTML по title="
response_parse = response_text.split('title="')

# 2) Проходимося по частинах
for element in response_parse[1:]:  # [1:], бо перший шматок — не книга
    # 3) Назва закінчується на "
    book_title = element.split('"')[0]
    print(book_title)
