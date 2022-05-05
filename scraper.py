#from logging.config import _OptionalDictConfigArgs
import requests
import json
from bs4 import BeautifulSoup
#from soupsieve import select
product_code = input("podaj kod produktu ")
url = "https://www.ceneo.pl/"+product_code+"#tab=reviews"
all_opinions = []
while(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    opinions = page.select("div.js_product-review")
   
    for opinion in opinions:
        #opinion = opinions.pop(0)
        opinion_id = opinion["data-entry-id"]
        author = opinion.select_one("span.user-post__author-name").get_text().strip()            #get_text ma nawiasy bo jest funkcją,    strip() usuwa ze zmiennej zbędne znaki białej
        try:
            recommendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
        except AttributeError:
            recommendation = None 
        stars = opinion.select_one("span.user-post__score-count").get_text().strip()
        content = opinion.select_one("div.user-post__text").get_text().strip()
        useful = opinion.select_one('span[id^="votes-yes"]').get_text().strip()
        useless = opinion.select_one('span[id^="votes-no"]').get_text().strip()
        publish_date = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
        try:
            purchase_date = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]
        except TypeError:
            purchase_date = None 

        pros = opinion.select("div.review-feature__title--positives ~ div.review-feature__item")
        pros = [item.get_text().strip() for item in pros]
        cons = opinion.select("div.review-feature__title--negatives ~ div.review-feature__item")
        cons = [item.get_text().strip() for item in cons]

        single_opinion = {
            "opinion_id": opinion_id,
            "author": author,
            "recommendation": recommendation,
            "stars": stars,
            "content": content,
            "useful": useful,
            "useless": useless,
            "publish_date": publish_date,
            "purchase_date": purchase_date,
            "pros": pros,
            "cons": cons

        }
        all_opinions.append(single_opinion)

    try:
        url = "https://www.ceneo.pl"+page.select_one("a.paginaton__next")["href"]
    except TypeError:
        url = None

with open("opinions/"+product_code+".json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)

    #print(recommendation, stars, content, useful, useless, publish_date, purchase_date)