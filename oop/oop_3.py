class Person:
    number_of_people = 0 #class attributes

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod #this is decorator ie it denotes it is a class method
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Raj")
p2 = Person("Rabik")
print(Person.number_of_people)