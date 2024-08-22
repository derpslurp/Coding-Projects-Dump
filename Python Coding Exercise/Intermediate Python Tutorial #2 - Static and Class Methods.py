#A class method takes cls as the first parameter while a static method needs no specific parameters
class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def getPopulation(cls):
        return cls.population
    @staticmethod
    def isAdult(age):
        return age >= 10

    def display(self):
        print(self.name, 'is', self.age, 'years old')

newPerson = person('tim', 18)

print(person.getPopulation())
print(person.isAdult(5))