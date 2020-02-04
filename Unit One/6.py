# Modules, common functions, and how to use them

import random, time

# See the code segment above, this imports two modules!  Modules are predetermined bits of code used to enhance your
# own code without requiring excess effort. If someone has already made a module to accomplish what you need, there is
# typically no reason to go through the hassle of writing it yourself.

# Modules can be used in many different ways, but for this example we will try some common functions from both the
# random and time modules. These modules are so useful and essential to the language, that they are always located
# in any python installation.

# Lets start with the random module, more specifically random.randint().

randomNumber = random.randint(0, 100)

# This will assign a random number, from zero to one hundred, to the variable randomNumber. If you haven't figured it
# out by now, variables hold information to be used later. Variables are the things that you've seen on the left side
# of expressions with an equal sign operator.

# randint is different than loops and iterables, in that it will pull both the lowest and highest number you enter.
# In the above example, it is possible to both have randomNumber be assigned to 0 or 100.

randomFloat = random.random()

# random.random() is similar to randomNumber, but it does not need any parameters (the things passed into functions).
# random() will return a random float, between 0.0 and 1.0.

exampleList = ['a', 'b', 'c', 'd']

choice = random.choice(exampleList)

# random.choice will choose a random option from any list, as shown above. Variable choice could be set to any of the
# first four letters of the alphabet.


# And now, on to time.

# One of the most functions in the time module is time.sleep, which allows you to pause execution of your program for
# a certain amount of time measured in seconds.

time.sleep(1)

# This code segment will pause the execution of your code for one second, and give whatever is running a slight delay.
# sleep() is useful in while loops, to not overload your system with continual requests to execute a code segment, among
# other things.

theTime = time.time()

# time.time() doesn't take any parameters, and will return the time in seconds passed system epoch, meaning when
# "time started" for that computer system. Most modern systems count seconds since January 1, 1970, 00:00:00. While
# time.time() is not that useful for telling the date, it is great for measuring time elapsed. See the example below.

startTime = time.time()
time.sleep(1)
endTime = time.time()

timeElasped = endTime-startTime
print(timeElasped)

# While not included in either of these modules, another helpful function is input(). input() allows you to ask the user
# to enter a value to be stored by the computer for use later in the program. This could be useful in a program which
# requires the user to input the dimensions of a rectangle in order to find it's area, or anything else where a user
# would need to supply information.

userInput = input("Please enter something to continue this program: ")

# Modules, and built in functions, often have documentation meant to show programmers like you how they work, without
# forcing you to read through their source code in order to understand every little thing the program does. You can
# typically search "module name" + documentation in order to find the official documentation for the module.





