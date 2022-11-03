import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


class MangaLibApi:
    def __init__(self):
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def getManga(self, name="", id=""):
        if id == "":
            id = self._getSpecName_(name)
            if id is None:
                return None

        self.driver.get(f'https://mangalib.me/{id}')
        soup = BeautifulSoup(self.driver.page_source, features="html.parser")
        if len(soup.select(".media-sidebar__cover img")) == 0:
            return None
        img = soup.select(".media-sidebar__cover img")[0]['src']
        name = soup.select(".media-name__main")[0].text
        desc = soup.select(".media-description__text")[0].text.replace("\n", "").lstrip().rstrip()
        rate = float(soup.select(".media-rating__value")[0].text)
        tags = [x.text for x in soup.select(".media-tag-item")]
        similar = [x.text.lstrip().rstrip().replace("\n", "") for x in soup.select(".manga-list-item__name")]
        try:
            chapterCount = soup.find_all("div", string="Загружено глав")[0].parent.find_all('div')[1].text
        except:
            chapterCount = 0
        try:
            typeM = soup.find_all("div", string="Тип")[0].parent.find_all('div')[1].text
        except:
            typeM = "Манга"

        return {'name': name, 'chapterCount': chapterCount, 'desc': desc, 'rate': rate, 'tags': tags, 'similar': similar, 'img': img, 'typeM': typeM}

    def _getSpecName_(self, name):
        mangas = json.loads("".join(open("mangas.json", "r", encoding="UTF-8").readlines()))
        if name in mangas:
            return mangas[name]
        return None

    def getMangaList(self, sort, direction, page):
        """
        Return mangas list
        :param sort: Sort by (rate, chap_count, name, created_at, views, last_chapter_at)
        :param direction: Dir (desc, asc)
        :param page: Page number
        """
        mangas = []
        self.driver.get(f'https://mangalib.me/manga-list?sort={sort}&dir={direction}&page={page}')
        soup = BeautifulSoup(self.driver.page_source, features="html.parser")
        for x in soup.find_all("h3", {'class': "media-card__title line-clamp"}):
            mangas.append({"name": x.text, "id": x.parent.parent['data-src'].split("/")[5]})
        return mangas

    def closeApi(self):
        self.driver.close()
        self.driver.quit()


class Manga:
    def __init__(self, name, chapterCount, desc, rate, tags, similar, imgUrl, typeM):
        self.name = name
        self.chapterCount = chapterCount
        self.chapterCount = chapterCount
        self.desc = desc
        self.rate = rate
        self.tags = tags
        self.similar = similar
        self.imgUrl = imgUrl
        self.typeM = typeM

    def __str__(self):
        return {'name': self.name, 'chapterCount': self.chapterCount, 'desc': self.desc, 'rate': self.rate, 'tags': self.tags, 'similar': self.similar, 'tags': self.tags, 'imgUrl': self.imgUrl}
