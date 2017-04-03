import requests
from bs4 import BeautifulSoup
import urlparse

url = "https://www.walmart.com/ip/54649026"
imgurl = []
def imgget():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    og_image = (soup.find('meta', property='og:image') or
                        soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        print ''

    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        print ''

    for img in soup.findAll("img", src=True):

        if img["src"] not in imgurl:
            imgurl.append(img["src"])
    return map(str,imgurl)
