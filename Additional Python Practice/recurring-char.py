# Identify the first recurring character in a given string
# Example string "DBCABA"

def first_recurring(given_string):
    # define hash table / dictionary
    counts = {}
    # for loop to check each character against the table to see if it is already there
    for char in given_string:
        # if it is return that character
        if char in counts:
            return char
        # if not add it to the table in a key value pair
        else:
            counts[char] = 1
    print("There are no recurring characters in the string.")

phrase = "DBCABA"

print(first_recurring(phrase))