#1. Reverse the order of the items in an array.
#Example:
#a = [1, 2, 3, 4, 5]
#Result:
#a = [5, 4, 3, 2, 1]

a = [1,2,3,4,5
     ]
list.reverse(a)
print ('Ex1: Inverted list is:', a)

#2. Get the number of occurrences of var b in array a.
#Example:
#a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
#b = 2
#Result:
#4

a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
b = 2

count = 0
for i in a:
	if ( i == b):
		count+=1
print ('Ex2: The number of occurences is:', count)

#3. Given a sentence as string, count the number of words in it.
# Example:
# a = 'ana are mere si nu are pere'
# Result:
# 7

a = 'ana are mere si nu are pere'
res = a.count(' ') + 1
print ('Ex3: Number of words in string is:', res)

