from model import ShoeModel
from shoe import Shoe

class ShoeController:
    def __init__(self, shoe_model):
        self.shoe_model = shoe_model

    def add_shoe(self, brand, size, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        new_shoe = Shoe(len(self.shoe_model.shoes) + 1, brand, size, price)
        self.shoe_model.add_shoe(new_shoe)

    def remove_shoe(self, shoe_id):
        self.shoe_model.remove_shoe(shoe_id)

    def get_all_shoes(self):
        return self.shoe_model.get_all_shoes()

    def get_shoes_by_size(self, size):
        return self.shoe_model.get_shoes_by_size(size)

    def get_total_price(self):
        return self.shoe_model.get_total_price()
