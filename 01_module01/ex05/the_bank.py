# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 14:14:15 by asuteau           #+#    #+#              #
#    Updated: 2024/06/11 14:14:17 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# in the_bank.py

class Account(object):

	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount

class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []
	
	def add(self, new_account):
		"""	Add new_account in the Bank
			@new_account: Account() new account to append
			@return	True if success, False if an error occured
		"""
		# test if new_account is an Account() instance and if
		# it can be appended to the attribute accounts

		if not isinstance(new_account, Account):
			return False
		for account in self.accounts:
			if account.name == new_account.name: 
				return False

		self.accounts.append(new_account)
		return True

	def account_presence_check(self, acc):
		for account in self.accounts:
			#acc_name = account.name
			#print(f"account.name is {account.name}")
			if account.name == acc:
				return True
		return False

	def account_check(self, account):
		if not self.account_presence_check(account):
			raise AttributeError("Error: account isn't in the list")
		#if not isinstance(self.account, Account):
		#	raise AttributeError("Error: account is not an account object")
		#	return False



		for account in self.accounts:
			if account.name == origin:
				origin_account = account
			elif account.name == dest:
				dest_account = account


		if len(origin_account) % 2 != 0 :
			return False
			
	def	account_full_check(self, acc, amount):
		if not self.account_presence_check(acc):
			print("Error: account isn't in the list")
			return False
		for account in self.accounts:
			if account.name == acc:
				if not isinstance(account, Account):
					print("Error: origin account is not the right object")
					return False
				if len(account.__dict__) % 2 == 0:
					print("Error: origin account attributes is even")
					return False
				if any(att.startswith('b') for att in dir(account)):
					print("Error: account contains attribute that starts with b")
					return False
				if not "zip" in dir(account) and not "addr" in dir(account):
					print("Error: no attribute zip or addr")
					return False
				if not "name" in dir(account):
					print("Error: no attribute name")
					return False
				if not "id" in dir(account):
					print("Error: no attribute id")
					return False
				if not "value" in dir(account):
					print("Error: no attribute value")
					return False
				if not isinstance(account.id, int):
					print("Error: id attribute is not an int")
					return False
				if not isinstance(account.value, int) and not isinstance(account.value, float):
					print("Error: value attribute is not an int or float")
					return False		
		return True



	def transfer(self, origin, dest, amount):

		if amount < 0:
			print("Error: transfer amount is inferior to zero")
			return False

		for account in self.accounts:
			if account.name == origin:
				if account.value < amount:
					print("Error: account value is too small")
					return False
				
		if not self.account_full_check(origin, amount):
			return False
		elif not self.account_full_check(dest, amount):
			return False
	
		for account in self.accounts:
			if account.name == origin:
				account.value -= amount
			elif account.name == dest:
				account.value += amount

		# self[origin].value -= amount
		# self[dest].value += amount

	def fix_account(self, acc):
		for account in self.accounts:
			if account.name == acc:
				if len(account.__dict__) % 2 == 0:
				 	print("Fix: Attribute was added")
				 	account.get_even = "attribute to get even"
				if any(att.startswith('b') for att in dir(account)):
					for att in account:
						if (att.startswith('b')):
							del att
					print("Fix: Attribute starting with b was deleted")
				if not "zip" in dir(account) and not "addr" in dir(account):
					account.zip = "X"
					print("Fix: Attribute zip was added")
				if not "id" in dir(account):
					account.id = ID_COUNT
					Account.ID_COUNT += 1
					print("Fix: Attribute id was added")
				if not "value" in dir(account):
					account.value = 0
					print("Fix: Attribute value was added")
				if not isinstance(account.id, int):
					account.id = ID_COUNT
					Account.ID_COUNT += 1
					print("Fix: Attribute id was inted")
				if not isinstance(account.value, int) and not isinstance(account.value, float):
					account.value = 0
					print("Fix: Attribute value was inted")
		





	def __str__(self):
		account_details = "\n".join([f"ID: {account.id}, Name: {account.name}, Value: {account.value}" for account in self.accounts])
		return f"The bank contains the following accounts:\n{account_details}"
	


if __name__=="__main__":
	bank = Bank()

	account01 = Account("William John", value=1000)
	account02 = Account("Lil John")

	bank.add(account01)
	bank.add(account02)

	# for account in bank.accounts:
	# #	print(account.__dict__)
	# 	print(dir(account))
	# 	print(f"account is {account.name} len(account) is : {len(dir(account))}")

	bank.transfer("William John", "Lil John", 30)
	
	print(bank)