import urllib.request as ureq
from bs4 import BeautifulSoup as soup
uop=ureq.urlopen("http://books.toscrape.com/")
uread=uop.read()
uop.close()
usouped=soup(uread,'html.parser')
contain=usouped.findAll("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
filename="products.csv"
f=open(filename,"w")
headers="Book_Name,Pricing,Ratings,Avalibility\n"
f.write(headers)
i=0

for contai in contain:
    Book_name=contai.div.img["alt"]

    price_contain=usouped.findAll("p",{"class":"price_color"})
    price=price_contain[i].text

    rateing=contai.article.p["class"]

    avilable=usouped.findAll("p",{"class":"instock availability"})
    avi=avilable[i].text.strip()

    print("Book_Name:"+Book_name)
    print("Price:"+price)
    print("Rating:"+rateing[1])
    print("Availability:"+avi)
    i += 1
