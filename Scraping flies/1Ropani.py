import requests
from bs4 import BeautifulSoup
import csv
import sys

URL = "http://www.1ropani.com/House.aspx"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

data = []


Total_content = soup.findAll('div', {'class': 'list_desc'})


# filename = "aaba.csv"
# f = open(filename, "w")


# headers = "Location,Price,Area\n"
# f.write(headers)


for element in Total_content:
    # Final_Location=Price=Area= None
    New = element.findAll('b')
    print(New)
    sys.exit()
    Location = New[1].text
    print(Location, end=" ")
    Final_Location = Location[0].replace(',', '|')[0]
    for_seperation = New[0].text
    Price = for_seperation.split('|')[0]
    # print(Price,end=" ")
    Area = for_seperation.split('|')[1]
    # print(Area,end=" ")


# f.write(Final_Location.replace("|",",") +" ,"+Final_Price + " ,"+Final_Area +"\n")

    row = [Final_Location, Price, Area]
    data.append(row)
    print(row)
    print('............')


headers = ['Location', 'Price', 'Area']
with open('csv-flies/1Ropani.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)


# f.close()

