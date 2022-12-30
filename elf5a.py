import re

f = open("mini5a.txt",'r')
#read in the file line by line.
#allItems contains the crates
count=0
for line in f:
    # remove the new line
    firstLine = line.strip()
    # if hit a blank line, skip it
    print(firstLine)
    if firstLine == '':
        continue
    elif firstLine[0] == 'm':
    # if hit a line starting with m, it is a move line. save the digits and remove the words
        moveItems = re.findall(r"\d", firstLine)
        # NEED TO ADD or append moveItems to a list of lists
    # change the strings to ints
        moveItems = list(map(int, moveItems))
        print("move items", moveItems)
    elif firstLine!='' and firstLine[0] != 'm' and firstLine[0] != '1':
        #allItems = re.search(r"\w", firstLine)
        allItems = re.sub(r"[\]", "", firstLine)

        # NEED TO ADD or append allItems to a list of lists. Is there a prepend or does it have to be append?
        
        
        print(allItems)
        # append the line read in to a list of lists
    
    else: 
        continue    
#at the end of the loop, all items have been read in and added to moveItems or allItems
f.close()

    

