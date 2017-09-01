def quest():
    print "hello and welcome!"
    name = raw_input("what is your name?    ")
    print "welcome %s" %name
    quest = raw_input("what is your quest?  ")
    print "that's what i would've chosen."
    weapon = raw_input("which weapon will you choose?   ")
    print "solid choice. only the pros use that one."
    number = raw_input("please pick a number between 1-10   ").lower()
    if (len(number) > 0 and number.isdigit()) and (number < 10 and number > 1):
        print "was your number %s?" %(number)
    elif number > 10 or number < 1:
        print "you didn't pick a number bewteen 1-10"
    else:
        print "please choose a number"
        quest()
quest()

# which weapon will you choose?

# grafdy man. grafdy always beats
# rock, paper OR scissors

# if name != name:
#    print "you don't know your name."
# else:
#   print "hiya there %s" %(name)


