class ShoeModel:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        if shoe not in self.shoes:
            self.shoes.append(shoe)

    def remove_shoe(self, shoe_id):
        for shoe in self.shoes:
            if shoe.id == shoe_id:
                self.shoes.remove(shoe)
                break

    def get_all_shoes(self):
        return self.shoes

    def get_shoes_by_size(self, size):
        return [shoe for shoe in self.shoes if shoe.size == size]

    def get_total_price(self):
        return sum(shoe.price for shoe in self.shoes)
