#from src.customer import Customer

class Pub:

    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.drinks = []

    def add_drink_to_list(self, drink):
        self.drinks.append(drink)