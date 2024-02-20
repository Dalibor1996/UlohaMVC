class ShoeView:
    def display_shoe(self, shoe):
        print(f"Shoe ID: {shoe.id}")
        print(f"Brand: {shoe.brand}")
        print(f"Size: {shoe.size}")
        print(f"Price: ${shoe.price:.2f}")

    def display_all_shoes(self, shoes):
        for shoe in shoes:
            self.display_shoe(shoe)

    def display_total_price(self, total_price):
        print(f"Total price: ${total_price:.2f}")
