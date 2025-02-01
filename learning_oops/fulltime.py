from employee import Employee

class FullTime(Employee):
    def __init__(self, first_name, last_name, dob, salary, position, middle_name=''):
        Employee.__init__(self, first_name, last_name, dob, salary, middle_name)
        self.position = position

    def ssf_amouunt(self):
        return self.salary * 0.3

    def employee_contribution(self):
        return self.salary * 0.1

    def company_contribution(self):
        return self.salary * 0.2

    def total_salary(self):
        return self.salary + self.employee_contribution()

    @property
    def tax(self):
        return self.total_salary() * 0.15

    def gross_salary(self):
        return self.total_salary() - self.tax()

    def __str__(self):
        return super().__str__() + f" | Tax:{self.tax}"

if __name__ == "__main__":
    ft = FullTime("lijah", "sikhrakar", "2002-04-27", 60000, "CEO")
    print(ft)