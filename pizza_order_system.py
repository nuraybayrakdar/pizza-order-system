import csv
import datetime

with open('Menu.txt', 'w') as f:
    f.write("* Please Choose a Pizza Base:\n")
    f.write("1: Classic\n")
    f.write("2: Margherita\n")
    f.write("3: TurkPizza\n")
    f.write("4: PlainPizza\n")
    f.write("* and sauce of your choice:\n")
    f.write("11: Olives\n")
    f.write("12: Mushrooms\n")
    f.write("13: GoatCheese\n")
    f.write("14: Meat\n")
    f.write("15: Onions\n")
    f.write("16: Corn\n")
    f.write("* Thank you!\n")

class Pizza:
    def __init__(self, name, descripton, price):
        self.name = name
        self.descripton = descripton
        self.price = price

    def get_descripton(self):
        print(self.descripton)
        # return self.description

    def get_cost(self):
        print(self.price)
        # returm self.price


class klasikPizza(Pizza):
    def __init__(self):
        super().__init__(
            "Klasik Pizza", "Domates, kaşar keyniri, mantar, sucuk, salam ve sosis", "60 ₺"
        )


class margaritaPizza(Pizza):
    def __init__(self):
        super().__init__('Margarita', "Mozarella, domates, fesleğen", "50 ₺")


class turkPizza(Pizza):
    def __init__(self):
        super().__init__('Türk Pizza', 'Sucuk, pastırma, biber, mantar', "45 ₺")


class sadePizza(Pizza):
    def __init__(self):
        super().__init__('Sade Peynirli', 'Parmesan, rokfor, kaşar, mozarella', "55 ₺")



klasikPizzam = klasikPizza()
margaritaPizzam = margaritaPizza()
turkPizzam = turkPizza()
sadePizzam = sadePizza()

klasikPizzam.get_descripton()
