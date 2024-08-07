class shoes:

	def __init__(self,name,price):
		self.name = name
		self.price =float(price)
	
	def budget_check(self,budget):
		if not isinstance (budget,(int,float)):
			print("invalid entry")
			exit()
	
	def change(self,budget):
		return (budget - self.price)
		
	def buy(self,budget):
		self.budget_check(budget)
		
		if budget>=self.price:
			print (f"You Can go to the {self.name}")
			
			if budget ==self.price:
				print("you have exactly enough money")
			else:
				 print(f'You can buy these shoes and have ${self.change(budget)} left over.')
			
			exit('Thanks for using the Shoes Budget Tool App')
