# ##########################################
# Example file for variables
# ##########################################

###########################################
# # Declare a variable and initialize it

# f=0
# print(f)

###########################################
# # re-declaring the variable works

# f="abcd"
# print(f)

###########################################
# # ERROR: variables of different types cannot be combined

# # print("This is a string " + 123)

###########################################
# # ERROR Resolved by converting the int to a string

# print("This is a string " + str(123))

###########################################
# Global vs. local variables in functions

f = 0

def someFunction():
    global f
    f="def"
    print(f)

someFunction()
print(f)

del f
print(f)