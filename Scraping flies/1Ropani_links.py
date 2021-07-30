import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import time
import sys
import os

# function to get links from the 1ropani website
def get_links():
    count = 1
    header = ['links']
    links = []
    browser = webdriver.Chrome('C:\Program Files (x86)\Chromedriver\chromedriver.exe')
    URL = "http://www.1ropani.com/House.aspx"
    browser.get(URL)
    select = browser.find_element_by_id('ContentPlaceHolder1_HouseListControl1_ItemsPerPageDropDownList')
    all_options = select.find_elements_by_tag_name("option")
    #set the results to 100 results per page
    for option in all_options:
        if option.text == '100':
            option.click()
            time.sleep(6)

            # first row and last row contains navigation links and all inbetween contains the house links
            # get all links from the navigation table and store it in a csv file named as 1ropani_links.csv

    # looping throuh 7 pages after setting 100 results per page.
    for i in range(1,8):
        pagination = browser.find_element_by_class_name('search_result_pagi')
        indexes = pagination.find_elements_by_tag_name('a')
        for index in indexes:
            if index.text == str(i):
                index.click()
                time.sleep(20)
                break

        table = browser.find_element_by_id('ContentPlaceHolder1_HouseListControl1_GridView1')
        table_rows = table.find_elements_by_tag_name('tr')
        for row in table_rows[2:-2]:
            link = []
            link.append(row.find_element_by_tag_name('a').get_attribute('href'))
            # check if the link contains apartment and skip if it is an apartment
            if 'apartment' in link[0].lower():
                continue
            print("Number: " + str(count) + " : " + link[0])
            count = count + 1
            links.append(link)



    #save links in a csv file named as 1ropani_links.csv
    with open('csv_files/1ropani_links.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(links)



def ek_ropani():

    # get links from 1ropani_links.csv
    links = []
    with open('../csv_files/links/1ropani_links.csv', 'r') as f:
        reader = csv.reader(f)
        # start from 2nd item
        for row in reader:
            links.append(row[0])

    # #check if 1ropani is empty
    with open ("../csv_files/raw/1ropani.csv",'r', newline='',encoding="utf-8") as f:
        reader = csv.reader(f)
        if list(reader) == []:
            write_headers()
    #slicing to remove column name
    links = links[1:]

    # store links in csv 1ropani.csv in stored_links vaiable

    with open('../csv_files/raw/1ropani.csv', 'r') as f:
        reader = csv.reader(f)
        stored_links = []
        for row in reader: stored_links.append(row[-1])
    for link in links:
        if link not in stored_links:
            print(links.index(link))
            source = requests.get(link).text
            soup = BeautifulSoup(source, 'lxml')
            soup = soup.find('div',{'id':'property_detail'})
            title = soup.find('h2').get_text(strip=True)
            if 'commercial' in title.lower():
                continue
            print(links.index(link))
            price = soup.find('span',{'class':'price'}).get_text(strip=True).split('|')[0]
            if "on call" in price:
                continue
            else:
                price = price.split('Rs.')[1].strip()
            location = soup.find('td',attrs = {'style' : 'width: 200px; padding-left: 5px; padding-right: 15px;'}).get_text(strip=True).split('Land Description:')[0].split(':')[1]
            district = location.split(',')[0]
            area = soup.find('td',attrs = {'style' : 'width: 200px; padding-left: 5px; padding-right: 15px;'}).get_text(strip=True).split('Price:')[0].split('Area:')[1].strip()
            if(area == ''): #skip the house without area
                print('!!!!!!!!!!!!!!!!!!!!!')
                print('Empty area',link)
                print('!!!!!!!!!!!!!!!!!!!!!')
                continue
            #feature_list = ul with floor, bedroom, bath, kitchen, living room
            feature_list = soup.find('ul',{'class':'feature_list'})
            for li in feature_list.find_all('li'):
                if 'floor' in li.get_text().lower():
                    floor = li.get_text(strip=True)
                if 'bed' in li.get_text().lower():
                    bedroom = li.get_text(strip=True)
                if 'bath' in li.get_text().lower():
                    bathroom = li.get_text(strip=True)
                if 'living' in li.get_text().lower():
                    livingroom = li.get_text(strip=True)
                if 'kitchen' in li.get_text().lower():
                    kitchen = li.get_text(strip=True)
            print("Price: ",price)
            print('area: ',area)
            print("district: ",district)
            print('location: ',location)
            print("Title: ", title)
            print("floor: ",floor)
            print("bedroom: ",bedroom)
            print("livingroom: ",livingroom)
            print("bathroom: ",bathroom)
            print("link",link)

            if 'parking' in soup.text.lower():
                parking = 1
            else:
                parking = 0
            print(parking)
            room = None # It does not provide total rooms
            print('----------------------------------------------------------------')
            row = [title,price,area,location,district,floor,room,bedroom,bathroom,livingroom,kitchen,parking,link]
            with open ("../csv_files/raw/1ropani.csv",'a', newline='',encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(row)

def write_headers():
        headers = ['title','price','area','location','district','floor','room','bedroom','bathroom','livingroom','kitchen','parking','link']
        with open('../csv_files/raw/1ropani.csv', 'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

write_headers()
ek_ropani()

