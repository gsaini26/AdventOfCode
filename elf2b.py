# X lose, Y Draw, Z win




# A X  each 4
# B X  one wins gets 8 two gets 1
# C X  one loses gets 3 two gets 7
# A Y  one loses gets 1 two gets 8
# A Z  one wins get 7 two gets 3
# B Z  one loses gets 2 two gets 9
# B Y each get 5
# C Z each get 6
# C Y one wins gets 9 two gets 2

totalScore=0
scoreOne=scoreTwo=0
f= open("input.txt", 'r')
for theline in f:
    print("line",theline[0], theline[2])
#A X = AZ
#A Y = AX
#A Z = AY

    if (theline[0]=='A' and theline[2]=='X'):
        line=theline.replace('X','Z')
    elif (theline[0]=='A' and theline[2]=='Y'):
        line=theline.replace("Y","X")
        print("after replacement")
        print(line)
    
    elif (theline[0]=='A' and theline[2]=='Z'):
        line=theline.replace('Z','Y')
#B X = BX
#B Y = BY
#B Z = BZ
# no change

#C X = CY
#C Y = CZ
#C Z = CX
    if (theline[0]=='B'):
        line=theline
 
 
    if (theline[0]=='C' and theline[2]=='X'):
        line=theline.replace('X','Y')
    elif (theline[0]=='C' and theline[2]=='Y'):
        line=theline.replace('Y','Z')
    elif (theline[0]=='C' and theline[2]=='Z'):
        line=theline.replace('Z','X')
 
 
    print("newline is ", line)
 
 
 
    if line[0] == 'A':    
        if line[2] == 'X':
            scoreOne = scoreTwo = 4
        elif line[2]=='Y': 
            scoreOne=1
            scoreTwo=8
        elif line[2]=='Z':
            scoreOne=7
            scoreTwo=3
 
    elif line[0]=='B':
        if line[2] == 'X':
            scoreOne=8
            scoreTwo=1 

        elif line[2]=='Y':        
            scoreOne=scoreTwo=5

        elif line[2]=='Z':
            scoreOne=2
            scoreTwo=9
    
    elif line[0] == 'C':
        
        if line[2] == 'X':
            scoreOne = 3
            scoreTwo = 7

        elif line[2]=='Y':        
            scoreOne=9
            scoreTwo=2

        elif line[2]=='Z':
            scoreOne=scoreTwo=6

        else:
            print("error")

    else:
        print("error")    
    totalScore=scoreTwo+totalScore

    #print("scoreOne", scoreOne, "scoreTwo", scoreTwo)
    print("totalScore", totalScore)