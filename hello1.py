# this object and method will print 
# the current time and date down to the 
# millionth of a second
from datetime import datetime
now = datetime.now()

# this will prompt a user for input and 
# save the user input to a variable
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
name = raw_input("what art thou name? ")
quest = raw_input("what art thou quest? ")
color = raw_input("what art thou favorite color? ")
random = raw_input("pick a number between 1 and 10 ")

# this will print the variable "random"
print "was your number %s? :-)" % (random)

# this will print the "name" "quest" and 
# "color" variables
print "so, your name is %s, and your quest is %s, your favorite color is %s?" % (name, quest, color)

# this will propt the user for input and 
# save the input to a variable
answer = raw_input("Y or N ")

# this will ask the user if the information 
# was correct
print "are you sure your answer is %s?" %(answer)
print "would you like to sign up for our newsletter?"

# this will propt the user for input and 
# save the input to a variable
newsletter = raw_input("Y or N ")


# this section is to mess with someone who 
# didn't read the source code before they 
# ran the program.
print "sorry our newsletter isn't available. visit wwww.qwerty.net for info."
enter = raw_input("Press Enter.")

# this section is more for the pause effect 
# of knowing your root directry was just deleted
print "connection established. beginning deletion of \"/\" directory."
raw_input()

# this completes the prank, they obviously know their 
# root directory wasn't delted because their computer 
# is probably still working   """
print "....process completed", now , "Good Bye, %s." % (name)


# this will prompt a user for input
# then it will save the input to a 
# function vriable. variables 
# saved within a function are not
# available globally
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()
clinic()


# this version is very wrong
# the ending else statement 
# doesn't take arguments or options
def quest():
    myList = [1,2,3,4,5,6,7,8,9,10]
    print "hello and welcome!"
    name = raw_input("what is your name?")
    print "welcome %s" %name
    quest = raw_input("what is your quest?")
    print "that's what i would've chosen."
    weapon = raw_input("which weapon will you choose?")
    print "solid choice. only the pros use that one."
    number = raw_input("please pick a number between 1-10")
    if number = myList:
        print "was your number %s" %(number)
    else number != myList:
        print "please pick a number between 1-10"
        quest()
quest()