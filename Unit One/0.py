# Lesson Zero
# How stuff works

# Take a minute to look at the number of this lesson, zero. This may be strange, as in most counting we start
# at the number one. This isn't true for computers, which start counting at the number zero.
# In a list, expressed as

exampleList = ["valueOne", "valueTwo", "ValueThree"]

# you can access the zeroth, first, and second value, but not the third even though there are three values
# stored within the list. There are still three values, but we take the "normal" counting number and subtract
# one to use it in programming. Eventually, if you code enough, you may find yourself counting from zero
# when even dealing in non-programming topics.

# Feel free to try accessing the values in the list, using the syntax below:

# exampleList[0]
# exampleList[1]
# exampleList[2]

# Now, you'll notice that I said the above data structure is known as a list. There are many types of data
# structures, and they are all used for different things. I'll go through some of the most basic structures below.

# DICTIONARY

exampleDict = {
    "keyOne": "valueOne",
    "keyTwo": "valueTwo",
    "keyThree": "valueThree"
}

# Dictionaries, often abbreviated as "dict", store a key and a value accessed by the key. This key can be a string,
# which is simply a set of characters stored by the computer. The key can also be another data type, including another
# dictionary if you so wish.

exampleNestedDict = {
    "dictKey": {
        "nested": "dictionary"
    }
}

exampleNestedList = {
    "listKey": [0, 1, 2, 3]
}

# You can access a dictionary by using the format below:

# exampleDict["keyOne"]
# exampleDict["keyTwo"]
# exampleDict["keyThree"]

# You can similarly access nested data structures like this:

# exampleNestedDict["dictKey"]["nested"]

# exampleNestedList["listKey"][0] (replace zero with the number of the value you want, which is known as an integer)

# LISTS

exampleList = ["valueOne",
               "valueTwo",
               "ValueThree"]

# See first section for more information on lists. Lists are an unordered data type that can be accessed by the integer
# position of the value you need. For the shown list, 0-2

# Strings

exampleString = "This is a string!"

# Strings are pretty basic, just a set of characters laid out in a computer-storable format.

# Integers

Integer = 5

# You know this one from math class, any whole number.

# Floats

Float = 0.23335

# You can remember these as a decimal number, but there are many ways of storing a decimal number. For now,
# just think of floats.


# Feel free to play around with any of these data types, as they are extremely useful to know. A strong programming
# talent is dependant on knowledge of the fundamentals.


