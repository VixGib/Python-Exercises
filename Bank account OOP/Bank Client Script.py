from current_account import CurrentAccount
from savings_account import SavingsAccount
from isa_account import IsaAccount

person1 = CurrentAccount("Vicki", "Gibbison")
person1.get_pin()
print(person1)
person1.get_account_type()
person1.get_account_num("987654")

person1.set_interest_rate("1.5%")
person1.get_email("vickigibbison@getintotech.com")
person1.get_phone_num("07955443322")


print("                                   ")

person2 = SavingsAccount("Vicki", "Gibbison")
person2.get_pin()
print(person2)
person2.get_account_type()
person2.get_account_num("123456")
person2.set_interest_rate("5%")
person2.get_email("vickigibbison@getintotech.com")
person2.get_phone_num("07955443322")


print("                                   ")

person3 = IsaAccount("Vicki", "Gibbison")
person3.get_pin()
print(person3)
person3.get_account_type()
person3.get_account_num("444555")
person3.set_interest_rate("8%")
person3.get_email("vickigibbison@getintotech.com")
person3.get_phone_num("07955443322")










