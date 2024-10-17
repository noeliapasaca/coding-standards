"""
This is a module for a shopping cart system
"""

class Itemz:
    """This is a class for items in a shopping cart"""
    def __init__(self, name, price, qty):

        self.name = name

        self.price = price

        self.qty = qty

        self.category = "general"

        self.env_fee = 0

    def get_total(self):
        """This method returns the total price of the item"""
        return self.price * self.qty

    def get_most_prices(self):
        """This method returns the total price of the item"""
        return self.price * self.qty * 0.6

class ShoppingCart:
    """This is a class for a shopping cart"""

    def __init__(self):

        self.items = []

        self.tax_rate = 0.08

        self.member_discount = 0.05

        self.big_spender_discount = 10

        self.coupon_discount = 0.15

        self.currency = "USD"



    def add_item(self, item):

        """This method adds an item to the shopping cart"""

        self.items.append(item)



    def calculate_subtotal(self):

        """This method calculates the subtotal of the shopping cart"""

        subtotal = 0

        for item in self.items:

            subtotal += item.getTotal()

        return subtotal



    def apply_discounts(self, subtotal, is_member):

        """This method applies discounts to the subtotal"""

        if is_member == "yes":

            subtotal = subtotal - (subtotal * self.member_discount)

        if subtotal > 100:

            subtotal = subtotal - self.big_spender_discount

        return subtotal



    def calculate_total(self, is_member, has_coupon):

        """This method calculates the total price of the shopping cart"""

        subtotal = self.calculate_subtotal()

        subtotal = self.apply_discounts(subtotal, is_member)

        total = subtotal + (subtotal * self.tax_rate)

        if has_coupon == "YES":

            total = total - (total * self.coupon_discount)

        return total



def main():

    """
    This is the main function
    """

    cart = ShoppingCart()

    item1 = Itemz("Apple", 1.5, 10)

    item2 = Itemz("Banana", 0.5, 5)

    item3 = Itemz("Laptop", "1000", 1)

    item3.category = "electronics"

    cart.add_item(item1)

    cart.add_item(item2)

    cart.add_item(item3)

    is_member = True

    has_coupon = "YES"



    total = cart.calculate_total(is_member, has_coupon)



    if total < 0:

        print("Error in calculation!")

    else:

        print("The total price is: $" + str(int(total)))



if __name__ == "__main__":

    main()
