# poetry run python deliverable_01.py
import requests
website_url = 'https://manning.com'
r = requests.get(website_url)
print(r.text)
