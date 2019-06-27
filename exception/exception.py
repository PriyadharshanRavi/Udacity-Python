while True:
	try:
		number = int(input("Quote the value for this price\n"))
		c = str(number * .20)
		print(c+" will be my comission")
		break
	except Exception:
		print("Bid an appropriate value")
#	else:
#		pass
	finally:
		print("Exception loop completed") 