# Быстрый экскурс

<b> Для удобства далее манг, манхва, маньхуа и т.п. будет называться одним словом - манга <\b>

1. Откройте мангу на mangalib
2. В адресной строке скопируйте ID манги:
```
В данном случае ID: ore-no-genjitsu-wa-renai-game-ka-to-omottara-inochigake-no-game-datta
https://mangalib.me/ore-no-genjitsu-wa-renai-game-ka-to-omottara-inochigake-no-game-datta/v12/c48?page=46
```
```python
d = api.getManga(id="")
```
3. Вам выведутся похожие тайтлы

Необходимые библиотеки
```
1)  beautifulsoup4
2)  requests
3)  lxml
4)  selenium
5)  chromedriver_binary
6)  webdriver-manage
7)  packaging
```

Была попытка создать свой тип данных для параметров манги, если кому понадобиться, то вот его структура:
```
Manga:
    name
    chapterCount
    desc
    rate
    tags
    similar
    imgUrl
    typeM (Манга, Маньхуа, Манхва, Комикс и тп)
```
