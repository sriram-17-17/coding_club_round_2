def fm(str):
	return '{:^15}'.format(str)

class Customer:
	all = []
	def __init__(self, name : str, room : int, ID : str, swd_balance = 0.0, cart = []):

		assert swd_balance >= 0, f"SWD Balance {swd_balance} is not greater than 0!" 

		self.name = name
		self.room = room
		self.swd_balance = swd_balance
		self.ID = ID
		self.cart = cart
		Customer.all.append(self)
		 
	def __repr__(self):
		return f"{self.__class__.__name__}('{self.name}', {self.room}, {self.ID}, {self.cart}, {self.swd_balance})"

	def get_name(self):
		return self.name

	def get_room(self):
		return self.room

	def get_swd_balance(self):
		return self.swd_balance

	def get_id(self):
		return self.ID

	def get_cart(self):
		return self.cart

	@classmethod
	def validate_customer(self, num):
		for cust in Customer.all:
			if cust.ID == num:
				return True, cust
		return False, None

	def view_cart(self):
		i = 1
		for item in self.cart:
			print(fm(str(i)) + "\t\t" +  fm(item.name) + "\t\t" + fm(item.price) + "\t\t" + fm(item.quantity) + '\n')

		print("\n\n")

	def purchase(self):
		total = 0
		for item in self.cart:
			temp = item.price
			item.apply_discount()
			total = total + item.price
			item.price = temp

		print("The total amount after applying respective discounts on each item is:", total)
		print("\n\n\n")
		print("Enter one of the following options of payment:" + "\n\n\n")
		user_input = int(input(fm("1. UPI") + "\t\t" + fm("2. Cash") + "\t\t" + fm("3. SWD") + "\n\n\n" + "Choice:"))
		print("\n\n\n")
		if user_input == 3:
			self.deduct_from_swd(total)
			print("Your SWD balance is :", self.get_swd_balance())

		print("\t\t\t\t\t\t\t" + fm("AKSHAY SUPERMARKET") + "\t\t\t\t\t\t\t")
		print("\t\t\t\t\t\t\t" + fm("BILL") + "\t\t\t\t\t\t\t")
		print("\n\n")
		self.view_cart()
		print("The total amount after applying respective discounts on each item is:", total)
		print("\t\t\t\t\t\t\t" + fm("THANKS") + "\t\t\t\t\t\t\t")
		self.cart.clear()

	def deduct_from_swd(self, num):
		self.swd_balance = self.swd_balance - num

class Admin:
	all = []
	def __init__(self, password: str):
		self.password = password
		Admin.all.append(self)

	def __repr__(self): 
		return f"{self.__class__.__name__}('{self.password}')"

class Item:
	discount = 0.2
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		assert price >= 0, f"Price {price} is not greater than 0!"
		assert quantity >= 0, f"Price {quantity} is not greater than 0!"

		self.name = name
		self.price = price 
		self.quantity = quantity
		Item.all.append(self) 
	
	
	def __repr__(self): 
		return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


	def calculate_total_price(self): 
		return self.quantity * self.price

	def apply_discount(self):
		self.price = self.price - (self.price * self.discount)

	def get_name(self):
		return self.name

	def get_price(self):
		return self.price

	def get_quantity(self):
		return self.quantity

	@classmethod
	def view_categories(self):
		lst = []
		i = 1
		for item in self.all:
			if i == 1:
				lst.append(item.__class__.__name__)
				i = i + 1
			else:
				if item.__class__.__name__ != lst[i - 2]:
					lst.append(item.__class__.__name__)
					i = i + 1
		print(fm("Sl.No") + "\t\t" + fm("Category"))

		for i in range(len(lst)):
			print(fm(str(i + 1)) + "\t\t" + fm(lst[i]))


	@classmethod		
	def view_items(self):
		print(fm("Sl.No") + "\t\t" + fm("Name") + "\t\t" + fm("Price") + "\t\t" + fm("Quantity"))
		i = 0
		for item in self.all:
			print(fm(str(i + 1)) + "\t\t" + fm(f'{item.name}') + "\t\t" + fm(str(item.price)) + "\t\t" + fm(str(item.quantity)))
			i = i + 1
		print("\n\n\n")	

		


class Food(Item):
	discount = 0.15
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)

		Food.all.append(self)

	

class Stationery(Item):
	discount = 0.1
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Stationery.all.append(self)

class Cosmetic(Item):
	discount = 0.15
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Cosmetic.all.append(self)

class Electronic(Item):
	discount = 0.3
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Electronic.all.append(self)

class Book(Item):
	discount = 0.1
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Book.all.append(self)

class Cloth(Item):
	discount = 0.3
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Cloth.all.append(self)

class Cleaning(Item):
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Cleaning.all.append(self)

class Utensil(Item):
	discount = 0.25
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Utensil.all.append(self)

class Plastic(Item):
	discount = 0.1
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Plastic.all.append(self)


class Sport(Item):
	discount = 0.05
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Sport.all.append(self)

class Bedding(Item):
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Bedding.all.append(self)

class Toiletery(Item):
	discount = 0.1
	all = []
	def __init__(self, name: str , price: float, quantity = 0): 

		super().__init__(
			name, price, quantity
		)
		
		Toiletery.all.append(self)


food1 = Food("Lays Chips", 20, 10)
food2 = Food("Dairy Milk", 20, 10)
food3 = Food("Tropicana", 50, 10)
food4 = Food("Hide&Seek", 30, 10)
food5 = Food("Aloo Bhujia", 40, 10)

stationery1 = Stationery("Pilot V5", 70, 10)
stationery2 = Stationery("Apsara Pencil", 50, 10)
stationery3 = Stationery("Kangaro Stapler", 30, 10)
stationery4 = Stationery("Nataraj Sharpener", 50, 10)
stationery5 = Stationery("Pilot Marker", 100, 10)

cosmetic1 = Cosmetic("Lakme Lotion", 70, 10)
cosmetic2 = Cosmetic("Dove Soap", 40, 10)
cosmetic3 = Cosmetic("Conditioner", 100, 10)
cosmetic4 = Cosmetic("Dettol Soap", 80, 10)
cosmetic5 = Cosmetic("Ponds Cream", 70, 10)


electronic1 = Electronic("Charger", 500, 10)
electronic2 = Electronic("Wire", 600, 10)
electronic3 = Electronic("Phone", 500, 10)
electronic4 = Electronic("Mouse", 600, 10)
electronic5 = Electronic("Laptop", 500, 10)

book1 = Book("Note", 200, 10)
book2 = Book("Kreative", 100, 10)
book3 = Book("Nataraj", 200, 10)
book4 = Book("Classmate", 100, 10)
book5 = Book("Paper Grid", 200, 10)



cloth1 = Cloth("Sock", 200, 10)
cloth2 = Cloth("Shirt", 100, 10)
cloth3 = Cloth("Pant", 200, 10)
cloth4 = Cloth("Hoodie", 100, 10)
cloth5 = Cloth("Sweater", 200, 10)

cleaning1 = Cleaning("SurfXL", 100, 10)
cleaning2 = Cleaning("Vanish", 200, 10)
cleaning3 = Cleaning("Nirma", 100, 10)
cleaning4 = Cleaning("Ghadi", 200, 10)
cleaning5 = Cleaning("Vim", 100, 10)

utensil1 = Utensil("Bottle", 350, 10)
utensil2 = Utensil("Fork", 250, 10)
utensil3 = Utensil("Spoon", 450, 10)
utensil4 = Utensil("Cooker", 350, 10)
utensil5 = Utensil("Pan", 250, 10)

plastic1= Plastic("Bucket", 100, 10)
plastic2= Plastic("Bag", 200, 10)
plastic3= Plastic("Cover", 100, 10)
plastic4= Plastic("Container", 200, 10)
plastic5= Plastic("Mug", 100, 10)

sport1 = Sport("Football", 300, 10)
sport2 = Sport("Basketball", 300, 10)
sport3 = Sport("Cricket Bat", 400, 10)
sport4 = Sport("Tennis ball", 50, 10)
sport5 = Sport("Leather Ball", 200, 10)

bedding1 = Bedding("Pillow", 100, 10)
bedding2 = Bedding("Bedsheet", 80, 10)
bedding3 = Bedding("Blanket", 150, 10)
bedding4 = Bedding("Bed", 100, 10)
bedding5 = Bedding("Thick Blanket", 50, 10)

admin = Admin("password")

customer1 = Customer("Rahul", 4130, 203, 4000.0)
customer1 = Customer("Gotur", 4120, 202, 3000.0)
customer1 = Customer("Bom", 4110, 201,  2000.0)




