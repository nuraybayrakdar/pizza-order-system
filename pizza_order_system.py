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

    classicPizzam = classicPizza()
    margaritaPizzam = margaritaPizza()
    turkishPizzam = turkishPizza()
    cheesePizzam = cheesePizza()

    classicPizzam.get_descripton()
    margaritaPizzam.get_descripton()
    turkishPizzam.get_descripton()
    cheesePizzam.get_descripton()

class Decorators: #soslar üst sınıf
    def  __init__(self, extra, prices):
        self.extra = extra
        self.prices = prices
    def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)


    def get_description(self):
       return self.component.get_description() + \
          + Pizza.get_description(self)

class Zeytin: #soslar alt sınıfları
    def __init__(self):
        self.name = "Zeytin Sosu"
        self.ingredients = ["Zeytin"]
        self.price = 3

    def __str__(self):
        return self.name

class Mantar:
    def __init__(self):
        self.name = "Mantar Sosu"
        self.ingredients = ["Mantar"]
        self.price = 4

    def __str__(self):
        return self.name

class KeciPeyniri:
    def __init__(self):
        self.name = "Keçi Peyniri Sosu"
        self.ingredients = ["Keçi Peyniri"]
        self.price = 5

    def __str__(self):
        return self.name

class Et:
    def __init__(self):
        self.name = "Et Sosu"
        self.ingredients = ["Et"]
        self.price = 9

    def __str__(self):
        return self.name

class Sogan:
    def __init__(self):
        self.name = "Soğan Sosu"
        self.ingredients = ["Soğan"]
        self.price = 6

    def __str__(self):
        return self.name

class Misir:
    def __init__(self):
        self.name = "Mısır Sosu"
        self.ingredients = ["Mısır"]
        self.price = 2

    def __str__(self):
        return self.name



