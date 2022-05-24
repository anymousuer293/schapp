# Import modules
import random as r
import numpy as np

class Question():
    def __init__(self, grade):
        self.grade = grade
    def math(self, topic: str):
        if self.grade == 0:
            if topic.lower() == "adding 1 digit numbers":
                    numerator = r.randrange(1, 10)
                    denominator = r.randrange(1, 10)
                    ri = 0
                    w = 0
                    bik = 0

                    a = input("What is {} + {}?".format(numerator, denominator))
                    if a == numerator + denominator:
                        print("That is right!")
                        ri += 1
                        bik += 1
                    else:
                        print("That is wrong!")
                        w += 1
                        bik += 1
                    

            if topic.lower() == "adding 2 digit numbers":
                    numerator = r.randrange(1, 25)
                    denominator = r.randrange(1, 25)
                    rig = 0
                    wr = 0
                    bike = 0

                    if int(str(numerator)[1]) + int(str(denominator)[1]) > 9:
                        denominator = r.randrange(1, 9-numerator)
                    
                    a = input("What is {} + {}".format(numerator, denominator))

                    if int(a) == numerator + denominator:
                        print("That is right!")
                        rig += 1
                        bike += 1
                    else:
                        print("That is wrong!")
                        wr += 1
                        bike += 1

            if topic.lower() == "skip counting":
                    skipcountingby = [2, 5, 10]
                    skipcountby = r.choice(skipcountingby)
                    howmanytimes = r.randrange(1,10)
                    wro = 0
                    righ = 0
                    bikes = 0

                    a = input("If you count by {}s {} times. How much do you get?:\n".format(skipcountby, howmanytimes))

                    if int(a) == skipcountby * howmanytimes:
                        print("That is right!")
                        righ += 1
                        bikes += 1
                    else:
                        print("That is wrong!")
                        wro += 1
                        bikes += 1

            if topic.lower() == "subtraction 1-10":
                    numerator = r.randrange(1,10)
                    denominator = r.randrange(1,10)

                    if str(numerator + denominator).startswith("-"):
                        denominator = r.randrange(1, 10-(10-numerator))
                    
                    wrong = 0
                    right = 0
                    bikesa = 0

                    a = input("What is {} - {}?\n".format(numerator, denominator))
                    if int(a) == numerator - denominator:
                        print("That is right!")
                        right += 1
                        bikesa += 1
                    else:
                        print("That is wrong!")
                        wrong += 1
                        bikesa += 1
                    
            if topic.lower() == "2 digit subtraction":
                    numerator = r.randrange(1, 25)
                    denominator = r.randrange(1, 25)
                    righte = 0
                    wron = 0
                    bikesar = 0

                    if str(numerator + denominator).startswith("-"):
                        denominator = r.randrange(1, 25-(25-numerator))
                        
                    a = input("What is {} + {}".format(numerator, denominator))

                    if int(a) == numerator - denominator:
                            print("That is right!")
                            righte += 1
                            b += 1
                    else:
                        print("That is wrong!")
                        wron += 1
                        bikesar += 1

            if topic.lower() == "odd or even":
                    oddoreven = r.randrange(1,100)

                    a = input("Is {} odd or even?\n".format(oddoreven))
                    wronged = 0
                    righted = 0
                    bikesare = 0

                    if a.lower() == 'odd' and oddoreven % 2 != 0:
                        print("That is right!")
                        righted += 1
                        bikesare += 1
                    elif a.lower() == 'even' and oddoreven % 2 == 0:
                        print("That is right!")
                        righted += 1
                        bikesare += 1
                    elif a.lower() != 'even' and oddoreven % 2 != 0:
                        print("That is wrong!")
                        wronged += 1
                        bikesare += 1
                    elif a.lower() != 'odd' and oddoreven % 2 == 0:
                        print("That is wrong!")
                        wronged += 1
                        bikesare += 1
        if self.grade == 1:
            if topic.lower() == '3 by 3 digit subtraction':
                