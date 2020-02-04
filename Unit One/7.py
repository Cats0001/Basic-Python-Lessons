# Miscellaneous + Project Prep

# To conclude this "unit", we will be covering some quality of life (QOL) coding tips, and other miscellaneous
# information. You will then be asked to complete a series of projects, increasing in difficulty. Requirements will be
# posted with each project and you are ENCOURAGED to either ask or google answers to questions. In programming,
# googling your questions and reading documentation is essential. Many entry-level programmers believe that "googling"
# the answers to specific errors and problems is cheating, but this can't be farther from the truth. Any programming
# teacher / professor work their salt will see this as using resources available to you. To this day, when I encounter
# an issue regarding my code, my first response is to google the specific question or find a link to the documentation
# of the module in question, if using a module.

# F-strings

# Want to print multiple variables in one line? F strings are your friend! You can do all sorts of operations
# within the context of an F string and only the result will be sent to console. For example:


wordOne = "You"
wordTwo = "will"
wordThree = "now"
wordFour = "be"
wordFive = "awkwardly"
wordSix = "stared"
wordSeven = "at."

print(f"{wordOne} {wordTwo} {wordThree} {wordFour} {wordFive} {wordSix} {wordSeven}")

# This can also be represented as a variable as this:

words = f"{wordOne} {wordTwo} {wordThree} {wordFour} {wordFive} {wordSix} {wordSeven}"

# And without an F string:

words = wordOne + ' ' + wordTwo + ' ' + wordThree + ' ' + wordFour + ' ' + wordFive + ' ' + wordSix + ' ' + wordSeven

# If you want to be advanced, you can also use a for loop and a list for this! This example will accept any number of
# words, and is more adaptable.

wordList = ["You", "will", "now", "be", "awkwardly", "stared", "at"]
words = ''
for word in wordList:
    words = words + word + ' '
print(words)

# Function definitions

# Want to create your own functions, to use later in your code? This is how. Examples below.


def function_name(parameter_one, parameter_two):  # function name and then parenthesis with the variables you require
    print(parameter_one)  # Any code you want here
    print(parameter_two)


# You can use the return statement to call a function and assign it's result to a variable, or simply
# print it to console.

def square(number_one, number_two):
    return number_one ** number_two


squaredNumbers = square(5, 2)
print(squaredNumbers)
print(square(5, 2))

# Classes can be used to incorporate many functions in one object. This style of code is known as "object oriented".
# Object-oriented programming will be covered more in the next unit, as this unit only covers basic syntax and
# operations.
