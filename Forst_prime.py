# Marcus Forst
# Scientific Computing I 
# Prime Number Selector

# This function prints all of the prime numbers between two entered values. 

import math as ma

# These functions ask for the number range, and assign them to 'x1' and 'x2'
x1 = int(input('smallest number to check: '))
x2 = int(input('largest number to check: '))

print ('The Prime numbers between', x1, 'and', x2, 'are:')

for i in range(x1, x2+1):
	if i<=0:
		continue	
	if i==1: 
		continue
	for j in range (2, int(ma.sqrt(i))+1):
		if i%j == 0:
			break
	else:
		print (i)

#print ('There are no Prime numbers between', x1, 'and', x2, '.')