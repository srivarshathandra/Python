# Task : 

# UPI Payment System using Abstraction Problem Statement:
#  You are building a simple UPI Payment System. Different apps like PhonePe, Google Pay, and Paytm can make payments, but all follow the same process. Steps: 
# 1. Create an abstract class 'UPIPayment' with methods pay(amount)
#  2. Create subclasses: PhonePe, GooglePay, Paytm. 
# 3. Implement pay() to deduct balance and print payment message. 
# 4. Implement check_balance() to show remaining balance. 
# 5. Assign initial balances (PhonePe: 5000, GooglePay: 3000, Paytm: 4000). 
# 6. Create objects and call methods. 
# Rules: - Do not instantiate abstract class – Use abc module – Hide implementation details
#  Expected Output: Paid ■1000 using PhonePe 


from abc import ABC,abstractmethod

class UPIPayment(ABC):
    def __init__(self,balance):
        self.balance=balance
    
    @abstractmethod
    def pay(self,amount):
        pass
    
    def check_balance(self):
        print(f"Remaining balance",self.balance)
        print("----------------------")
        

#Phone pe class
class PhonePe(UPIPayment):
    def __init__(self):
        super().__init__(5000)
    
    def pay(self,amount):
        if amount <= self.balance:
            self.balance = self.balance-amount
            print(f"Paid Rs{amount} using PhonePe")
        else:
            print(f"Insufficient funds!!!")
            print("----------------------\n")
 
 # Googlepay 
class GooglePay(UPIPayment):
    def __init__(self):
        super().__init__(3000)
    
    def pay(self,amount):
        if amount <= self.balance:
            self.balance = self.balance-amount
            print(f"Paid Rs{amount} using GooglePay")
        else:
            print(f"Insufficient funds!!!")
            print("----------------------\n")
 
 # Paytm           
class Paytm(UPIPayment):
    def __init__(self):
        super().__init__(6000)
    
    def pay(self,amount):
        if amount <= self.balance:
            self.balance = self.balance-amount
            print(f"Paid Rs{amount} using Paytm")
        else:
            print("Insufficient funds!!!")
            print("----------------------\n")
            
   
p1=PhonePe()
p2=GooglePay()
p3=Paytm()

p1.pay(200)
p1.check_balance()

p2.pay(300)
p2.check_balance()

p3.pay(400)
p3.check_balance()