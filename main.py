from learning_oops.Person import Person

file = open("/Users/lijah/PycharmProjects/DSML-DTC/data/persons.csv", "r")
person_file = [line.strip().split(",") for line in file.readlines()[1:]]

persons = []
for line in person_file:
        person = Person("first_name","last_name","citizenship_no","male","2002","height_ft","height_inch")
        persons.append(person)

file.close()

for person in persons:
    print(
        f"<Person: Citizenship: {person.all_digits_of_citizenship_no() + person.last_three_digits_of_citizenship_no()} | Full Name: {person.full_name()}>")
