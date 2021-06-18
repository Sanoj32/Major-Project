# paramrters Rooms bedrooms? bathrooms?
#installed lxml, bs4, requests
from bs4 import BeautifulSoup
import requests

source = requests.get("https://99aana.com/properties/?_offer_type=sale&keyword_search=&_listing=&realteo_order=date-desc&_property_type=houses&_price_min=&_price_max=").text
soup = BeautifulSoup(source,'lxml')
print(soup.prettify())
