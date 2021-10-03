# This is in progress. I have not finished it if this line is still here.

# Given a Matrix of numbers, pick one number from each row.
#
# 1 2 3 4 9
# 9 4 5 6 3
# 3 4 5 6 7
#
# If you change columns between rows you must pay a penalty 
# equivalent to the difference between the 2 column numbers. 
# abs(x-y)
# (i.e. if the first number came from column 5 but the second 
# number came from column 4, you'd take a penalty of 1.)
# Try to maximize the end total.

numberMatrix = [[1,2,3,4,9],[9,4,5,6,3],[3,4,5,6,7]]

maxTotal = 0
prevCharLoc = 0
newCharLoc = 0
penalty = 0

for row in numberMatrix:
    pass
    for number in row:
        pass
    if newCharLoc != prevCharLoc:
        prevCharLoc = newCharLoc

print (maxTotal)