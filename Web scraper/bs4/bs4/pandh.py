from bs4 import BeautifulSoup
import requests

#url,req,soup
url="https://www.varzesh3.com/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
# print(soup.find_all('h6'))

print(soup.find_all('p'))




