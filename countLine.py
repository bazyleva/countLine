import sys

path = sys.argv[1]
counter = 0

with open(path) as file:
	for line in file:
		counter +=1
print (counter)
