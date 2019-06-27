import heapq

class_marks = [337, 100, 256, 200, 62, 487]

print(heapq.nlargest(3, class_marks))

friends = [
	{'person' : 'Archana', 'year' : 6},
	{'person' : 'Om', 'year' : 5},
	{'person' : 'saravanan', 'year' : 2}

]

print(heapq.nsmallest(2, friends, key = lambda friends : friends['year']))
