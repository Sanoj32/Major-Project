from logging import exception
from typing import Text
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import csv
from selenium import webdriver 
PATH = "C:/ProgramData/Anaconda3/scripts/chromedriver.exe" #always keeps chromedriver.exe inside scripts to save hours of debugging
driver =webdriver.Chrome(PATH) #preety important part
driver.get("https://www.gharghaderi.com/")
driver.implicitly_wait(10)
house = driver.find_elements_by_class_name('griddetails')
for x in house:
   print(x.text)
   house_list = []
house = driver.find_elements_by_class_name('griddetails')
for x in house:
   house_list.append(x.text)
data = {
         'Details': house_list
        }
df = pd.DataFrame.from_dict(data)
df.to_csv('housingprices.csv')
driver.implicitly_wait(20)
driver.get("https://www.gharbazar.com/property/search/?_q=&_vt=1&_r=0&_pt=residential&_si=0&_srt=latest")
links = driver.find_elements_by_xpath("//div[@id = 'search-properties']/a")
for ele in links:
   print(ele.get_attribute('href'))
page= 2
pagelinks= []
    #links of the 1st page
links = driver.find_elements_by_xpath("//div[@id = 'search-properties']/a")
for ele in links:
        pagelinks.append(ele.get_attribute('href'))

while True:
        nextoption = driver.find_element_by_xpath("//div[@id='pagination-div']//a[contains(text(),'>>')]")
        driver.execute_script("arguments[0].scrollIntoView(true);",nextoption)
        driver.execute_script("window.scrollBy(0,-300)")
        time.sleep(5)
        try:
            driver.find_element_by_link_text(str(page)).click()
            page += 1
            links = driver.find_elements_by_xpath("//div[@id = 'search-properties']/a")
            for ele in links:
                pagelinks.append(ele.get_attribute('href'))
            time.sleep(3)

        except Exception as e:
            print(e)
            break
print(len(pagelinks))
for i in range(len(pagelinks)):
        print(pagelinks[i])
data = {
         'Links':pagelinks 
        }
df = pd.DataFrame.from_dict(data)
df.to_csv('housinglinks.csv', index = 0)  

