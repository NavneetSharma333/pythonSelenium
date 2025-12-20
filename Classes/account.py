
import random

class Account(object):
    
    def __init__(self, user_id, currency= "USD"):
        self.userId = user_id
        self.mudra = currency
        self.current_balance = self.__read_balance_from_database()
        print(f"Current balance is: {self.current_balance} ")
        
    def withdraw(self, amount):
        self.current_balance = self.current_balance - float(amount)
        print(f"Current balance after withdraw: {self.current_balance}")
    
    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f"Current balance after deposit: {self.current_balance}")
    
    def generate_statement(self, start_date, end_date):
        pass
    
    def __read_balance_from_database(self):
        print(f"Getting balance from db for: {self.userId}")
        return random.randint(0, 100)
    
    
account1 = Account(999)
    
import pdb; pdb.set_trace()
