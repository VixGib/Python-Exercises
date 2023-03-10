from person import Person


class Employee(Person):
    number_of_employees = 0

    def __init__(self, employee_firstname, employee_surname):
        super().__init__(employee_firstname, employee_surname)
        Employee.number_of_employees += 1

    def get_national_insurance_num(self, national_insurance_num):
        print("National Insurance Number: ", national_insurance_num)

    def get_hours(self, hours_worked):
        print("Hours worked: ", hours_worked)

    def get_days(self, days):
        print("Days worked: ", days)

    def job_title(self, job):
        print("Job title:", job)

    def years_worked(self, years):
        print("Number of years worked: ", years)



