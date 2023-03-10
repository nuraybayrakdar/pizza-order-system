class Pizza:
    def __init__(self, name, descripton, price):
        self.name = name
        self.descripton = descripton
        self.price = price

    def get_descripton(self):
        print(self.descripton)
        """ return self.component.get_description() + \
         ' ' + Pizza.get_description(self)
        """

    def get_cost(self):
        print(self.price)
        """
        return self.component.get_cost() + \
         Pizza.get_cost(self)
       """


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
