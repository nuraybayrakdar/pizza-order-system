
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
