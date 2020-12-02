
def coffe_bot():
    print("Welcome to the cafe")
    size = get_size()
    drink_type = get_drink_type()
    coffe_hot = coffee_hotness()
    print(f"Alright, that's a size {coffe_hot} {size}, {drink_type} coming up")
    cuptype = cup_type
    name = input("Can I please get your name? \n>")
    print(f"Thanks {name}, your order will be ready soon")
    another = another_coffee()
def print_message():
	return "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
  	return "small"
  elif res == 'b':
  	return "medium"
  elif res == 'c':
  	return "Large"
  else: 
  	print(print_message())
  	return get_size()

def get_drink_type():
    res = input("What kind of drink would you like? \n[a] Brewd coffe \n[b] Macho \n[c] Latte \n>  ")
    if res == 'a':
    	return "Brewd coffee"
    elif res == 'b':
    	return "Macho"
    elif res == 'c':
    	return order_latte()
    else:
    	print(print_message())
    	return get_drink_type()
def order_latte():
	res = input("What kind of milk would you like with your latte? \n[a] 2% milk \n[b] non-fat milk \n[c] soy milk \n>")
	if res == 'a':
		return "2% milk"
	elif res == 'b':
		return "non-fat milk"
	elif res == 'c':
		return "Soy milk"
	else:
		print(print_message())
		return order_latte()
def cup_type():
	res = input("Would you like a [a]plastic cup(extra charges) or do you have a [b]reusable one?")
	if res == 'a':
		return "extra cup"
	elif res == 'b':
		return "reusable cup"
	else:
		print(print_message())
		return cup_type()
def coffee_hotness():
	res = input("Do you like your coffee \n[a] Cool\n[b] Hot\n>")
	if res == 'a':
		return "Cool"
	elif res == 'b':
		return "hot"
	else:
		print(print_message())
		return coffee_hotness()
def another_coffee():
	res = input("Would you like another coffe?[Yes or no]")
	res = res.lower()
	if res == 'yes':
		return coffe_bot()
	if res == 'no':
		print("All right")
		print("Thank you and goodbye")
		quit()

coffe_bot()

