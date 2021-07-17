from typing import final
from bs4 import BeautifulSoup
import requests
import csv
import sys
import time
import pandas as pd
import os

# function to get data using links from the links csv file
def aana():
    stored_links = []
    # write headers in a csv file if its empty
    if os.stat('csv-files/99aana.csv').st_size == 0:
        with open ("csv-files/99aana.csv",'w', newline='',encoding="latin1") as f:
            writer = csv.writer(f)
            headers = ['title','price','location','district','floor','room','bedroom','bathroom','livingroom','kitchen','parking','link']
            writer.writerow(headers)

    for count in range(1,290):
        source = requests.get("https://99aana.com/properties/page/" + str(count) + "?_offer_type=sale&keyword_search&_listing&realteo_order=date-desc&_property_type=houses&_price_min&_price_max").text
        soup = BeautifulSoup(source,'lxml')
        links = [] # these contain the links to the pages where the housing details are stored
        listing_title = soup.findAll('div',class_="listing-title")
        for title in listing_title:
            link = title.find('a')['href']
            links.append(link)
        for link in links:
            if link not in stored_links:
                title = price = location = floor = room = bedroom = bathroom = livingroom = kitchen = parking = None
                source = requests.get(link).text
                soup = BeautifulSoup(source,'lxml')

                title = soup.find('div',class_="property-title").h1.get_text(strip=True)
                title = title.split('For Sale')[0] #Removing For Sale in the title
                price = soup.find('div',class_='property-pricing').get_text(strip=True)
                location = soup.find('a',class_='listing-address').get_text(strip=True)
                district = location.split()[-1]

                soup = soup.find('div',class_="property-description")
                try:
                    soup.find('div',class_="listings-container").decompose()  # Remove the similar properties div
                except:
                    pass
                main_features = soup.find('ul',class_='property-main-features')
                area = main_features.find('li',class_="main-detail-_area").get_text(strip=True)
                try:
                    room = main_features.find('li',class_="main-detail-_rooms").span.get_text(strip=True)
                except:
                    pass
                try:
                    bedroom = main_features.find('li',class_="main-detail-_bedrooms").span.get_text(strip=True)
                except:
                    pass
                try:
                    bathroom = main_features.find('li',class_="main-detail-_bathrooms").span.get_text(strip=True)
                except:
                    pass
                floor = soup.get_text(strip=True)
                if "storied" in floor:
                    floor = floor.split("storied")[0].split()[-1]

                elif "stories" in floor:
                    floor = floor.split("stories")[0].split()[-1]

                # misc = living room, Bathroom and Kitchen also bedrooms,bathrooms , and rooms written after property highlights
                misc = soup.findAll('ul')[2]
                misc = misc.findAll('li')

                for li in misc:
                    if "livingroom" in li.text.lower() and "total" in li.text.lower():
                        if ":" in li.text.lower():
                            livingroom = li.get_text(strip=True).split(':')[1]
                        else:
                            livingroom = li.get_text(strip=True).split('-')[1]
                    if "kitchen" in li.text.lower() and "total" in li.text.lower():
                        if ":" in li.text.lower():
                            kitchen = li.get_text(strip=True).split(':')[1]
                        else:
                            kitchen = li.get_text(strip=True).split('-')[1]
                    if bedroom == None:
                        if "bedroom" in li.text.lower() and "total" in li.text.lower():
                            if ":" in li.text.lower():
                                bedroom = li.get_text(strip=True).split(':')[1]
                            else:
                                bedroom = li.get_text(strip=True).split('-')[1]
                    if room == None:
                        if " room" in li.text.lower() and "total" in li.text.lower():
                            if ":" in li.text.lower():
                                room = li.get_text(strip=True).split(':')[1]
                            else:
                                room = li.get_text(strip=True).split('-')[1]
                    if bathroom == None:
                        if "bathroom" in li.text.lower() and "total" in li.text.lower():
                            if ":" in li.text.lower():
                                bathroom = li.get_text(strip=True).split(':')[1]
                            else:
                                bathroom = li.get_text(strip=True).split('-')[1]

                parking_temp = soup.findAll('ul')[3]
                parking_temp = parking_temp.findAll('li')
                print(link)
                for p in parking_temp:
                    if "parking" in p.text.lower() and "available" in p.text.lower():
                        parking = 1


                row = [title,price,location,district,floor,room,bedroom,bathroom,livingroom,kitchen,parking,link]

                print(row)
                with open ("csv-files/99aana.csv",'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)

                print('-----------------------------------------------------------------------------')
                time.sleep(1)

    print('-----------------------------------------------------------------------------')
    print('99aana.csv generated')
    print('-----------------------------------------------------------------------------')

# This function is used to get the links to the individual pages where the housing details are stored.
# The links are stored in a csv file.
def get_links():

    for count in range(1,297):
        source = requests.get("https://99aana.com/properties/page/" + str(count) + "?_offer_type=sale&keyword_search&_listing&realteo_order=date-desc&_property_type=houses&_price_min&_price_max").text
        soup = BeautifulSoup(source,'lxml')
        links = [] # these contain the links to the pages where the housing details are stored
        listing_title = soup.findAll('div',class_="listing-title")
        for title in listing_title:
            link = title.find('a')['href']
            links.append(link)
            print(str(count) + ": " + link)
        with open('csv-files/99aana_links.csv','a',newline='') as f:
            writer = csv.writer(f)
            for l in links:
                writer.writerow([l])
        if count == 296:
            break

# function to check if there are any duplicate links in the csv links file for 99aana
def check_duplicate():
    with open('csv-files/99aana_links.csv') as f:
        stored_links = []
        reader = csv.reader(f)
        for row in reader:
            stored_links.append(row[0])
        if len(stored_links) == len(set(stored_links)):
            print("No duplicates here")