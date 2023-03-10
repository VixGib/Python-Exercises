from person import Person

from employee import Employee

from customer import Customer

person1 = Employee("Vicki", "Gibbison")
employees = []
employees.append(person1)
print(person1)
person1.get_address("85 Shakespeare Drive, Cheadle")
person1.get_live_location("Manchester")
person1.get_dob("09/04/80")
person1.get_age(42)
person1.get_gender("Female")
person1.get_national_insurance_num("MK097760")
person1.mobile_num("07123123123")
person1.email("vickigibbison@skygrads.com")
person1.job_title("Software Graduate")
person1.get_hours(40)
person1.get_days("Mon : Fri")
person1.years_worked("1")
person1.get_hobbies("Paddle board and walk my dog")
person1.can_drive("can drive")


customer1 = Customer("Phillip", "Gibbison")
customers = []
customers.append(customer1)
print(customer1)
customer1.get_address("85 Shakespeare Drive, Cheadle")
customer1.mobile_num("07345345345")
customer1.email("philgibbison@home.com")
customer1.preferred_type_of_shopping("In person")
customer1.grocery_shop("Aldi")
customer1.clothes_shop("Tessuti")
customer1.places_to_go("The pub, the cinema, nice restaurants and water sports centers")


