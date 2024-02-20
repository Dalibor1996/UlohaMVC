from shoe import Shoe
from model import ShoeModel
from controller import ShoeController
from view import ShoeView

def main():
    shoe_model = ShoeModel()
    shoe_controller = ShoeController(shoe_model)
    shoe_view = ShoeView()

    # Add some shoes to the model
    shoe_controller.add_shoe("Nike", 9, 120.00)
    shoe_controller.add_shoe("Adidas", 10, 100.00)
    shoe_controller.add_shoe("Converse", 8, 80.00)

    # Display all shoes
    shoe_view.display_all_shoes(shoe_controller.get_all_shoes())

    # Get shoes by size
    size_9_shoes = shoe_controller.get_shoes_by_size(9)
    shoe_view.display_all_shoes(size_9_shoes)

    # Get total price
    total_price = shoe_controller.get_total_price()
    shoe_view.display_total_price(total_price)

if __name__ == "__main__":
    main()
