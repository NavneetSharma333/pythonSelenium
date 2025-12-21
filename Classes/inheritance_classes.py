


class My_class_1:
    
    def __init__(self, cls1_method_1):
        print("__init_ of class 1 ")
        self.prop_cls1 = 10
        self.cls1_in_1 = cls1_method_1
        print(self.cls1_in_1 + "------") # This will come from super init method value given in class 2 
        
    def method_1_class_1(self):
        print("from method_1_class_1")
        
# Inheriting from another class, from class_1 
class My_class_2(My_class_1):
    
    def __init__(self):
        super().__init__("cls1_method_3")
        print("__init_ of class 2 ")
        
    def method_1_class_2(self):
        print("FROM method_1_class_2")
    
    
# obj1 = My_class_1()
# obj1.method_1_class_1()

obj2 = My_class_2()
obj2.method_1_class_2()