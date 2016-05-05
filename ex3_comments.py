# LPTHW Exercise 3: Numbers and Math http://learnpythonthehardway.org/book/ex3.html
# Completed 5.5.2016
#Learn about numbers and math in python. (Use python as a calculator) BONUS GOAL : 1.Above each line, use the # to write a comment to yourself explaining what the line does.

#Print text statement to clarify unit we are counting (chickens)
print "I will now count my chickens:"
# Uses order of operations to give number of hens: divides 30 by 6 (5) and then adds 25. Returns 30.
print "Hens", 25 + 30 / 6
# Uses order of operations number of roosters: multiplies 25*3 (75), divides the result by 4 (72 R 3)and returns the remainder (3). 
# Then the remainder is taken from 100 (100 - 3). Returns 97
print "Roosters", 100 - 25 * 3 % 4
#Print text statement to clarify unit we are counting (eggs)
print "Now I will count the eggs:"
# Uses order of operations to give number of eggs: First finds the remainder of 4/2 (0). Then divides -1/4 (-.25). 
# Finally adds 3+2+1-5+0-.25+6 (6.75) Because numbers are whole numbers not float python rounds up. Returns 7. 
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# print statement to let user know what we are testing.
print "Is it true that 3 + 2 < 5 - 7?"
# solves each side of the equation and then tests to see if the value returned on the left side is LESS THAN than the  value returned on the right side. 
#Returns False.
print 3 + 2 < 5 - 7
# Print the math problem we are asking python to solve. Python then solves the  equation. Returns 5.
print "What is 3 + 2?", 3 + 2
# Print the math problem we are asking python to solve. Python then solves the  equation. Returns -2
print "What is 5 - 7?", 5 - 7
# Print statement referring to the false result on line 20.
print "Oh, that's why it's False."
# Print text
print "How about some more."
# Checks each side of the equation and checks to see if the value on left  side is GREATER THAN the  value on the right side.
# Returns True 
print "Is it greater?", 5 > -2
# Checks each side of the equation and checks to see if the value on left  side is GREATHER THAN OR EQUAL TO the  value on the right side.
# Returns True
print "Is it greater or equal?", 5 >= -2
# Checks each side of the equation and checks to see if the value on left  side is LESS THAN OR EQUAL TO the  value on the right side.
# Returns False
print "Is it less or equal?", 5 <= -2
