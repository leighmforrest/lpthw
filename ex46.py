## Animal is-a object (yes, sort of confusing) look at the extrea credit
class Animal(object):
    def sound(self):
        print("I don't talk")


## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

    def sound(self):
        print("WOOFF WOOFF!!!!!")


## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

    def sound(self):
        print("MEOW!")


## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def pet_sounds(self):
        if self.pet is not None:
            print(f"{self.name}'s pet {self.pet.name} makes this sound:", end=" ")
            self.pet.sound()
        else:
            print(f"{self.name} does not have a pet.")


## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

    def pet_sounds(self):
        print(f"{self.name} is a grunt!", end=" ")
        super().pet_sounds()


## ??
class Fisher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.fish = []

    def add_fish(self, fish):
        self.fish.append(fish)

    def __str__(self):
        str1 = f"Fisher {self.name}:\n"

        for fishie in self.fish:
            str1 += f"{fishie}\n"

        return str1[:-1]


class Fish(object):
    def __init__(self):
        self.type = "fish"
        self.shape = "fusiform"

    def __str__(self):
        return f"{self.type} is the fish and the shape is {self.shape}."


## ??
class Salmon(Fish):
    def __init__(self):
        self.type = "salmon"
        self.shape = "torpedo"


## ??
class Halibut(Fish):
    def __init__(self):
        self.type = "halibut"
        self.shape = "oval"


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

rod = Employee("Roderick", 100000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()

rover.sound()
satan.sound()

frank.pet_sounds()
mary.pet_sounds()
rod.pet_sounds()
print(flipper)
print(crouse)
print(harry)

frederick = Fisher("Frederick")
frederick.add_fish(flipper)
frederick.add_fish(crouse)
frederick.add_fish(harry)
print(frederick)
