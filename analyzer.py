import os
import pandas as pd
print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")             #ta gwiazdka wypakowuje wartości z listy na osobne zmienne
product_id = input("Podaj indentyfikator produktu: ")

opinions = pd.read_json(f"opinions/{product_id}.json")
print(opinions)