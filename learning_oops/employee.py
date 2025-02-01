from newperson import Person

class Employee(Person):

   def __init__(self, first_name, last_name, dob, salary, middle_name=" "):
     super().__init__(first_name, last_name, dob, middle_name)
     self.salary = salary

if __name__ == "__main__":
    employee = Employee("lijah", "sikhrakar", "2002-04-27", 20000)
    print(employee, employee.salary)
