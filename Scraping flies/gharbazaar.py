# Scrape data from gharbazaar.py
import requests
from bs4 import BeautifulSoup

url = "https://www.gharbazar.com/property/details/house-at-sinamangal-4075"
source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')
soup = soup.find('div',class_='property_details')
print(soup.prettify())
