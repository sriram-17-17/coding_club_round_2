from Class import Customer, Admin, Item, Food, Stationery, Cosmetic, Electronic, Book, Cloth, Cleaning, Utensil, Plastic, Sport, Bedding

items_lst = [Food.all, Stationery.all, Cosmetic.all, Electronic.all, Book.all, Cloth.all, Cleaning.all, Utensil.all, Plastic.all, Sport.all, Bedding.all]



def view_items(lst, inp):
	while True:
		category_lst = []
		print("Sl.No\t\tName\t\tPrice\t\tQuantity\t\tDiscount")
		i = 1
		for item in lst[inp - 1]:
			print(i,item.name, item.price, item.quantity, item.discount, sep = '\t\t')
			category_lst.append([i, item.name, item.price, item.quantity, item.discount, item])
		
		return category_lst






def validate(input):
	if (input == Admin.all[0].password):
		return True
	else:
		return False



def fm(str):
	return '{:^15}'.format(str)

while True:
	print("\t\t\tWELCOME TO AKHSAY SUPERMARKET!\n\n\n\n")
	ui = int(input(fm('1. Customer Login') + "\t\t" + fm('2. Admin Login') + "\t\t" + fm('3. Exit') + "\n\n\n" + "Choice:"))
	print("\n\n\n")
	if ui == 1 :
		while True:
			'''

			THIS BLOCK CONTAINS CUSTOMER FEATURES

			'''
			ui = int(input(fm('1. Enter ID number') +'\t\t' + fm('2. Exit') + '\n\n' + 'Choice:'))
			print("\n\n\n")
			if ui == 1:
				while True:
					ID = int(input("Enter your ID number:"))
					print("\n\n\n")
					ui, cust = Customer.validate_customer(ID)
					if ui == True:

						print("Welcome" + ' ' + cust.name + "!")
						print("\n\n\n")
						ui = int(input(fm("1. View cart") + "\t\t" + fm("2. Add to cart") + "\t\t" + fm("3. Remove to cart") + "\t\t" + fm("4. Exit") + "\n\n\n" + "Choice:"))
						print("\n\n\n")

						if ui == 1:
							while True:
								'''
								THIS BLOCK CONTAINS VIEW CART

								'''
								print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity") + "\n")
								cust.view_cart()

								ui = int(input(fm("1. Buy items") + "\t\t" + fm("2. Go back") + "\n\n\n" + "Choice:"))
								print("\n\n\n")
								if ui == 1:
									cust.purchase()
									break
								elif ui == 2:
									break
						elif ui == 2:
							while True:
								Item.view_categories()
								print("\n\n\n")
								ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("2. Exit") + "\n\n\n" + "Choice:"))
								print("\n\n\n")
						
						
								if ui == 1:
									Food.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Food.all)):
										cust.cart.append(Food.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break

								elif ui == 2:
									Stationery.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Stationery.all)):
										cust.cart.append(Stationery.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break
								

								elif ui == 3:
									Cosmetic.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Cosmetic.all)):
										cust.cart.append(Cosmetic.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break
								elif ui == 4:
									Electronic.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Electronic.all)):
										cust.cart.append(Electronic.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break

								elif ui == 5:
									Book.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Book.all)):
										cust.cart.append(Book.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break

								elif ui == 6:
									Cloth.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Cloth.all)):
										cust.cart.append(Cloth.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break

								elif ui == 7:
									Cleaning.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Cleaning.all)):
										cust.cart.append(Cleaning.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break

								elif ui == 8:
									Utensil.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Utensil.all)):
										cust.cart.append(Utensil.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break

								elif ui == 9:
									Plastic.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Plastic.all)):
										cust.cart.append(Plastic.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break

								elif ui == 10:
									Sport.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Sport.all)):
										cust.cart.append(Sport.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break

								elif ui == 11:
									Bedding.view_items()
									ui = int(input(fm("1. Enter Sl No") + "\t\t" + fm("0 to exit") + "\n\n\n" + "Choice:"))
									print("\n\n\n")
									if (ui != 0) and (ui <= len(Bedding.all)):
										cust.cart.append(Bedding.all[ui - 1])
										print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
										cust.view_cart()
										break
									else:
										break

								else:
									break
								

								

						elif ui == 3:
							print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
							cust.view_cart()
							ui = int(input(fm("1. Enter Sl.No") + "\t\t" + fm("2. Exit") + "\n\n\n"))
							del cust.cart[ui - 1]
							cust.view_cart()
							break

						else:
							break

					else:
						print("Wrong ID....Redirecting you back to home page......")
						print("\n\n\n")
						break 
			else:
				break

	elif ui == 2:
		user_input = input("Enter Password:")
		user_input = validate(user_input)

		if (user_input == True):
			print("\n\n\nWelcome admin!\n\n")
			while True:
				user_input = int(input(fm("1. View Categories") + "\t\t" + fm("2. View Profits") + "\t\t" + fm("3. Logout") + "\n\n" + "Choice:"))

				if user_input == 1:
					while True:
						view_categories()
						user_input = int(input("\n\n\nEnter Sl. No to view items in category\n\nEnter 0 to go back\n\nChoice:"))
						if user_input == 1:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 2:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 3:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 4:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 5:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 6:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 7:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 8:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 9:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 10:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						elif user_input == 11:
							user_input, category_lst = view_items(items_lst, user_input)
							if user_input == 1:
								break
						else:
							break
				elif user_input == 2:
					pass
				else:
					print("\n\n\nLogging out...\n\n\n")
					break

	else:
		break

		