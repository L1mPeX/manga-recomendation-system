from mangalib_api import MangaLibApi

api = MangaLibApi()

d = api.getManga(id="")
print(d['similar'])

api.closeApi()
