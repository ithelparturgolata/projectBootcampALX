import requests
from bs4 import BeautifulSoup

strona = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
soup = BeautifulSoup(strona.content, "html.parser")


soup = soup.find(class_="pull-right price").get_text()


print(soup)




