

class Dog():
    
    def __init__(self, breed, name):
        self.dog_breed = breed
        self.dog_name = name
        
    def eat(self):
        print("eat.........")
        
    def breath(self):
        print("breath........")
        
    def bark(self):
        print("wooff")
        
    def as_security(self):
        print("My dog is my home security")
        
        
        
class Cat():
    
    def __init__(self, breed, name):
        self.cat_breed = breed
        self.cat_name = name
        
    def eat(self):
        print("Eat.....")
        
    def breath(self):
        print("cat breath....")
        
    def meaw(self):
        print("Meaww")
        
    
myDog = Dog("kiran", "kalu")
print(myDog.dog_breed)
print(myDog.dog_name)
myDog.eat()
myDog.bark()
myDog.breath()


myCat = Cat("white", "catu")
myCat.eat()
myCat.meaw()