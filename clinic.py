# clinic.py

def clinic():
    print "you've been chosen to represent the break lounge!"
    print "pick a number between 1-10"
    answer = raw_input("!!!	").lower()
    if answer == "1" or answer == "one":
        print "was your number %s!?" %(answer)
    elif answer == "2" or answer == "two":
        print "was your number %s!?" %(answer)
    elif answer == "3" or answer == "three":
        print "was your number %s!?" %(answer)
    elif answer == "4" or answer == "four":
        print "was your number %s!?" %(answer)
    elif answer == "5" or answer == "five":
        print "was your number %s!?" %(answer)
    elif answer == "6" or answer == "six":
        print "was your number %s!?" %(answer)
    elif answer == "7" or answer == "seven":
        print "was your number %s!?" %(answer)
    elif answer == "8" or answer == "eight":
        print "was your number %s!?" %(answer)
    elif answer == "9" or answer == "nine":
        print "was your number %s!?" %(answer)
    elif answer == "10" or answer == "ten":
        print "was your number %s!?" %(answer)
    else:
        print "you didn't pick a number! Try again.."
        clinic()
clinic()