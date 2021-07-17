
class User():                                                                 # Parent class
	def __init__(self,name, age, gender, occupation):                           # initialization
		self.name = name                                                          # defining properties
		self.age = age
		self.gender = gender
		self.occupation = occupation
	def show_details(self):                                                     # method to display person
		print("-----------------------------")
		print("	  Personal History")
		print("-----------------------------")
		print("Name: ", self.name)
		print("Age: ",self.age)
		print("Gender: ", self.gender)
		print("Occupation: ",self.occupation)


class Bank(User):                                                             # Child class
	def __init__(self,name,age, gender, occupation):
		super().__init__(name, age, gender,occupation)                            # super() lessesns the burden to write properties in init ... this is inheritance
		self.balance = 0                                                          # initializing balance
	def deposit(self,amount):                                                   # method to deposit amount into bank
		self.amount = amount
		self.balance = self.balance + self.amount
		print("Balance updated with INR ",self.balance)
	def withdraw(self,amount):                                                  # method to withdraw amount from bank
		self.amount = amount
		if (self.amount > self.balance):                                          # checking balance
			print("Insufficient Balance to process withdrawal, your available balance is only INR",self.balance)
		else:
			self.balance = self.balance - self.amount
			print("Balance updated with INR ",self.balance)
	def acc_details(self):                                                      # method to display account and personal details
		self.show_details()
		print("Account Balance: " ,self.balance)

Micky = Bank("Micky Mouse", 38, "Male", "Self-employed")                      # Function calling
Micky.deposit(2500)
Micky.withdraw(50)
Micky.acc_details()
