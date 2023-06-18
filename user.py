class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
              
    def show_details(self):
        print("User Personal Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        
        
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account Balance: KES", self.balance)
    
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            return "Insufficient Fund. Current Balance: KES", self.balance
        self.balance = self.balance - self.amount
        return "Account Balance Updated. Current Balance: KES", self.balance
    
    def view_balance(self):
        self.show_details()
        return "Account Balance is: KES", self.balance
  

if __name__ == "__main__":
    peter = Bank("Peter", 14, 'Male')
    print(peter.show_details())
