#easy method to handle large number of items in the list
def drop_first_last(grades):
	first, *middle, last = grades
	avg = sum(middle)/len(middle)
	print(avg)

drop_first_last([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

'''
************** another method************
date, item, price = ['January 1, 2019', 'Ice Cream', 100]
print(price) 
*****************************************
'''