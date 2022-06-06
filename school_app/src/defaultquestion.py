# Import modules
import random as r
import numpy as np

#todo: get all the default topics for math, reading, science, and social studies

class DefaultQuestion():
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
                    else:
                        print("That is wrong!")
                        wronged += 1
                        bikesare += 1
        if self.grade == 1:
            if topic.lower() == '3 by 3 digit subtraction':
                numerator = r.randrange(1,500)
                denominator = r.randrange(1,500)

                wronged = 0
                righted = 0
                b = 0

                if str(numerator - denominator).startswith("-"):
                    denominator = r.randrange(1, 500-(500-numerator))

                a = input("What is {} - {}?\n".format(numerator, denominator))

                if int(a) == numerator - denominator:
                    print("That is right!")
                    b += 1
                    righted += 1
                else:
                    print("That is not right!")
                    b += 1
                    wronged += 1
            if topic.lower() == '2 by 2 digit subtraction':
                numerator = r.randrange(1,100)
                denominator = r.randrange(1,100)

                wronged = 0
                righted = 0
                b = 0

                if str(numerator - denominator).startswith("-"):
                    denominator = r.randrange(1, 100-(100-numerator))

                a = input("What is {} - {}?\n".format(numerator, denominator))

                if int(a) == numerator - denominator:
                    print("That is right!")
                    b += 1
                    righted += 1
                else:
                    print("That is not right!")
                    b += 1
                    wronged += 1
            if topic.lower() == '1 by 1 digit subtraction':
                numerator = r.randrange(1,10)
                denominator = r.randrange(1,10)

                wronged = 0
                righted = 0
                b = 0

                if str(numerator - denominator).startswith("-"):
                    denominator = r.randrange(1, 10-(10-numerator))

                a = input("What is {} - {}?\n".format(numerator, denominator))

                if int(a) == numerator - denominator:
                    print("That is right!")
                    b += 1
                    righted += 1
                else:
                    print("That is not right!")
                    b += 1
                    wronged += 1
            if topic.lower() == '3 by 3 digit addition':
                numerator = r.randrange(100,500)
                denominator = r.randrange(100,500)

                wronged = 0
                righted = 0
                b = 0


                a = input("What is {} + {}?\n".format(numerator, denominator))

                if int(a) == numerator + denominator:
                    print("That is right!")
                    b += 1
                    righted += 1
                else:
                    print("That is not right!")
                    b += 1
                    wronged += 1
            if topic.lower() == '2 by 2 digit addition':
                numerator = r.randrange(10,100)
                denominator = r.randrange(10,100)

                wronged = 0
                righted = 0
                b = 0


                a = input("What is {} + {}?\n".format(numerator, denominator))

                if int(a) == numerator + denominator:
                    print("That is right!")
                    b += 1
                    righted += 1
                else:
                    print("That is not right!")
                    b += 1
                    wronged += 1
            if topic.lower() == '1 by 1 digit addition':
                numerator = r.randrange(1,10)
                denominator = r.randrange(1,10)

                wronged = 0
                righted = 0
                b = 0


                a = input("What is {} + {}?\n".format(numerator, denominator))

                if int(a) == numerator + denominator:
                    print("That is right!")
                    b += 1
                    righted += 1
                else:
                    print("That is not right!")
                    b += 1
                    wronged += 1
            if topic.lower() == '1 by 1 digit multiplication':
                numerator = r.randrange(1,5)
                denominator = r.randrange(1,5)

                wronged = 0
                righted = 0
                b = 0


                a = input("What is {} x {}?\n".format(numerator, denominator))

                if int(a) == numerator * denominator:
                    print("That is right!")
                    b += 1
                    righted += 1
                else:
                    print("That is not right!")
                    b += 1
                    wronged += 1
            if topic.lower() == 'sides of shapes':
                shapesides = {"Circle": 0, "Triangle": 3, "Square": 4, "Pentagon": 5, "Hexagon": 6}
                shapes = ['Circle', 'Triangle', 'Square', 'Pentagon', 'Hexagon']
                randomshape = r.choice(shapes)

                wronged = 0
                righted = 0
                b = 0

                a = input("How many sides does a {} have?".format(randomshape))

                if int(a) == shapesides[randomshape]:
                    print("That is right!")
                    righted += 1
                    b += 1
                else:
                    print("That is wrong!")
                    wronged += 1
                    b += 1
            if topic.lower() == 'vertices of shapes':
                shapesides = {"Circle": 0, "Triangle": 3, "Square": 4, "Pentagon": 5, "Hexagon": 6}
                shapes = ['Circle', 'Triangle', 'Square', 'Pentagon', 'Hexagon']
                randomshape = r.choice(shapes)

                wronged = 0
                righted = 0
                b = 0

                a = input("How many vertices does a {} have?".format(randomshape))

                if int(a) == shapesides[randomshape]:
                    print("That is right!")
                    righted += 1
                    b += 1
                else:
                    print("That is wrong!")
                    wronged += 1
                    b += 1
            if topic.lower() == 'sides of solids':
                shapesides = {"Sphere": 0, "Triangular Prism": 5, "Cube": 6, "Rectangular Prism": 6, "Cone": 1, "Cylinder": 2}
                shapes = ['Sphere', 'Trianglular Prism', 'Cube', 'Rectangular Prism', 'Cone', 'Cylinder']
                randomshape = r.choice(shapes)

                wronged = 0
                righted = 0
                b = 0

                a = input("How many sides does a {} have?".format(randomshape))

                if int(a) == shapesides[randomshape]:
                    print("That is right!")
                    righted += 1
                    b += 1
                else:
                    print("That is wrong!")
                    wronged += 1
                    b += 1
            if topic.lower() == 'vertices of solids':
                shapesides = {"Sphere": 0, "Triangular Prism": 6, "Cube": 8, "Rectangular Prism": 8, "Cone": 0, "Cylinder": 0}
                shapes = ['Sphere', 'Trianglular Prism', 'Cube', 'Rectangular Prism', 'Cone', 'Cylinder']
                randomshape = r.choice(shapes)

                wronged = 0
                righted = 0
                b = 0

                a = input("How many vertices does a {} have?".format(randomshape))

                if int(a) == shapesides[randomshape]:
                    print("That is right!")
                    righted += 1
                    b += 1
                else:
                    print("That is wrong!")
                    wronged += 1
                    b += 1
            if topic.lower() == 'edges of solids':
                shapesides = {"Sphere": 0, "Triangular Prism": 9, "Cube": 12, "Rectangular Prism": 12, "Cone": 0, "Cylinder": 0}
                shapes = ['Sphere', 'Trianglular Prism', 'Cube', 'Rectangular Prism', 'Cone', 'Cylinder']
                randomshape = r.choice(shapes)

                wronged = 0
                righted = 0
                b = 0

                a = input("How many edges does a {} have?\n".format(randomshape))

                if int(a) == shapesides[randomshape]:
                    print("That is right!")
                    righted += 1
                    b += 1
                else:
                    print("That is wrong!")
                    wronged += 1
                    b += 1
        elif self.grade == 2:
            if topic.lower() == "1 by 1 digit multiplication":
                numerator = r.randrange(1, 10)
                denominator = r.randrange(1, 10)

                a = input("What is {} x {}?\n".format(numerator, denominator))
                if int(a) == numerator * denominator:
                    print("That is right!")
                else:
                    print("That is wrong!")
            elif topic.lower() == "plain geometry sides":
                shapesides = {"Circle": 0, "Triangle": 3, "Square": 4, "Pentagon": 5, "Hexagon": 6, "Heptagon": 7, "Octogon": 8, "Nonagon": 9, "Decagon": 10, "Hendecagon": 11}
                shapes = ["Circle", "Triangle", "Square", "Pentagon", "Hexagon", "Octogon", "Nonagon", "Decagon", "Hendecagon"]
                randomshape = r.choice(shapes)

                a = input("How many sides does a {} have?\n".format(randomshape))

                if int(a) == shapes[randomshape]:
                    print("That is right!")
                else:
                    print("That is wrong!")
            elif topic.lower() == "plain geometry vertices":
                shapesides = {"Circle": 0, "Triangle": 3, "Square": 4, "Pentagon": 5, "Hexagon": 6, "Heptagon": 7, "Octogon": 8, "Nonagon": 9, "Decagon": 10, "Hendecagon": 11}
                shapes = ["Circle", "Triangle", "Square", "Pentagon", "Hexagon", "Octogon", "Nonagon", "Decagon", "Hendecagon"]
                randomshape = r.choice(shapes)

                a = input("How many sides does a {} have?\n".format(randomshape))

                if int(a) == shapes[randomshape]:
                    print("That is right!")
                else:
                    print("That is wrong!")
            elif topic.lower() == "addition up to 1000":
                numerator = r.randrange(1,750)
                denominator = r.randrange(1,750)

                a = input("What is {} + {}?\n".format(numerator, denominator))

                if numerator + denominator > 1000:
                    denominator = r.randrange(1, 750-(750-numerator))
                    
                if int(a) == numerator + denominator:
                    print("That is right!") # print "That is right!"
                else:
                    print("That is wrong!") # print "That is wrong!"