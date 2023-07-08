from bs4 import BeautifulSoup
import time
from selenium import webdriver

'''dr = webdriver.Chrome()
dr.get("https://www.pararius.com/apartments/delft")
time.sleep(3)
soup = BeautifulSoup(dr.page_source, 'html.parser')

titles = soup.find_all(class_="listing-search-item__link listing-search-item__link--title")

dr.get("https://www.pararius.com/apartments/delft/page-2")
soup = BeautifulSoup(dr.page_source, 'html.parser')
for title in soup.find_all(class_="listing-search-item__link listing-search-item__link--title"):
    titles.append(title)

titles = list(titles)
print(len(titles))'''

def pararius_initial_link(filters):
    link = "https://pararius.com/apartments/" + filters["city"].lower()
    priceRange = "/" + str(filters["minPrice"]) + "-" + str(filters["maxPrice"])
    if filters["rooms"] != 1:
        rooms = "/" + str(filters["rooms"]-1) + "-bedrooms"
    else :
        rooms = ""
    if filters["interior"].lower()=="unfurnished":
        filters["interior"]="upholstered"
    interiorType = "/" + filters["interior"].lower()
    size = "/" + str(filters["size"]) + "m2"
    link+=priceRange + rooms + interiorType + size
    return link

def get_pararius_links(filters) :
    dr = webdriver.Chrome()
    initialLink = pararius_initial_link(filters)
    print(initialLink)
    dr.get(initialLink)
    time.sleep(5) 
    soup = BeautifulSoup(dr.page_source, 'html.parser')

    links=[]
    infos = soup.find_all(class_="listing-search-item__info")
    index=0
    for apartment in soup.find_all(class_="listing-search-item__link listing-search-item__link--title") :
        if infos[index].a.text!="Björnd Makelaardij":
                links.append(apartment["href"])
        index+=1
        

    pages = soup.find_all(class_="pagination__item")
    if len(pages)>=3:
        lastPageNo = pages[len(pages)-2].a["data-page"]
    else : 
        lastPageNo = 1  
    for pageNo in range(2, int(lastPageNo) + 1) :
        dr.get(initialLink + "/page-" + str(pageNo))
        soup = BeautifulSoup(dr.page_source, 'html.parser')
        infos = soup.find_all(class_="listing-search-item__info")
        index=0
        for apartment in soup.find_all(class_="listing-search-item__link listing-search-item__link--title") :
            if infos[index].a.text!="Björnd Makelaardij":
                links.append(apartment["href"])
            index+=1
    return links

def get_pararius_apartments(filters) :
    apartments = []
    counter=0
    links = get_pararius_links(filters)
    dr = webdriver.Chrome()
    for link in links:
        link = "https://pararius.com" + link
        dr.get(link)
        print(link)
        counter+=1
        if counter==1:
            time.sleep(2)
        soup = BeautifulSoup(dr.page_source, 'html.parser')
        if validate_apartment(soup):
            address = soup.find(class_="listing-detail-summary__location").text
            name = soup.find(class_="listing-detail-summary__title").text
            price = soup.find(class_="listing-detail-summary__price").contents[0].strip()
            roomNo = soup.find(class_="illustrated-features__item illustrated-features__item--number-of-rooms").text
            size = soup.find(class_="illustrated-features__item illustrated-features__item--surface-area").text
            image = soup.find(class_="picture__image")["src"]
            #check if number of rooms is strictly equal to the requested number
            if roomNo[0] == str(filters["rooms"]):
                apartments.append(Apartment(link,image,name,address,price,roomNo,size))
    return apartments           

def validate_apartment(soup):
    for elem in soup.find_all("p") + soup.find_all("li"):
        if not_for_students(elem.text):
            return False
    return True

#check if text inside the advert contains strings that exclude students
def not_for_students(text):
    gatekeep_list = ["no students", "not for students", "no student", "not suitable for students"]
    if any(gatekeeper in text.lower() for gatekeeper in gatekeep_list):
        return True
    return False

class Apartment:
    def __init__(self, link, image, name, address, price, roomNo, size):
        self.link = link
        self.image = image
        self.name = name
        self.address = address
        self.price = price
        self.roomNo = roomNo
        self.size = size

    def printApartment(self):
        print("Name: ", self.name, ", Address: ", self.address, ", Price: ", self.price, ", Rooms: ", self.roomNo, ", Size: ", self.size, ", Image: ", self.image)