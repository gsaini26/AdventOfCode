import re

f = open("input4a.txt",'r')

# '8' < '12'

count=0
for line in f:

    firstLine = line.strip()
    allItems = re.split(r'-|,', firstLine)
    allItems = list(map(int, allItems))
    # we can assume exactly 4 items in this problem
    
    # 0 1 2 3
    # 2 <= 0 <= 3 or  2 <= 1 <= 3   or 0<=2<=1 or 0<=3<=1
    if ((allItems[2]<=allItems[0]<=allItems[3]) or (allItems[2]<=allItems[1]<=allItems[3])) or ((allItems[0]<=allItems[2]<=allItems[1]) or (allItems[0]<=allItems[3]<=allItems[1])):
        print("Inrange")
       
        count=count+1
    else:
        print("notInRange")
print("total",count)
# if the first number in the second range is in the first range or the second 
# number in the first range is in the second range,
# there are intersecting numbers

# if the first number is in the second range and the second number is in the second range
# or if the second number is in the first range and the second number is in the first range
# then the number is fully contained in the other. First Part of 4.
f.close()

    

