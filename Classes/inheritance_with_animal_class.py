

class Animal:
    
    def __init__(self, color, food_type, playing, name):
        print("This is init from Parent.")
        self.rang = color
        self.food = food_type
        self.playing = playing
        self.name = name
        
    def move(self):
        print("animal moves")
        
    def eat(self):
        print("animal eats when-ever required")
        print("this animal eats {}". format(self.food))
        
    def breath(self):
        print("animal can breathe")
        
    def playing_with_kids(self):
        print(f"{self.name} is friendly with everyone and play {self.playing}")     

class Dog(Animal):
    
    def __init__(self, color, food_type, breed, name, playing):
        super().__init__(color, food_type, playing, name)
        self.dog_name = name
        self.dog_breed = breed
        
    def bark(self):
        print("wooff")
        
    def as_security(self):
        print("My dog is my home security")
        
        
        
class Cat(Animal):
    
    def __init__(self, color, food_type, breed, name, playing):
        super().__init__(color, food_type, playing, name)
        self.cat_breed = breed
        self.cat_name = name

    def meaw(self):
        print("Meaww")
        
    
myDog = Dog("Black", "meat", "rotwheeler", "Dog-kalu", "flying disc")
print(myDog.dog_name)
print(myDog.dog_breed)
print(myDog.rang)
myDog.eat()
myDog.bark()
myDog.breath()
myDog.playing_with_kids()


myCat = Cat("white", "chawal", "persian", "Cat-Kitty", "jumping on tree")
print(myCat.cat_name)
print(myCat.cat_breed)
print(myCat.rang)
myCat.meaw()
myCat.eat()
myCat.playing_with_kids()