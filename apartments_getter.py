from bs4 import BeautifulSoup
import time
from selenium import webdriver

dr = webdriver.Chrome()
dr.get("https://www.pararius.com/apartments/delft")
time.sleep(3)
soup = BeautifulSoup(dr.page_source, 'html.parser')

titles = soup.find_all(class_="listing-search-item__link listing-search-item__link--title")

dr.get("https://www.pararius.com/apartments/delft/page-2")
soup = BeautifulSoup(dr.page_source, 'html.parser')
for title in soup.find_all(class_="listing-search-item__link listing-search-item__link--title"):
    titles.append(title)

titles = list(titles)
print(len(titles))

def pararius_link(filters):
    link = "https://pararius.com/apartments/" + filters["city"]
    priceRange = "/" + filters["minPrice"] + "-" + filters["maxPrice"]
    rooms = "/" + filters["rooms"] + "-bedrooms"
    interiorType = "/" + filters["interior"]
    size = "/" + filters["size"] + "m2"
    link+=priceRange + rooms + interiorType + size
    return link

def get_from_pararius(filters) :
    dr = webdriver.Chrome()
    initialLink = pararius_link(filters)
    dr.get(initialLink)
    time.sleep(3) 
    soup = BeautifulSoup(dr.page_source, 'html.parser')

    links=[]

    for apartment in soup.find_all(class_="listing-search-item__link listing-search-item__link--title") :
        links.append(apartment["href"])

    pages = soup.find_all(class_="pagination__item")
    if len(pages)>=3 :
        lastPageNo = pages[len(pages)-2]["data-page"]
    else : 
        lastPageNo = 1  
    for pageNo in range(2, lastPageNo + 1) :
        dr.get(initialLink + "/page-" + pageNo)
        soup = BeautifulSoup(dr.page_source, 'html.parser')

        for apartment in soup.find_all(class_="listing-search-item__link listing-search-item__link--title") :
            links.append(apartment["href"])
    
    return links
    

class Apartment:
    def __init__(self, link, name, address, price, roomNo, size, description):
        self.link = link
        self.name = name
        self.address = address
        self.price = price
        self.roomNo = roomNo
        self.size = size
        self.description = description