import csv
import datetime

class pizza:
    def __init__(self, name,materials, price):
        self.name = name
        self.materials= materials
        self.price = price
    
    def describe(self):
        print(f"{self.name}: {', ' .join(self.materials)}, {self.price}₺")

klasik = pizza("Klasik Pizza", ["Domates", "kaşar keyniri", "mantar","sucuk","salam", "sosis",], 60)
margarita = pizza("Margarita", ["Mozarella", "domates", "fesleğen"], 50)
turkPizza = pizza("Türk Pizza", ["Sucuk","pastırma","biber","mantar",], 45)
sade = pizza("Sade Peynirli", ["Parmesan", "rokfor", "kaşar", "mozarella"], 55)

klasik.describe()
margarita.describe()
turkPizza.describe()
sade.describe()

