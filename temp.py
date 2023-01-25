class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = agedef say_hello(self):
        print("Hello, my name is {} and I am {} years old".format(self.name, self.age))

