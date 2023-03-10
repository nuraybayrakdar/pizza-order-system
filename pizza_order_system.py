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


class classicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", "Tomato, Cheddar Cheese, Mushroom, Sausage, Salami and Sausage", "60 ₺")


class margaritaPizza(Pizza):
    def __init__(self):
        super().__init__('Margarita', "Mozzarella, tomato, basil", "50 ₺")


class turkishPizza(Pizza):
    def __init__(self):
        super().__init__('Turkish Pizza', 'Sausage, bacon, pepper, mushroom', "45 ₺")


class cheesePizza(Pizza):
    def __init__(self):
        super().__init__('Cheese Pizza', 'Parmesan, Roquefort, Cheddar, Mozzarella', "55 ₺")

class Decorators:
    def  __init__(self, extra, prices):
        self.extra = extra
        self.prices = prices

extra = {"Ketchup:": 3, "Mushroom": 5, "Goat Cheese": 9, "Meat": 7, "Onion": 4, "Corn": 3,}




klasikPizzam = classicPizza()
margaritaPizzam = margaritaPizza()
turkishPizzam = turkishPizza()
cheesePizzam = cheesePizza()

klasikPizzam.get_descripton()
