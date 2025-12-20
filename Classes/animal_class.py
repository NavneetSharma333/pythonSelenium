
class Animal:
    
    def __init__(self, color="red", food_type="none"):
        print("This is init.")
        self.rang = color
        self.food = food_type
        
    def move(self):
        print("animal moves")
        
    def eat(self):
        print("animal eats when-ever required")
        print("this animal eats {}". format(self.food))
        
    def breath(self):
        print("animal can breathe")
            
    def main(self):
        self.move()
        self.eat()
        self.breath()
        print(f"the color from main of this animal is: {self.rang}")
        
# my_animal_1 = animal("white", "Veggies")
# print(f"color of animal 1: {my_animal_1.rang}")
# my_animal_1.move()
# my_animal_1.eat()


my_animal_2 = Animal("brown", "veggies")
# my_animal_2.eat()


my_animal_2.main()