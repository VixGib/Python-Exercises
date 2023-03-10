from person import Person


class Customer(Person):
    number_of_customers = 0

    def __init__(self, customer_firstname, customer_surname):
        super().__init__(customer_firstname, customer_surname)
        Customer.number_of_customers += 1


    def preferred_type_of_shopping(self, virtual_or_in_person):
        print("I like to do my shopping", virtual_or_in_person)

    def grocery_shop(self, shop):
        print("I do my grocery shopping at", shop)

    def clothes_shop(self, shop):
        print("I like to buy my clothes from", shop)

    def places_to_go(self, places):
        print("The places I like to go in my free time are", places)


