class Restaurant:

    def __init__ (self, name, app, capacity):
        self.name = name
        self.menu = []
        self.reviews = []
        self.prices = []  # This is probably part of the menu
        self.contact = {} # Phone, email, ...
        self.app = app # Link to app
        self.capacity = capacity

    def __str__ (self):
        return f"{self.name} - App: {self.app} \
Menu items: {len(self.menu)} \
Price range: {self.calculate_price_range()} \n\
{self.convert_menu_to_str()}"

    # Inputs: None
    # Process: Loop through menu items find the min and the max
    # Output: String: Min-Max
    def calculate_price_range (self):
        min_price = 999999999
        max_price = 0
        for menu_item in self.menu:
            if menu_item.price < min_price:
                min_price = menu_item.price
            if menu_item.price > max_price:
                max_price = menu_item.price
        return f"{min_price}-{max_price}"

    def convert_menu_to_str (self):
        menu_str = ""
        for menu_item in self.menu:
            menu_str += f"{menu_item.name} | {menu_item.price}\n"
        return menu_str

class MenuItem:

    def __init__ (self, name, price, category, calories, ingredients):
        self.name = name
        self.price = price
        self.category = category
        self.calories = calories
        self.ingredients = ingredients # Is this a string or a list?

    def __str__ (self):
        return f"{self.name} | {self.price} | {self.category} | {self.calories} | {self.ingredients}"


restaurant_1 = Restaurant("Wing Stop", "wingstop.com/app", 4)
restaurant_2 = Restaurant("Blue Line Deli", "dining.byu.edu", 60)

menu_item_1 = MenuItem("12 Wings", 12.00, "Entree", 400, "Chicken, Spices, Sauce, Ranch")
menu_item_2 = MenuItem("Fries", 2.99, "Sides", 300, "Potatos, Seasoning, Oil")
menu_item_3 = MenuItem("Whole Hog", 8.99, "Sandwich", 600, "Bread, Bacon, Pulled Pork, Ham, Mayo")
menu_item_4 = MenuItem("Burrito", 7.99, "Burritos", 500, "Tortilla, Beans, Cheese, Lettuce")

restaurant_1.menu.append(menu_item_1)
restaurant_1.menu.append(menu_item_2)
restaurant_2.menu.append(menu_item_3)
restaurant_2.menu.append(menu_item_4)

print(restaurant_1)
print(restaurant_2)