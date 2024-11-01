from requests import get

url = input("Paste your URL here: ")
resp = str( get(url).content )
title = resp[resp.find("<title>")+7 : resp.find("</title>")]
print(title)
