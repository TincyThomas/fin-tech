# Parent class
class User():
	def __init__(self,name, age, gender, occupation):
		self.name = name
		self.age = age
		self.gender = gender
		self.occupation = occupation
	def show_details(self):
		print("-----------------------------")
		print("	  Personal History")
		print("-----------------------------")
		print("Name: ", self.name)
		print("Age: ",self.age)
		print("Gender: ", self.gender)
		print("Occupation: ",self.occupation)

# Child class
class Bank(User):
	def __init__(self,name,age, gender, occupation):
		super().__init__(name, age, gender,occupation)
		self.balance = 0
	def deposit(self,amount):
		self.amount = amount
		self.balance = self.balance + self.amount
		print("Balance updated with INR ",self.balance)
	def withdraw(self,amount):
		self.amount = amount
		if (self.amount > self.balance):
			print("Insufficient Balance to process withdrawal, your available balance is only INR",self.balance)
		else:
			self.balance = self.balance - self.amount
			print("Balance updated with INR ",self.balance)
	def acc_details(self):
		self.show_details()
		"{0}'s Account Balance is {1}".format("name", self.balance)
		print("Account Balance: " ,self.balance)

Tincy = Bank("Tincy", 23, "Female", "Unemployed")
Tincy.deposit(2500)
Tincy.withdraw(50)
Tincy.acc_details()