from bs4 import BeautifulSoup
import csv
import requests
# Get data from hamrobazar.com


url = 'https://hamrobazaar.com/c113-real-estate-for-sale-house?catid=113&order=popularad&offset=0'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml').text
# Get all the links from soup
print(soup)
