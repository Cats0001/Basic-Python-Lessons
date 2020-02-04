# Conditional Statements

atHome = True
watchingNetflix = True

# A conditional statement ONLY executes when it's value is equal to whatever it is being compared to, which is defaulted
# to "True", or another "truthy" value. For now, focus on True itself. This means that the following example will only
# run the print() functions IF atHome is set to True.

if atHome:
    print("I am at home")

# Here is another example:

if watchingNetflix:
    print("I am watching netflix")

# A & operator will tell the computer to only run the code if the first AND second conditions are met, in this case,
# you must be atHome and watchingNetflix for this code to run.

if atHome & watchingNetflix:
    print("I am at home watching netflix")

# There are more levels of sophistication as well, you can add code that will run if the condition is not met as well
# by using an else statement.

watchingNetflix = False

if atHome & watchingNetflix:
    print("I am at home watching netflix")
else:
    print("I am not at home watching netflix")

# You can also directly compare to see if the condition is not met, by using "if not"

if not atHome & watchingNetflix:
    print("I am not at home watching netflix")

# In addition, you can compare directly to False, True, or any other value you desire! See the examples below.

example = True

if example == True:
    print("Example is equal to true")

valueOne = "test"

if valueOne == "test":
    print("valueOne is equal to the string 'test' ")

# To compare multiple values in one statement, where you only expect one outcome at a time, you can use an "else if"
# statement, which is expressed as an "elif" in python

one = False
two = False
three = True

if one:
    print("One is True")
elif two:
    print("Two is True")
else:
    print("One and Two are false, so three is True!")


# To finish this lesson, play around with conditional statements! Try comparing some values you set yourself.
