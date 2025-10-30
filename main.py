import requests
from bs4 import BeautifulSoup


url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

tag = soup.find('span', class_='a-offscreen')
full_price = tag.get_text()
price =float (full_price.split("$")[1])
print(price)



