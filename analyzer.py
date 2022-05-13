import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")             #ta gwiazdka wypakowuje wartości z listy na osobne zmienne
product_id = input("Podaj indentyfikator produktu: ")

opinions = pd.read_json(f"opinions/{product_id}.json")
# print(opinions)

opinions.stars = opinions.stars.map(lambda x: float(x.split("/")[0].replace(",",".")))
opinion_count = len(opinions.index)
#opinion_count = opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
average_score = opinions.stars.mean().round(2)      #mean liczy średnią, round zaokrągla do dwóch miejsc po przecinku

recommendation = opinions.recommendation.value_counts(dropna = False).sort_index().reindex(["Nie polecam", "Polecam", "None"])
recommendation.plot.pie(
    label="", 
    autopct="%1.1f%%", #autopct - liczba rzeczywista z precyzją do jednego miejsca po przecinku wyrażona w procentach
    colors=["crimson", "forestgreen", "lightskyblue"],
    labels = ["Nie polecam", "Polecam", "Nie mam zdania"]       
    )
plt.title("Rekomendacja")
plt.savefig(f"plots/{product_id}_recommendations.png")
plt.close()      #okienko samo się nie zamknie, tylko my ręcznie zamykamy

stars = opinions.stars.value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
stars.plot.bar()
plt.xticks(rotation=0)
plt.title("Oceny produktu")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.grid(True)
plt.savefig(f"plots/{product_id}_stars.png")