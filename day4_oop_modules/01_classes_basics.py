# Student
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return 'O'
        elif self.marks >= 75:
            return 'A'
        elif self.marks >= 60:
            return 'B'
        elif self.marks >= 40:
            return 'C'
        return "Fail"

    def __str__(self):
        return f"{self.name}: Grade {self.grade()}"

s = Student("Saurabh", 82)
print(s)

# Bank Account
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.show_balance()
acc.withdraw(2000)