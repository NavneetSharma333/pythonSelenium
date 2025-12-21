

class Animal:
    
    def __init__(self, color, food_type):
        print("This is init from Parent.")
        self.rang = color
        self.food = food_type
        
    def move(self):
        print("animal moves")
        
    def eat(self):
        print("animal eats when-ever required")
        print("this animal eats {}". format(self.food))
        
    def breath(self):
        print("animal can breathe")


class Dog(Animal):
    
    def __init__(self, color, food_type, breed, name):
        super().__init__(color, food_type)
        self.dog_name = name
        self.dog_breed = breed
        
    def bark(self):
        print("wooff")
        
    def as_security(self):
        print("My dog is my home security")
        
        
        
class Cat(Animal):
    
    def __init__(self, color, food_type, breed, name):
        super().__init__(color, food_type)
        self.cat_breed = breed
        self.cat_name = name

    def meaw(self):
        print("Meaww")
        
    
myDog = Dog("Black", "meat", "rotwheeler", "kalu")
print(myDog.dog_name)
print(myDog.dog_breed)
print(myDog.rang)
myDog.eat()
myDog.bark()
myDog.breath()



myCat = Cat("white", "chawal", "persian", "catu")
print(myCat.cat_name)
print(myCat.cat_breed)
print(myCat.rang)
myCat.meaw()
myCat.eat()