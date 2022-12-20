
# A X rock 1, B Y paper 2, C Z scissors 3

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
for line in f:
    print("line",line[0], line[2])
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