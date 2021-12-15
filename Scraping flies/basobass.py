from re import L
from typing import Counter
from selenium import webdriver
import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
# implement headless mode
chrome_options = Options()

chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
# browser = webdriver.Chrome('C:\Program Files (x86)\Chromedriver\chromedriver.exe')


#funtion to get all the links of houses from basobass.com
def get_links():
    counter = 0
    click_counter = 0
    links = []
    #open the website
    url = "https://basobaas.com/properties/for-sale/residential/house"
    browser.get(url)

    while(True):
        try:
            # load_more_btn = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'loadingBtn')))
            load_more_btn = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID,'loadingBtn')))
            load_more_btn.click()
            click_counter = click_counter + 1
            print('Clicked: ',click_counter)

        except:
            pass
        if 'no more properties' in load_more_btn.text.lower():
            print('Reached the end of the file!!!!!!!!!')
            break
    #find all the links
    houses = browser.find_elements_by_class_name('padding-right-remove')
    for house in houses:
        try:
            link = house.find_element_by_tag_name('a').get_attribute('href')
            links.append(link)
            counter = counter + 1
            print(counter, ': ',link)
        except:
            continue
    # store the links on a csv file
    with open('csv_files/links/basobass_links.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        for l in links:
            writer.writerow([l])
    print('csv file created')
get_links()

