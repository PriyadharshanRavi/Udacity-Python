stocks = {
	'GOOG' : 456,
	'AAPL' : 321,
	'FB' : 789,
	'AMZN' : 165

}

print(min(stocks)) #print min alpha

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price) #print min value eg.,('456' : 'GOOG')