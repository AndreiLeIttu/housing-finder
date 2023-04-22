from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

dr = webdriver.Chrome()
dr.get("https://www.pararius.com/apartments/delft")
time.sleep(5)
soup = BeautifulSoup(dr.page_source, 'html.parser')

titles = soup.find_all(class_="listing-search-item__link listing-search-item__link--title")

for title in titles: 
    print(title['href'])


class Apartment:
    def __init__(self, link, name, address, price, roomNo, size, description):
        self.link = link
        self.name = name
        self.address = address
        self.price = price
        self.roomNo = roomNo
        self.size = size
        self.description = description