from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
myurl ="https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
uClient=ureq(myurl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, features="html.parser")
containers = page_soup.find_all("div", {"class": "_2kHMtA"})
# container = containers[0]
# # print(soup.prettify(container))
#
# price = container.find_all("div",{"class": "col col-5-12 _2o7WAb"})
# print(price[0].text)
#
# ratings = container.find_all("div",{"class": "niH0FQ"})
# print(ratings[0].text)
#
# #
# # print(len(containers))
# print(container.div.img["alt"])

# Creating CSV File that will store all data
filename = "product1.csv"
f = open(filename, "w")

headers = "Product_Name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
    print(container)

    product_name = container.img["alt"]
    print(product_name)
    price_container = container.find_all("div", {"class": "col col-5-12 nlI3QM"})
    price = price_container[0].text.strip()
    print(price)
    rating_container = container.find_all("div", {"class": "gUuXy-"})
    ratings = rating_container[0].text
    print(ratings)
    # print("product_name:"+product_name)
    # print("price:"+price)
    # print("ratings:"+ str(ratings))

    edit_price = '?'.join(price.split('₹'))
    print((edit_price))
    sym_rupee = edit_price.split("?")
    add_rs_price = "Rs" + sym_rupee[1]
    split_price = add_rs_price.split("E")
    final_price = split_price[0]

    split_rating = str(ratings).split(" ")
    final_rating = split_rating[0]

    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")

f.close()
print(myurl)