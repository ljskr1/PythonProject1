class Person:
    def __init__(self, first_name, last_name, dob, middle_name = ""):
        self.__name = {'first': first_name, 'last': last_name, 'middle': middle_name}
        self.dob = dob

    def get_full_name(self):
        return " ".join(value.capitalize() for value in self.__name.values() if value != "" )

    def __str__(self):
        return f"{self.get_full_name()} | {self.dob}"

if __name__ == "__main__":
    p = Person("lijah", "sikhrakar", "2002-04-27")
    print(p)