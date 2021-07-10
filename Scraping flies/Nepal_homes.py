#scrape links from Nepalhomes.com
import selenium
import csv
import time
from selenium import webdriver
from selenium.webdriver.common import touch_actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# implement headless mode
chrome_options = Options()

chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

#open a new browser

count = 1 # need to loop this to 135 times. Each pagte contains 8 links
for count in range(44, 135):
    links = []
    url = "https://www.nepalhomes.com/list/&sort=1&page=" + str(count) + "&is_project=&agency_id=&find_district_id=&find_area_id=&find_property_category=5d660cb27682d03f547a6c4a&find_property_type=5d70b3df4139ae34c8fbab94&find_property_purpose=5db2bdb42485621618ecdae6"
    driver.get(url) #open the url
    table = driver.find_element_by_class_name('table-list')
    a_tags = table.find_elements_by_tag_name('a') #get all a tags in table
    for a_tag in a_tags:
        link = a_tag.get_attribute('href')
        links.append(link)
    with open('csv-files/nepal_homes_links.csv','a',newline='') as f:
        writer = csv.writer(f)
        # write links on csv file
        for link in links:
            writer.writerow([link])



