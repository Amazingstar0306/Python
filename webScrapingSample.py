import bs4
import requests

res = requests.get("https://www.javatpoint.com/")
print("The object type:", type(res))

# Convert the request object to the Beautiful Soup Object
soup = bs4.BeautifulSoup(res.text, 'html5lib')
print("The object type:", type(soup))
soup.select('.homecontent')
##for i in soup.select('.homecontent'):
   ## print(i.text, end = ',')
print(soup.title.text)
for item in soup.find_all("a"):
    print("inner text is : {}".format(item.text))
    print("title is : {}" .format(item.get("title")))
    print("link is : {}" . format(item.get("href")))