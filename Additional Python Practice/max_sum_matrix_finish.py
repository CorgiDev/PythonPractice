#############################################################################
# This is in progress. I have not finished it if this line is still here.
#
# Given a 2D Array of numbers, pick one number from each row.
#
# 1 2 3 4 9
# 9 4 5 6 3
# 3 4 5 6 7
#
# If you change columns between rows you must pay a penalty 
# equivalent to the difference between the 2 column locations 
# (going 1 - 5, not 0 - 5  for the column numbers for the purpose of this
# formula).
#
# abs(x-y)
#
# (i.e. if the first number came from column 5 but the second # number came
# from column 4, you'd take a penalty of 1.)
# Try to maximize the end total.
#############################################################################

#numberMatrix = [[1,2,3,4,9],[9,4,5,6,3],[3,4,5,6,7]]
numberMatrix = [[15,21,39,45,9],[95,12,50,16,30],[34,47,52,20,7]]

selection = []
maxTotal = 0
prevCharLoc = -1
newCharLoc = 0

for row in range(len(numberMatrix)):
    highestValue = 0
    print("Currently checking row #", row)

    for col in range(len(numberMatrix[row])):        
        totValue = 0

        # Set the penalty (-1 indicates first row which gets 0 penalty by default)
        if prevCharLoc == -1:
            penalty = 0
            # Calculate the value of the number after considering penalty
            totValue = numberMatrix[row][col]
        elif col != prevCharLoc:
            penalty = abs((col+1)-(prevCharLoc+1)) # The +1 ensures penalty still gets calculated if the the number is in the 0 column
            # Calculate the value of the number after considering penalty
            totValue = numberMatrix[row][col]-penalty

        # Replace the highest value for the row with the new value if it is higher
        if totValue > highestValue:
           highestValue = totValue
           # Ensures the character's location gets tracked so it can be used for calculating penalty on next row
           newCharLoc = col
    
    # Once a number is selected for the row, update prevCharLoc if needed
    if newCharLoc != prevCharLoc:
            prevCharLoc = newCharLoc

    print("The number selected from Row #", row , "is", highestValue)

    # Add new highest value to selection list
    print("The new highest value is", highestValue)
    selection.append(highestValue)
    print("") # Merely for asthetics and improved readability

print("The following are the max values, after peanlty subtraction, selected from each row:")
print(selection)

# Add new value to the total
maxTotal = sum(selection)

print("") # Merely for asthetics and improved readability
print ("The highest total obtainable from this matrix is", maxTotal)

# TODO: Need to alter to actually get the max value. 
# Second row impacts potential penalty in 3rd row, 
# and so on if there are more rows. So you have to think
# beyond just the penalty faced by the second row.