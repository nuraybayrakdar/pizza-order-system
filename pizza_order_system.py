import csv
import datetime
# Menu.txt adlı bir dosya oluşturun ve içine aşağıdaki metni yazıyoruz.
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


# "Pizza" üst sınıfını oluşturuyoruz. 
class Pizza:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def get_description(self):
        return self.description

    def get_cost(self):
        print(self.price)
        return self.price

#Farkli pizza türleri için Pizza snıfından miras alan  alt sınıflar oluşturuyoruz.
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

classicPizzam.get_description()
margaritaPizzam.get_description()
turkishPizzam.get_description()
cheesePizzam.get_description()

# Tüm alt sos sınıflarının süper sınıfı olan decorator sınıfını oluşturuyoruz
class Decorators: 

    def __init__(self, extra, prices):
        self.extra = extra
        self.prices = prices

    def get_cost(self):
        return self.component.get_cost() + \
            Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
            + Pizza.get_description(self)


# Decorator sınıfının alt sınıfı olan sos sınıfları
class Zeytin(Decorators):  # soslar alt sınıfları
    def __init__(self):
        self.name = "Zeytin Sosu"
        self.ingredients = ["Zeytin"]
        self.price = 3

    def __str__(self):
        return self.name


class Mantar(Decorators):
    def __init__(self):
        self.name = "Mantar Sose"
        self.ingredients = ["Maetar"]
        self.price = 4

    def __str__(self):
        return self.name


class KeciPeyniri(Decorators):
    def __init__(self):
        self.name = "Keçi Peyniri Sosu"
        self.ingredients = ["Keçi Peyniri"]
        self.price = 5

    def __str__(self):
        return self.name


class Et(Decorators):
    def __init__(self):
        self.name = "Et Sosu"
        self.ingredients = ["Et"]
        self.price = 9

    def __str__(self):
        return self.name


class Sogan(Decorators):
    def __init__(self):
        self.name = "Soğan Sosu"
        self.ingredients = ["Soğan"]
        self.price = 6

    def __str__(self):
        return self.name


class Misir(Decorators):
    def __init__(self):
        self.name = "Mısır Sosu"
        self.ingredients = ["Mısır"]
        self.price = 2

    def __str__(self):
        return self.name

# menuyu ekrana yazdıracak method
def show_menu():
    # 'Menu.txt' dosyasını 'r' modunda açıyoruz
    with open('Menu.txt', 'r') as f:
        print(f.read())
    
    # kullanıcıdan pizza ve sos seçmesi için input 
    pizza_choice = input("Please choose a pizza base (1-4): ")
    sauce_choice = input("Please choose a sauce (11-16): ")
    
    #kullanıcıdan gelen inputu return ediyoruz
    return pizza_choice, sauce_choice

#show_menu() methodundan dönen değerlere göre fiyat hesapalama
def calculate_price(pizza_choice, sauce_choice):
    pizza = None
    sauce = None
    
    if pizza_choice == '1':
        pizza = classicPizzam
        
    elif pizza_choice == '2':
        pizza = margaritaPizzam
    elif pizza_choice == '3':
        pizza = turkishPizzam
    elif pizza_choice == '4':
        pizza = cheesePizzam
    if sauce_choice == '11':
        sauce = Zeytin()
    elif sauce_choice == '12':
        sauce = Mantar()
    elif sauce_choice == '13':
        sauce = KeciPeyniri()
    elif sauce_choice == '14':
        sauce = Et()
    elif sauce_choice == '15':
        sauce = Sogan()
    elif sauce_choice == '16':
        sauce = Misir()
   
    total_price = float(pizza.price.split()[0]) + sauce.price

    return total_price, pizza, sauce

#müşteridem isim, tc, card no, cvc, order date değerlerini aldığımuz method
def get_customer_info():

    total_price, pizza, sauce = calculate_price(*show_menu())
    print(pizza.description , sauce.name )

    name = input("Please enter your name: ")
    tc_no = input("Please enter your TC identity number: ")
    credit_card_number = input("Please enter your credit card number: ")
    credit_card_cvc = input("Please enter your credit card CVC number: ")
    now = datetime.datetime.now()
    order_time = now.strftime("%Y-%m-%d %H:%M:%S")

    #aldığımız inputu 'Orders_Database.csv' dosyasına append modunda ekliyoruz
    with open('Orders_Database.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, tc_no, credit_card_number, pizza.name + " with " + sauce.name, order_time, credit_card_cvc])

    print(f"Thank you for your order! Your total price is {total_price} ₺")


get_customer_info()

