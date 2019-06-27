expense = [300,500,700,859,123,235,634]

def double(dollars):
	return dollars * 2

new_expense = list(map(double, expense))
print(new_expense)	

'''

we can also run this list through for loop. but map is much easier

for x in expense:
	print(x*2)

'''