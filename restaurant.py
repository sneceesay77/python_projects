class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Name of restaurant {self.restaurant_name} Cuisine type {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is opened")
    
    def set_restaurant_name(self, new_name):
        self.restaurant_name = new_name

restaurant = Restaurant("Chicken Plaza", "Fried Chicken")
print(f"\nRestaurant Name: {restaurant.restaurant_name.title()} \nCuisine Type: {restaurant.cuisine_type.title()}")
print("====================================================")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_restaurant_name("Ali Baba")
restaurant.describe_restaurant()


class BigRestaurant(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

print("===============================================================")
restaurant_play = BigRestaurant("Play and Chop Center", "Chicken, Asian, Mexican, African")
restaurant_play.describe_restaurant()


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
    
    def display_flavours(self):
        for flavour in self.flavours:
            print(f"- {flavour}")

flavours = ["Vanilla", "Strawberry", "Choclate"]
icecream_restaurant = IceCreamStand("B and K Ice Cream Stand", "Ice Cream", flavours)
icecream_restaurant.display_flavours()