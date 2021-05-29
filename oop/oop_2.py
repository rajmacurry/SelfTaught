class Animal:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. I am a {self.gender}")

    def speak(self):
        print("I do not know what to say!?")

class Dog(Animal):
    def __init__(self, name, age, gender, colour):
        super().__init__(name, age, gender)
        self.colour= colour

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. I am a {self.gender} and I am {self.colour} in colour.")

    def speak(self):
        print("Woof Woof")

class Cat(Animal):
    def speak(self):
        print("Meow Meow")

class Fish(Animal):
    pass

d = Animal("Blaze", 3, "male")
d.show()

a = Dog("Kanchi", 2, "female", "Brown")
a.speak()
a.show()

b = Cat("Julie", 5, "female")
b.speak()
b.show()

c = Fish("Bubbles", 4, "female")
c.speak()
