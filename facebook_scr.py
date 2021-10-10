import facebook_scraper
import os
print(dir(facebook_scraper))
listphotos = []
a = 0
for photo in facebook_scraper.get_photos("nintendo",pages=2):
    a +=1
    if a>5: break
    for b in photo["images"]:
        print(b)
        listphotos.append(b)

