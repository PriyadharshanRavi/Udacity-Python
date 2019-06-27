from operator import itemgetter

user = [
	{"fname" : "Priyadharshan", "lname" : "Ravi"},
	{"fname" : "Vijay", "lname" : "Kuber"},
	{"fname" : "Dinesh", "lname" : "Sankaran"},
	{"fname" : "Harsha", "lname" : "Gunaseelan"},
	{"fname" : "Archana", "lname" : "Surulichamy"},
	{"fname" : "Saravanan", "lname" : "Ravi"},
	{"fname" : "Archana", "lname" : "Subramanyam"}
]

for x in sorted(user, key = itemgetter('fname')):
	print(x)

print("_________________________\n")

for x in sorted(user, key = itemgetter("fname", "lname")):
	print(x)	