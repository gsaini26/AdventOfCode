f = open("mini4a.txt",'r')
firstRange = f.readline().strip()
twoItems = firstRange.split(',')
firstNum = twoItems[0].split('-')
secondNum = twoItems[1].split('-')

print(firstNum, " ", secondNum, " ")



