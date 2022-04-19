import os

import numpy
import requests
from bs4 import BeautifulSoup
import django
import numpy as np

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sjtuer.settings")
django.setup()

from update.models import Newslist


def get_news_link_sjtu():
    url = "https://www.sjtu.edu.cn"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
    }
    resp = requests.get(url, headers=headers)
    page = BeautifulSoup(resp.text, 'html.parser')
    uls = page.find_all("ul", class_="uli14 nowrapli list-ondisc")
    h4s = page.find_all('h4', class_="add-list-title")
    params = []
    for ul, h4 in zip(uls[:2], h4s[:2]):
        title = h4.find("a").string
        lis = ul.find_all("li")
        for li in lis:
            text = li.text
            href = li.find("a")['href']
            params.append([title, text, href])
    title = h4s[2].find("a").string
    lis = uls[2].find_all("li")
    for li in lis:
        text = li.text.replace('\n', '').replace(' ', '')
        href = li.find("a")['href']
        params.append([title, text, href])
    resp.close()
    return params


def update_index_news():
    newslist = Newslist.objects.all()
    newslist.delete()
    new_newslist = get_news_link_sjtu()
    for news in new_newslist:
        Newslist.objects.create(title=news[0], info=news[1], href=news[2])


if __name__ == '__main__':
    update_index_news()
