import string

f = open("input3a.txt",'r')
priority = string.ascii_lowercase + string.ascii_uppercase
print(priority)
result = 0    

for line in f:
    halfway=len(line)//2
    string1= line[:halfway]
    string2= line[(halfway+1):]
 #   print("string1", string1, "  ", "string2", string2)

    string1, string2 = line[:len(line)//2], line[len(line)//2:]
    for i in string1: 
        if i in string2:
            break
   # print("common char is ", i)
    print(priority.index(i))
    
    result = priority.index(i) + 1 + result
print("final",result)    