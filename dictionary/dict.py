# Min and Max and Sorting Dictionary

# Sample Dictionary

groceries = {
	'Wheat' : 120,
	'Handwash' : 30,
	'Sugar' : 100,
	'Salt' : 20,
	'Ketchup' : 70
}

print(min(zip(groceries.values(), groceries.keys())))
print(max(zip(groceries.values(), groceries.keys())))
print(sorted(zip(groceries.values(), groceries.keys())))