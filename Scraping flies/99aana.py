# paramrters Rooms bedrooms? bathrooms?
#installed lxml, bs4, requests
from typing import Tuple
from bs4 import BeautifulSoup
import requests
import csv

data = [] # This is used to store the rows of csv file

for count in range(1,5):
    source = requests.get("https://99aana.com/properties/page/" + str(count) + "?_offer_type=sale&keyword_search&_listing&realteo_order=date-desc&_property_type=houses&_price_min&_price_max").text
    soup = BeautifulSoup(source,'lxml')
    links = [] # these contain the links to the pages where the housing details are stored
    listing_title = soup.findAll('div',class_="listing-title")
    for title in listing_title:
        link = title.find('a')['href']
        links.append(link)
    for link in links:
        source = requests.get("https://99aana.com/property/bungalow-for-sale-at-lainchaur-kathmandu-8518/").text

        soup = BeautifulSoup(source,'lxml')
        title = price = location = floor = room = bedroom = bathroom = living_room = kitchen = parking = None
        title = soup.find('div',class_="property-title").h1.get_text(strip=True)
        title = title.split('For Sale')[0] #Removing For Sale in the title
        price = soup.find('div',class_='property-pricing').get_text(strip=True)
        location = soup.find('a',class_='listing-address').get_text(strip=True)
        area = soup.find('li',class_='main-detail-_area').get_text(strip=True)
        room = soup.find('li',class_='main-detail-_rooms').get_text(strip=True).split('Rooms')[1]
        bedroom = soup.find('li',class_='main-detail-_bedrooms').get_text(strip=True)
        bathroom = soup.find('li',class_='main-detail-_bathrooms').get_text(strip=True)
        floor = soup.find('div',class_='property-description').get_text(strip=True)
        if "storied" in floor:
            floor = floor.split("storied")[0].split()[-1]
            
        elif "stories" in floor:
            floor = floor.split("stories")[0].split()[-1]
   
        # LBK = living room, Bathroom and Kitchen
        LBK = soup.find('div',class_='property-description').findAll('ul')[2]
        LBK = LBK.findAll('li')

        for li in LBK:
            if "livingroom" in li.text:
                living_room = li.get_text(strip=True).split(':')[1]
            if "kitchen" in li.text:
                kitchen = li.get_text(strip=True).split(':')[1]

        parking_temp = soup.find('div',class_='property-description').findAll('ul')[3]
        parking_temp = parking_temp.findAll('li')
        for p in parking_temp:
            if "parking space" in p.text:
                parking = p.text.split('-')[1]

        row = [title,price,location,floor,room,bedroom,bathroom,living_room,kitchen,parking,link]
        data.append(row)
        print(row)
        print('-----------------------------------------------------------------------------')


headers = ['title','price','location','floor','room','bedroom','bathroom','living_room','kitchen','parking','link']
with open ('99aana.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

# store the column name of csv file

