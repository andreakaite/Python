print()
print()
print('CS118 Spring 2019')
print('Andrea Gray')
print('M02 Exercise Test 01')
print()

print('_____________________________________________________________________________')
#####################################################################################

# This exam is closed book.
# You will use IDLE and may use the help()function.
# There are 75 points possible on this test.
# Problems are worth various ammounts based on difficulty.
# Your total points will be divided by 5 for your final test score.
# A perfect score of 75 is worth the total 15 gradebook points.
# Correct answers for the inclass submission earn full points.
# You must submit your .py file within the time limit of the class.
# Be certain to save your .py file from the IDLE editor NOT the shell.
# I must be able to execute your entire .py test program in order to grade it.


#####################################################################################

# Out of class solutions.
# Correct answers for the out of class submission will earn HALF OF THE POINT VALUE. 
# Out of class submission must NOT include previously solved or unsolved problems.
# Delete code that was submitted in class or is not solved.
# You must submit your .py file by the out of class deadline.
# Be certain to save your .py file from the IDLE editor NOT the shell.
# I must be able to execute your entire .py test program in order to grade it.

#####################################################################################

'''

# Problem 1. (1 point for each solution, 12 possible. These must be answered in class)
print()
print('Problem 1:')
print()

# What data type is the RESULT of each of the following?
# You may not use the shell for this problem.
# If the each data type were asigned to a varible and you entered type(variable)
# What would be returned.


### a. 5

print('   a.','integer')
print()

### b. 5.0

print('   b.','float')
print()

### c. 5 > 1

print('   c.','boolean')
print()

### d. '5'

print('   d.','character')
print()

### e. 5 * 2

print('   e.','integer')
print()

### f. '5' * 2

print('   f.','string, character array')
print()

### g. '5' + '2'

print('   g.','concatenated string, character array')
print()

### h. 5 / 2

print('   h.','float division, float')
print()

### i. 5 // 2

print('   i.','floor division, integer')
print()

### j. [5, 2, 1]

print('   j.','array')
print()

### k. 5 in [1, 4, 6]

print('   k.','boolean')
print()

### l. math.pi

print('   l.','float using built in math library')
print()

print('_____________________________________________________________________________')

#####################################################################################

# Problem 2. (2 points for each solution, 20 possible. May be answered out of class for half value.)

print()
print('Problem 2:')
print()

# Write (evaluate and print) Python expressions that compute:

### a.	The product of 1111111 with itself.

# Enter code below this point.



# Create a variable with that evaluates the answer(value).

prob2a = 1111111**2

# Print the answer by entering the variable name next to the comma.

print('   a.', prob2a)  
print()


### b.	How many times does 81 go into 1000?

# Evalaute the answer here.



# Create a variable that evaluates the answer.

prob2b = 1000//81

# Print the answer by entering the variable name next to the comma.

print('   b.', prob2b)    
print()


### c.	What is the remainder when 1000 is divided by 81?

# Evalaute the answer here.



# Create a variable that evaluates the answer.

prob2c = 1000 % 81

# Print the answer by entering the variable name next to the comma.

print('   c.', prob2c)    
print()


### d.	You scored 90/100, 95/100 and 87/100: what is your average score on these three exams?

# Evalaute the answer here.



# Create a variable that evaluates the answer.

prob2d = ((0.9 + 0.95 + 0.87) / 3) * 100

# Print the answer by entering the variable name next to the comma.

print('   d. (out of 100)', prob2d)    
print()


### e.	You scored 90/100, 46/50, 55/60 and 66/70: what is your best score percentage on these four exams?

# Evalaute the answer here.

score1 = 90 / 100
score2 = 46 / 50
score3 = 55 / 60
score4 = 66 / 70
grades = [score1, score2, score3, score4]

# Create a variable that evaluates the answer.

prob2e = max(grades)

# Print the answer by entering the variable name next to the comma.

print('   e.', prob2e)    
print()

### f.	You scored 90/100, 46/50, 55/60 and 66/70: what is the lowest score percentage?

# Evalaute the answer here.

# using variables defined in part e

# Create a variable that evaluates the answer.

prob2f = min(grades)

# Print the answer by entering the variable name next to the comma.

print('   f.', prob2f)    
print()

### g.	The sum of the numbers 7 to 17.

# Evalaute the answer here.

numberList1 = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# Create a variable that evaluates the answer.

prob2g = sum(numberList1)

# Print the answer by entering the variable name next to the comma.

print('   g.', prob2g)    
print()


### h.	The product of the numbers 1 to 10.

# Evalaute the answer here.

numberList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
incrementation1 = 0
prob2h = 1
while incrementation1 < 10:
    prob2h *= numberList2[incrementation1]
    incrementation1 += 1

# Create a variable that evaluates the answer.



# Print the answer by entering the variable name next to the comma.

print('   h.', prob2h)    
print()


### i.	A Kb (kilobyte) is really 1024 bytes, where 1024 is 2 raised to the power 10:
#           how many bytes are there in a gigabyte (2 raised to the power 30)?

# Evalaute the answer here.



# Create a variable that evaluates the answer.

prob2i = 2**30

# Print the answer by entering the variable name next to the comma.

print('   i. (in bytes)', prob2i)    
print()


### j.	There are 8 bits in a byte. A bit is either 0 or 1. A bit is 2 to the power of 1, also equal to its number of encodings.
#       What are the number of different encodings of 8 bits.

# Evalaute the answer here.



# Create a variable that evaluates the answer.

prob2j = 2**8

# Print the answer by entering the variable name next to the comma.

print('   j.', prob2j)    
print()


print('_____________________________________________________________________________')

#####################################################################################

# Problem 3. (2 point for each solution, 6 possible. May be answered out of class for half value.)
print()
print('Problem 3:')
print()

# Write Python expressions or assignments as specified:

# Assign x to be 5, y to be 10, and z to be 8.

x = 5
y = 10
z = 8


### a.	Write an expression that evaluates and prints the average of x, y and z.

# Evalaute the answer here.



# Create a variable that evaluates the answer.

prob3a = (x + y + z) / 3

# Print the answer by entering the variable name next to the comma.

print('   a.', prob3a)    
print()



### b.	Write an expression that evaluates and prints the largest value among x, y, and z.

# Evalaute the answer here.



# Create a variable that evaluates the answer.

prob3b = max(x, y, z)

# Print the answer by entering the variable name next to the comma.

print('   b.', prob3b)    
print()


### c.	Write an expression that evaluates and prints the median value among x, y, and z
#           (Hint: the median of a, b, and c is a+b+c - max{a,b,c} - min{a,b,c}.)

# Evalaute the answer here.


# Create a variable that evaluates the answer.

prob3c = (x + y + z) - max(x, y, z) - min(x, y, z)

# Print the answer by entering the variable name next to the comma.

print('   c.', prob3c)    
print()

print('_____________________________________________________________________________')

#####################################################################################

'''

# Problem 4. (2 point for each solution, 8 points possible. May be answered out of class for half value.)
print()
print('Problem 4:')
print()

'''

# Write (evaluate and print) Python expressions that answer these questions:

### a.	How many letters are there in 'Supercalifragilisticexpialidocious'?

# Evalaute the answer here.

string1 = 'Supercalifragilisticexpialidocious'

# Create a variable that evaluates the answer.

prob4a = len(string1)

# Print the answer by entering the variable name next to the comma.

print('   a.', prob4a)    
print()


### b.	Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring?

# Evalaute the answer here.



# Create a variable that evaluates the answer.

prob4b = 'ice' in string1

# Print the answer by entering the variable name next to the comma.

print('   b.', prob4b)    
print()


### c.	Which of the following words is the longest: Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or Bababadalgharaghtakamminarronnkonn?

# Evalaute the answer here.

string2 = 'Honorificabilitundinitatibus'
string3 = 'Bababadalgharaghtakamminarronnkonn'
length1 = len(string1)
length2 = len(string2)
length3 = len(string3)
if length1 > length2 & length1 > length3:
    prob4c = length1
elif length2 > length1 & length2 > length3:
    prob4c = length2
else:
    prob4c = length3

# Create a variable that evaluates the answer.



# Print the answer by entering the variable name next to the comma.

print('   c.', prob4c)    
print()

'''

### d.	Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?

# Evalaute the answer here.

prob4d = ['Berlioz','Borodin','Brian','Bartok','Bellini','Buxtehude','Bernstein']
prob4d.sort()

# Print the answer by entering the variable name next to the comma.

print('   d.', prob4d[0])    
print()

print('_____________________________________________________________________________')

'''

#####################################################################################

# Problem 5. (2 point for each solution, 6 points possible. May be answered out of class for half value.)

print()
print('Problem 5:')
print()

### a.	Write an expression creating a new list called roman, containing the strings 'Julius', 'Augustus', 'Brutus', and 'Cassius'. Print the list.

# Evalaute the answer here.

roman = ['Julius', 'Augustus', 'Brutus', 'Cassius']


# Print the answer by entering the variable name next to the comma.

print('   a.', roman)    
print()


### b.	Write an expression creating a list called english, containing the strings 'Dickens', 'Austen', 'Henry', and 'Elizabeth'. Print the list.

# Evalaute the answer here.

english = ['Dickens', 'Austen', 'Henry', 'Elizabeth']


# Print the answer by entering the variable name next to the comma.

print('   b.', english)    
print()


### c.	Now write an expression creating a list called rulers, containing the first two elements of roman and the last two elements of english.
#       Use list manipulation expressions; do not just copy the data manually. Print the list.

# Evalaute the answer here.

rulers = [roman[0], roman[1], english[2], english[3]]

# Print the answer by entering the variable name next to the comma.print()
print('   c.', rulers)    
print()


print('_____________________________________________________________________________')

#####################################################################################

# Problem 6. (3 point for each solution, 12 points total. May be answered out of class for half value.)

print()
print('Problem 6:')
print()

# Write (evaluate and print) Python expressions that answer the below questions regarding a list lst of scores of 15 deliverables: 

lst = [94, 86, 85, 81, 86, 96, 91, 85, 86, 83, 89, 81, 86, 98, 84]


### a.	What are the lowest, highest, and average score?
# Evalaute the answer here.

averageLst = sum(lst) / len(lst)

# Create variables that evalulate each answer.

prob6a = [min(lst), max(lst), averageLst]

# Print the (comma separated) answers by entering the variable names next to the comma.

print('   a.', prob6a)    
print()


### b.	What is the median score?
#       The median is the middle point of a number set, in which half the numbers are above the median and half are below.

# Evalaute the answer here.


# Create a variable that evaluates the answer.

prob6b = sum(lst) - max(lst) - min(lst)

# Print the answer by entering the variable name next to the comma.
print('   b.', prob6b)    
print()


### c.	What is the range of the scores?
#       Range is the difference between the lowest and highest values.

# Evalaute the answer here.


# Create a variable that evaluates the answer.

prob6c = max(lst) - min(lst)

# Print the answer by entering the variable name next to the comma.
print('   c.', prob6c)    
print()


### d.	How many of the scores are 85?

# Evalaute the answer here.

prob6d = 0
lstIncrement = len(lst)
while lstIncrement <= 0:
    if 85 in lst[lstIncrement]:
        prob6d += 1
    lstIncrement -= 1

# Create a variable that evaluates the answer.


# Print the answer by entering the variable name next to the comma.
print('   d.', prob6d)    
print()


print('_____________________________________________________________________________')

'''

#####################################################################################

# Problem 7. (4 points for this solution. May be answered out of class for half value.)
print()
print('Problem 7:')
print()

# Assume you already have a list defined, called name, containing three strings: a person’s first, middle, and last name, in that order.

#       Write an expression that produces a string consisting of the person’s last name followed by a comma and space,
#       then the first name and a space, then the person’s middle initial followed by a period. So, for example,
#       if name is equal to ['John', 'Phillip', 'Sousa'], your expression will produce the string 'Sousa, John P.'
#       Print the result.
name = ['John', 'Phillip', 'Sousa']
print(name[2] + ", " + name[0] + " " + name[1][0] + ".")

print('_____________________________________________________________________________')

#####################################################################################

# Problem 8. (3 points for this solution. May be answered out of class for half value.)
print()
print('Problem 8:')
print()

# Assume you already have a list defined, called numbers, containing only numeric values.

#       Write an expression that finds the product of the largest and smallest values in the list.
#       For example, if the list is [4, 1, 0.5, 10, 6], your expression would find the product of 0.5 and 10.
#       Print the result.

numbers = [4, 1, 0.5, 10, 6]
product = min(numbers) * max(numbers)
print(product)

print('_____________________________________________________________________________')

#####################################################################################

# Problem 9. (4 points for this solution. May be answered out of class for half value.)
print()
print('Problem 9:')
print()

# Assume you already have a list defined, called numbers, containing only numeric values.

#       Write code (you may need more than one expression, or to manipulate the list in some way)
#       that finds the sum of the second-largest and second-smallest values in the list.
#       For example, if the list is [4, 1, 0.5, 10, 6], your code would find the sum of 1 and 6.
#       Print the result.

numbers.remove(max(numbers))
numbers.remove(min(numbers))
product2 = min(numbers) * max(numbers)
print(product2)

print('_____________________________________________________________________________')
