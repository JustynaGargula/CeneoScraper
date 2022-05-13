#from logging.config import _OptionalDictConfigArgs
import requests
import json
from bs4 import BeautifulSoup
#from soupsieve import select

def get_item(ancestor, selector, attribute=None, return_list=False):
    try:
        if return_list:
            return [item.get_text().strip() for item in ancestor.select(selector)]
        if attribute:
            return ancestor.select_one(selector)[attribute]
        return ancestor.select_one(selector).get_text().strip()
    except (AttributeError, TypeError):
        return None 

selectors = {
    "author": ["span.user-post__author-name"],
    "recommendation": ["span.user-post__author-recomendation > em"],
    "stars": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "useful": ['span[id^="votes-yes"]'],
    "useless": ['span[id^="votes-no"]'],
    "publish_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date": ["span.user-post__published > time:nth-child(2)","datetime"],
    "pros": ["div.review-feature__title--positives ~ div.review-feature__item", None, True],
    "cons": ["div.review-feature__title--negatives ~ div.review-feature__item", None, True]

}

product_code = input("podaj kod produktu ")
url = "https://www.ceneo.pl/"+product_code+"#tab=reviews"
all_opinions = []
while(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    opinions = page.select("div.js_product-review")
    for opinion in opinions:
        
        single_opinion = {
            key:get_item(opinion, *value)                             #ta gwiazdka wypakowuje wartości z listy na osobne zmienne
                for key, value in selectors.items()
        }
        single_opinion["opinion_id"] = opinion["data-entry-id"]
        all_opinions.append(single_opinion)

    try:
        url = "https://www.ceneo.pl"+get_item(page, "a.paginaton__next", "href")
    except TypeError:
        url = None

with open("opinions/"+product_code+".json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)

    #print(recommendation, stars, content, useful, useless, publish_date, purchase_date)