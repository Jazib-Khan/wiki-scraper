import requests

response = requests.get(
    url="https://en.wikipedia.org/wiki/web_scraping",
)
print(response.status_code)
