class Person:
    def __init__(self, an_firstname, an_surname):
        self._firstname = an_firstname
        self._surname = an_surname

    def __str__(self):
        return "Name: " + self._firstname + " " + self._surname

    def get_age(self, age):
        print("Age: ", age)

    def get_gender(self, gender):
        print("Gender: ", gender)

    def get_address(self, address):
        print("Address: ", address)

    def get_hobbies(self, hobbies):
        print("In my spare time I like to", hobbies)

    def get_live_location(self, location):
        print("Lives in: ", location)

    def get_dob(self, date_of_birth):
        print("DOB:", date_of_birth)

    def can_drive(self, driving_status):
        print("I", driving_status)

    def email(self, email_address):
        print("email address: ", email_address)

    def mobile_num(self, number):
        print("Mobile No: ", number)

