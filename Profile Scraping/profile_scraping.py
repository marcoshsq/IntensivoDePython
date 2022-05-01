import requests
from bs4 import BeautifulSoup as bs

user_name = input("Enter a github user name: \n")
url = "https://github.com/" + user_name
r = requests.get(url)
scrap = bs(r.content, "html.parser")
profile_image = scrap.find("img", {"alt": "Avatar"})["src"]
print(profile_image)
