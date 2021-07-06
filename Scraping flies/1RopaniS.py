import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import time




# Edited by sanoj

# function to get links from the 1Ropani website
def get_links():
    count = 1
    header = ['links']
    links = []
    driver = webdriver.Chrome('C:\Program Files (x86)\Chromedriver\chromedriver.exe')
    URL = "http://www.1ropani.com/House.aspx"
    driver.get(URL)
    select = driver.find_element_by_id('ContentPlaceHolder1_HouseListControl1_ItemsPerPageDropDownList')
    all_options = select.find_elements_by_tag_name("option")
    for option in all_options:
        if option.text == '100':
            option.click()
            time.sleep(6)
            
            # first row and last row contains navigation links and all inbetween contains the house links
            # get all links from the navigation table and store it in a csv file named as 1Ropani_links.csv
            

    for i in range(1,8):

        pagination = driver.find_element_by_class_name('search_result_pagi')
        indexes = pagination.find_elements_by_tag_name('a')
        for index in indexes:
            if index.text == str(i):
                index.click()
                time.sleep(6)
                break
    
        table = driver.find_element_by_id('ContentPlaceHolder1_HouseListControl1_GridView1')
        table_rows = table.find_elements_by_tag_name('tr')
        for row in table_rows[2:-2]:
            link = []
            link.append(row.find_element_by_tag_name('a').get_attribute('href'))
            print("Number: " + str(count) + " : " + link[0])
            count = count + 1
            links.append(link)
                


            #save links in a csv file named as 1Ropani_links.csv
    with open('csv-files/1Ropani_links.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(links)




get_links()
