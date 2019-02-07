# CS118 Spring 2019
# Andrea Gray
# M02 Problem Set 01 V02
# Version 2 : Updates were made to the formatting of the document and its output.

# Chapter 2 p. 45-48
# Problems: 11-18, 20-22, 24-27

print("Problem solutions below are printed out in print statments.")
print("Note: quotation marks for strings are shown as ' in print statments.\n")

# x is the variable for printing whitespace before the problem header.
x = 33 * " "

#----------#
#    11    #
#----------#
print(x + "Problem 2.11\n")
print(x + "~~~~~~~~~~~~")

## 11.a
# Write an expression of the sum of integers -7 through -1
intSum = -7 + -6 + -5 + -4 + -3 + -2 + -1
print("a) %d" %intSum)
print("\n")

## 11.b
# Write an expression of the average age of a group of kids ata summer camp
# given that 17 are 9 years old, 24 are 10 years old, 21 are 11 years old, and
# 27 are 12 years old
nine = 17
ten = 24
eleven = 21
twelve = 27
total = nine + ten + eleven + twelve
average = total / 4
print("b) %.2f" %average)
print("\n")

## 11.c
# Write an expression of 2 to the power -20
twoPower = 2**(-20)
print("c) %G" %twoPower)
print("\n")

## 11.d
# Write an expression of the number of times 61 goes into 4356
sixtyOneDivision = 4356 / 61
print("d) %.2f" %sixtyOneDivision)
print("\n")

## 11.e
# Write an expression of the remainder when 4365 is divided by 61
sixtyOneRemainder = 4365 % 61
print("e) %.2f" %sixtyOneRemainder)
print("\n")

#----------#
#    12    #
#----------#
print(x + "Problem 2.12\n")
print(x + "~~~~~~~~~~~~")
# Evaluate the assignments
s1 = '-'
s2 = '+'
# Now write string expressions involving s1 and s2 and string operators + and *
# that evaluate to:

## 12.a
# '-+'
print(s1 + s2)
print("\n")

## 12.b
# '-+-'
print(s1 + s2 + s1)
print("\n")

## 12.c
# '+--'
print(s2 + (s1 * 2))
print("\n")

## 12.d
# '+--+--'
print(2 * (s2 + (s1 * 2)))
print("\n")

## 12.e
# '+--+--+--+--+--+--+--+--+--+--+'
print((10 * (s2 + (s1 * 2))) + s2)
print("\n")

## 12.f
# '+-+++--+-+++--+-+++--+-+++--+-+++--'
print(5 * (s2 + s1 + (3 * s2) + (2 * s1)))
print("\n")

#----------#
#    13    #
#----------#
print(x + "Problem 2.13\n")
print(x + "~~~~~~~~~~~~")
# Write the expressions using string s
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# and the indexing operator that evaluate to 'a', 'c', 'z', 'y', and 'q'

print(alphabet[0])
print(alphabet[2])
print(alphabet[25])
print(alphabet[24])
print(alphabet[16])
print("\n")

#----------#
#    14    #
#----------#
print(x + "Problem 2.14\n")
print(x + "~~~~~~~~~~~~")
goodbye = 'goodbye'
# Write a boolean expression that checks whether:

## 14.a
# The first character of string s is 'g' - True
if goodbye[0] == "g":
    print("a) True\n")
else:
    print("a) False\n")

## 14.b
# The seventh character of s is 'g' - False
if goodbye[6] == "g":
    print("b) True\n")
else:
    print("b) False\n")

## 14.c
# The first two characters of s are 'g' and 'a' - False
if goodbye[0] == "g" and goodbye[1] == "a":
    print("c) True\n")
else:
    print("c) False\n")

## 14.d
# The next to last character of s is 'x' - False
sLength = len(goodbye);
if goodbye[sLength - 1] == "x":
    print("d) True\n")
else:
    print("d) False\n")

## 14.e
# The middle character of s is 'd' - True
middleOfS = (len(goodbye)-1) / 2
middleOfSI = int(middleOfS)
if goodbye[middleOfSI] == "d":
    print("e) True\n")
else:
    print("e) False\n")

## 14.f
# The first and last characters of string s are equal - False
if goodbye[0] == goodbye[len(goodbye)-1]:
    print("f) True\n")
else:
    print("f) False\n")

## 14.g
# The last four chatacters of string s match the string 'tion' - False
lastFour = len(goodbye) - 4
if goodbye[lastFour : len(goodbye)] == "tion":
    print("g) True\n")
else:
    print("g) False\n")

#----------#
#    15    #
#----------#
print(x + "Problem 2.15\n")
print(x + "~~~~~~~~~~~~")
# Write the Python expressions corresponding to these statments:

## 15.a
# The number of characters in the word "anachronistically" is 1 more than the
# number of characters in the word "counterintuitive"
word1 = "anachronistically"
word2 = "counterintuitive"
if len(word1) == (len(word2) + 1):
    print("a) True\n")
else:
    print("a) False\n")

## 15.b
# The word "misinterpretation" appears earlier in the dictionary than the word
# "misrepresentation"
word3 = "misinterpretation"
word4 = "misrepresentation"
outerLoopIncrement = 0
innerLoopIncrement = 0
inWord3 = 0
inWord4 = 0
while outerLoopIncrement < len(word3):
    while innerLoopIncrement < len(alphabet):
        if word3[outerLoopIncrement] == alphabet[outerLoopIncrement]:
            inWord3 = outerLoopIncrement
        if word4[outerLoopIncrement] == alphabet[outerLoopIncrement]:
            inWord4 = outerLoopIncrement
        if inWord3 == inWord4:
            outerLoopIncrement += 1
        elif inWord3 > inWord4:
            break
        else:
            break
    if inWord3 == inWord4:
        innerLoopIncrement += 1
    elif inWord3 < inWord4:
        print("b) Misinterpretation comes first in the dictionary.\n")
        break
    else:
        print("b) Misrepresentation comes first in the dictionary.\n")
        break

## 15.c
# The letter "e" does not appear in the word "floccinaucinihilipilification"
longWord = "floccinaucinihilipilification"
if "e" in longWord:
    print("c) True\n")
else:
    print("c) False\n")

## 15.d
# The number of characters in the word "counterrevolution" is equal to the sum
# of the number of characters in words "counter" and "resolution"
oneWord = "counterrevolution"
firstHalf = "counter"
secondHalf = "resolution"
twoWords = firstHalf + secondHalf
if len(oneWord) == len(twoWords):
    print("d) True\n")
else:
    print("d) False\n")

#----------#
#    16    #
#----------#
print(x + "Problem 2.16\n")
print(x + "~~~~~~~~~~~~")
# Write the corresponding Python assignment statments:

## 16.a
# Assign 6 to variable a and 7 to variable b
a = 6
b = 7
print("a) Variables assignment.\n")

## 16.b
# Assign to variable c the average of variables a and b
c = (a + b) / 2
print("b) variable c is the average of a and b. c = %.2f" %c)
print("\n")

## 16.c
# Assign to variable inventory the list containing strings 'paper', 'staples',
# and 'pencils'.
inventory = ["paper", "staples", "pencils"]
print("c) created an inventory list:")
print(inventory)
print("\n")

## 16.d
# Assign to variables 'first', 'middle', and 'last' the strings "John",
# "Fitzgerald", and "Kennedy"
first = "John"
middle = "Fitzgerald"
last = "Kennedy"
print("d) first = 'John'")
print("   middle = 'Fitzgerald'")
print("   last = 'Kennedy'")
print("\n")

## 16.e
# Assign to variable 'fullname' the concatenation of string variables 'first',
# 'middle', and 'last'. Make sure you incoorporate blank spaces appropriately
space = " "
fullname = first + space + middle + space + last
print("e) Fullname is printed: ")
print(fullname)
print("\n")

#----------#
#    17    #
#----------#
print(x + "Problem 2.17\n")
print(x + "~~~~~~~~~~~~")
# Using variables defined in Exercise 2.16, write Boolean expressions
# corresponding to the following logical statments and evaluate the expressions:

## 17.a
# The sum of 17 and -9 is less than 10
# unsure how to incoorporate exerecise 2.16 into this problem...
summation = 17 + (-9)
if summation < 10:
    print("a) True\n")
else:
    print("b) False\n")

## 17.b
# The length of list inventory is more than five times the length of string
# 'fullname'
inventoryCat = inventory[0] + inventory[1] + inventory[2]
FNFive = 5 * fullname
if len(inventoryCat) == len(FNFive):
    print("b) True\n")
else:
    print("b) False\n")

## 17.c
# c is no more than 24
if c <= 24:
    print("c) True\n")
else:
    print("c) False\n")

## 17.d
# 6.75 is between the values of integers a and b
if (6.75 < b) and (6.75 > a):
    print("d) True\n")
else:
    print("d) False\n")

## 17.e
# The length of string 'middle' is larger than the length of string 'first' and
# smaller than the length of string 'last'
if (len(middle) > len(first)) and (len(middle) < len(last)):
    print("e) True\n")
else:
    print("e) False\n")

## 17.f
# Either the list inventory is empty or it has more than 10 objects in it
if (len(inventory) == 0) or (len(inventory) > 10):
    print("f) True\n")
else:
    print("f) False\n")

#----------#
#    18    #
#----------#
print(x + "Problem 2.18\n")
print(x + "~~~~~~~~~~~~")
# Write Python statments corresponding to the following:

## 18.a
# Assigning to variable 'flowers' a list containing strings "rose", "bougainvillea",
# "yucca", "marigold", "daylilly", and "lilly of the valley".
flowers = ["rose", "bougainvillea", "yucca", "marigold", "daylilly", "lilly of the valley"]
print("a) Creating a flowers list.\n")

## 18.b
# Write a Boolean expression that evaluates to True if string "potato" is in the
# list 'flowers', and evaluate the expression.
if "potato" in flowers:
    print("b) True\n")
else:
    print("b) False\n")

## 18.c
# Assign to list 'thorny' the sublist consisting of the first three objects in
# 'flowers'
thorny = [flowers[0], flowers[1], flowers[2]]
print("c) Assigning the first three items in flowers to a list thorny.\n")

## 18.d
# Assign to list 'poisonous' the sublist consisting of just the last object of
# 'flowers'
flowerLength = len(flowers)
poisonous = [flowers[flowerLength - 1]]
print("d) Assigning the last object in flowers to a list poisonous.\n")

## 18.e
# Assign to list 'dangerous' the concatenation of lists 'thorny' and 'poisonous'
dangerous = thorny + poisonous
print("e) Assigning to list dangerous the concatenation of lists thorny and poisonous.\n")

#----------#
#    20    #
#----------#
print(x + "Problem 2.20\n")
print(x + "~~~~~~~~~~~~")
# Write an expression involving a three-letter string s that evaluates to a string
# whose characters are the characters of s in reverse order. If s is 'top', the
# expression should evaluate to 'pot'
threeLetterS = "dog"
sReverse = ["", "", ""]
print("The original word is: ", threeLetterS)
pTwentyIncrement = len(threeLetterS) - 1
backwardsIncrement = 0
while pTwentyIncrement > -1:
    sReverse[backwardsIncrement] = threeLetterS[pTwentyIncrement]
    pTwentyIncrement -= 1
    backwardsIncrement += 1
sReverseS = sReverse[0] + sReverse[1] + sReverse[2]
print("The word reversed is: ",  sReverseS)
print("\n")

#----------#
#    21    #
#----------#
print(x + "Problem 2.21\n")
print(x + "~~~~~~~~~~~~")
# Write an expression involving strings s and t containing the last name and the
# first name, respectively, of a person that evaluates to the person's initials.
# If the two strings contained the first and last name of the book's author, the
# expression would evaluate to 'LP'
sFirst = "Andrea"
tLast = "Gray"
initials = sFirst[0] + tLast[0]
print("Initials are " + initials + "\n")

#----------#
#    22    #
#----------#
print(x + "Problem 2.22\n")
print(x + "~~~~~~~~~~~~")
# The range of a list of numbers is the largest difference between any two numbers
# in the list. Write a Python expression that computes the range of a list of
# numbers 'lst'. If the list 'lst' is, say, [3, 7, -2, 12], the expression
# should evaluate to 14 (the difference between 12 and -2).
lst = [3, 7, -2, 12]
minimum = min(lst) 
maximum = max(lst)
rangeLst = maximum - minimum
print("The range of the list is %d" %rangeLst)
print("\n")


#----------#
#    24    #
#----------#
print(x + "Problem 2.24\n")
print(x + "~~~~~~~~~~~~")
# Start by assigning to variable 'grades' a list containing an arbitrary sequence
# of grades (strings) "A", "B", "C", "D", and "F". For example:
grades = ["B", "B", "F", "C", "B", "A", "A", "D", "C", "D", "A", "A", "B"]
# Write a sequence of Python statments that ultimately produce a list count that
# contains the numbers of occurrences of each grade in list 'grades' in
# alphabetic order. For the given example, the list count should be
# [4, 4, 2, 2, 1].
gradesIncrement = 0
countGrades = [0, 0, 0, 0, 0]
while gradesIncrement <= (len(grades) - 1):
    if grades[gradesIncrement] == "A":
        countGrades[0] += 1
    elif grades[gradesIncrement] == "B":
        countGrades[1] += 1
    elif grades[gradesIncrement] == "C":
        countGrades[2] += 1
    elif grades[gradesIncrement] == "D":
        countGrades[3] += 1
    else:
        countGrades[4] += 1
    gradesIncrement += 1
print(grades)
print(countGrades)
print("\n")

#----------#
#    25    #
#----------#
print(x + "Problem 2.25\n")
print(x + "~~~~~~~~~~~~")
# Repeat problem 2.24 with the following modification: variable 'grades' is
# defined to be of type 'tuple' rather than type 'list':
gradesT = ("B", "B", "F", "C", "B", "A", "A", "D", "C", "D", "A", "A", "B")
# Variable count should still refer to a list
tupleCounter = 0
countGradesT = [0, 0, 0, 0, 0]
while tupleCounter <= len(gradesT) - 1:
    if gradesT[tupleCounter] == "A":
        countGradesT[0] += 1
    elif gradesT[tupleCounter] == "B":
        countGradesT[1] += 1
    elif gradesT[tupleCounter] == "C":
        countGradesT[2] += 1
    elif gradesT[tupleCounter] == "D":
        countGradesT[3] += 1
    else:
        countGradesT[4] += 1
    tupleCounter += 1
print(gradesT)
print(countGradesT)
print("\n")

#----------#
#    26    #
#----------#
print(x + "Problem 2.26\n")
print(x + "~~~~~~~~~~~~")
# A dartboard of radius 10 and the wall it is hanging on are represented using
# the two-dimensional coordinate system, with the board's center at coordinate
# (0,0). Variables x and y store the x- and y-coordinate of a dart hit. Write an
# expression using variables x and y that evaluates to True if the dart hits
# (is within) the dartboard, and evaluate the expression for those dart
# coordinates:

## 26.a
# (0,0)

## 26.b
# (10,10)

## 26.c
# (6,-6)

## 26.d
# (-7,8)

boardHits = ((0,0), (10, 10), (6, -6), (-7, 8))
boardCounter = 0
while boardCounter < 4:
    if (boardHits[boardCounter][0] <= 10) and (boardHits[boardCounter][1] <= 10):
        print("True -- Hit in the board radius")
    else:
        print("False")
    boardCounter += 1
print("\n")

#----------#
#    27    #
#----------#
print(x + "Problem 2.27\n")
print(x + "~~~~~~~~~~~~")
# A ladder put up right against a wall will fall over unless put up at a certain
# angle less than 90 degrees. Given variables 'length' and 'angle' storing the
# length of the ladder and the angle that it forms with the ground as it leans
# against the wall, write a Python expression involving 'length' and 'angle'
# that computes the height reached by the ladder. Evaluate the expression for
# these values of 'length' and 'angle':
# Will need the function height = length * sin(angle)
# The math module sin() takes its input in radians. Therefore you will need to
# convert the angle given in degrees to the angle given in raidians using:
# randians = (pi * degrees) / 180

## 27.a
# 16 feet and 75 degrees

## 27.b
# 20 feet and 0 degrees

## 27.c
# 24 feet and 45 degrees

## 27.d
# 24 feet and 80 degrees
import math
ladderSpecs = ((16, 75), (20, 0), (24, 45), (24, 80))
ladderCounter = 0
while ladderCounter < 4:
    radians = (math.pi * ladderSpecs[ladderCounter][1]) / 180
    height = (ladderSpecs[ladderCounter][0]) * math.sin(radians)
    print("Ladder %d will reach a height of %.2f." %(ladderCounter, height))
    ladderCounter += 1
