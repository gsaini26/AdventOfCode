import string

f = open("input3a.txt",'r')
priority = string.ascii_lowercase + string.ascii_uppercase
print(priority)
result = 0    

while True:
    #    halfway=len(line)//2
    #   string1= line[:halfway]
    #   string2= line[(halfway+1):]
    #   print("string1", string1, "  ", "string2", string2)

    #  string1, string2 = line[:len(line)//2], line[len(line)//2:]
    string1 = f.readline()
    string2 = f.readline()
    string3 = f.readline()
    if not string1 or not string2 or not string3:
        break   

    print(string1)
    print(string2)
    print(string3)

    for i in string1: 
        if (i in string2) and (i in string3):
            result = priority.index(i) + 1 + result
            print("common char is ", i)

            print(priority.index(i))
            break
print("final",result)  
