class Shoe:
    def __init__(self, id, brand, size, price):
        self.id = id
        self.brand = brand
        self.size = size
        self.price = price

    def __str__(self):
        return f"Shoe(id={self.id}, brand={self.brand}, size={self.size}, price={self.price})"
