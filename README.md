# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|TYp zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|indentyfikator opinii|div.js_product-review \["data-entry-id"\]|opinion_id|str|
|autor opinii|span.user-post__author-name|author|str|
|rekomendacja|span.user-post__author-recomendation > em|rekommendation|str|
|liczba gwiazdek|span.user-post__score-count|stars|str|
|treść opinii|div.user-post__text|content|str|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item|pros||
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|cons||
|dla ilu osób przydatna|span[id^="votes-yes"]|useful|str|
|dla ilu osób nieprzydatna|span[id^="votes-no"]|useless|str|
|data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date|str|
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|str|
