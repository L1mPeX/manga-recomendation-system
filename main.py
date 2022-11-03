from mangalib_api import MangaLibApi

api = MangaLibApi()

d = api.getManga(id="ore-no-genjitsu-wa-renai-game-ka-to-omottara-inochigake-no-game-datta")
print(d['similar'])

api.closeApi()
