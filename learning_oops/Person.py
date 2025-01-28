class Person:

    def __init__(self, first_name="Unknown", last_name="Unknown", citizenship_no=None, sex=None, dob=None, height_in_ft=None, height_in_inch=None):
        self.first_name = first_name
        self.last_name = last_name
        self.citizenship_no = citizenship_no
        self.sex = sex
        self.dob = dob
        self.height_in_ft = int(height_in_ft)
        self.height_in_inch = int(height_in_inch)

    def full_name(self): #method
        return self.first_name + " " + self.last_name

    def last_three_digits_of_citizenship_no(self):
        return str(self.citizenship_no)[-3:]

    def all_digits_of_citizenship_no(self):
        return (len(self.citizenship_no) -3) * "*"

    def height_in_ft_and_inch_to_cm(self):
        return (self.height_in_ft * 30.48) + (self.height_in_inch * 2.54)

    def __str__(self):
        return self.all_digits_of_citizenship_no() + self.last_three_digits_of_citizenship_no() + " " + self.full_name() + " " + str(self.height_in_ft_and_inch_to_cm())

if __name__ == "__main__":
    p = Person("lijah", "sikhrakar", '18232189381231', 0,0,5,9)
    print(p)


#[each for each in name.values() if each !=""]
