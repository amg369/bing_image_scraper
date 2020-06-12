from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
    search = input("Search for:")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    # Make directory for each inputted search term
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    # Parse bing image searches
    url = "http://www.bing.com/images/search"
    r = requests.get(url,params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class":"thumb"})

    # Saves images in new directory
    for item in links:
       try:
            img_obj = requests.get(item.attrs["href"])
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            bytes = BytesIO(img_obj.content)
            try:
                img = Image.open(bytes)
                img.save("./" + dir_name + "/" + title, img.format)
            except:
                print("Could not save image")
       except:
           print("Could not request image")
    StartSearch()

StartSearch()
