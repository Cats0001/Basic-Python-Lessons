# Loops

# Loops are repeating segments of code, and come in two types, while and for. Lets start with a "for" loop.

# "for" loops can be expressed in the following manner:

for i in range(0, 9):
    print(i)

# For loops work by repeating until the loop has executed a specific number of times, or until all values in a data
# structure have been accessed. We will touch more on using for loops with data structures later in this lesson. But
# first, lets dissect what this code segment is doing.

# We first see the characters "for", which indicate to the computer that the following code will be a for loop.

# The next part of the code is known as the "iterable", and in this example, every time the code is run it will be
# increased in value by one.

# Following the iterable, we see what looks like a function, and it is! Don't worry about what it is too much, all
# you need to know right now is that it sets the range for this function, meaning that it sets the starting value, and
# the value at which the for loop will terminate at. This value is stored in the iterable "i". In the above example, the
# loop will stop when i reaches the value of 9, not before or after, but exactly on. This is checked at the start of
# each loop execution ("iteration").

# What follows the semicolon is what action the for loop will perform, in this case, it will simply print the current
# value of i. This value will increase with each iteration of the loop. i is increased by one at the end of each
# iteration.

# If you have a keen eye, you may have noticed that the loop only goes from zero to eight! You may think this is a
# bug, as (0, 9) is clearly specified as the range for the function, but you must remember lesson zero and how loops
# work. The value starts at zero, which is printed to console, and terminates at 9, which is checked at the beginning
# of each iteration. This means that nine would never be printed, as nine is the number at which the loop terminates at.
# If you count how many numbers are printed to console, you'll also notice nine numbers are there, since you began
# counting at zero.

exampleList = [
    "This", "Is", "a", "Demonstration"
    ]

for i in exampleList:
    print(i)

# In this loop, you'll see we have dropped range() in favor of a list! This means that the loop will execute until
# every value in the loop becomes "i". Since we are calling print() for each value, all of the strings stored inside
# the list will be printed to console. You can do many advanced things with this, as you will soon learn.


# While loops

condition = True
while condition:
    print("Success")
    condition = False


# While loops are a form of conditional statement, and will only run while the condition being checked against is
# True (by default), or anything you change it to. Many of the ways to interact with standard conditional statements
# also apply to while loops.

condition = False

while not condition:
    print("Success")
    condition = True

# And of course, strings work too!

exampleString = "rain"

while exampleString == "rain":
    print("Success")
    exampleString = "water"

# While loops are important, because they have no definite end. You may need to execute one block of code until a
# certain condition is met, for example, in web scraping, you may check a website until you find a certain block
# of text. You may also want to use while loops in user interfaces to continually ask questions, or to keep a certain
# block of code running in order to continually execute your program.

# To finish this lesson, try out both kinds of loops for yourself! Feel free to ask any questions.







