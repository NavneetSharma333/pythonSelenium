


class My_class_1:
    
    def __init__(self):
        print("__init_ of class 1 ")
        self.prop_cls1 = 10
        
    def method_1_class_1(self):
        print("from method_1_class_1")
        

class My_class_2(My_class_1):
    
    def __init__(self):
        super().__init__()
        print("__init_ of class 2 ")
        
    def method_1_class_2(self):
        print("FROM method_1_class_2")
    
    
# obj1 = My_class_1()
# obj1.method_1_class_1()

obj2 = My_class_2()
obj2.method_1_class_2()