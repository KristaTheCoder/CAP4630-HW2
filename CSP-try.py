from constraint import *

#set-up problem



'''
Henrietta's design went 35 feet
'''
def hint1(student, distance):
    if(student == "Henrietta" and distance != 35):
        return False
    if(student != "Henrietta" and distance == 35):
        return False
    return True
'''
Henrietta's deisgn was silver
'''
def hint2(student, color):
    if(student == "Henrietta" and color != "silver"):
        return False
    if(student != "Henrietta" and color == "silver"):
        return False
    return True

'''
Omar's design went somewhat farther than the silver airplane.
'''
def hint3a(student, color, distance):
    #Omar does not have the silver plane
    if(student == "Omar" and color == "silver"):
        return False
    #Silver plane cannot be the farthest
    if(color == "silver" and distance == 45):
        return False
    #Omar's plane is not the shortest
    if(student == "Omar" and distance == 15):
        return False
    return True


'''
Ella's design went 10 feet farther than the black plane
'''
def hint4(student, color, distance):
    ## Ella's plane is not the black plane
    if (student == "Ella" and color == "black"):
        return False
    #Ella's plane is not the slowest plane
    if (student == "Ella" and distance == 15):
        return False
    if(color == "black" and distance == 45):
        return False
    return True

'''
The pink plane went 10 feet further than the black plane
'''

def hint5(student, color, distance):
    #Ella's plane when 10 feet further than black plane so Ella's is pink
    if(student == "Ella" and color != "pink"):
        return False
    if(student != "Ella" and color == "pink"):
        return False
    #neither color can hold most extreme value
    if(color == "pink" and distance == 15):
        return False
    if(color == "black" and distance == 45):
        return False
    return True

#filter black based on ella
def hint5a(color, distance):
    global ellaD
    if(color == "black"):
        if(distance + 10  in ellaD):
            return True
        else:
             return False
    return True


def main():

    print "main"
    problem = Problem()
    students1 = ["Ella", "Henrietta", "Omar", "Valerie"]
    colors1 = ["black", "blue", "pink", "silver"]
    distances1 = [15, 25, 35, 45]
    problem.addVariable("students", students1)
    problem.addVariable("colors", colors1)
    problem.addVariable("distances", distances1)

    problem.addConstraint(FunctionConstraint(hint1), ["students", "distances"])
    problem.addConstraint(FunctionConstraint(hint2), ["students", "colors"])
    problem.addConstraint(FunctionConstraint(hint3a), ["students", "colors", "distances"])
    problem.addConstraint(FunctionConstraint(hint4), ["students", "colors", "distances"])
    problem.addConstraint(FunctionConstraint(hint5), ["students", "colors", "distances"])

    #pink is 10 more than black
    for pink in problem.getSolutions():
        if(pink["colors"] == "pink"):
            possiblePink = False
            for black in problem.getSolutions():
                if(black["colors"] == "black"):
                    if(pink["distances"] - black["distances"] == 10):
                        possiblePink == True
            if( not possiblePink):
                problem.addConstraint(lambda a, b: not(a != pink["distances"] and b == pink["colors"]), ("distances", "colors"))

    print len(problem.getSolutions())
    for answer in problem.getSolutions():
        print answer.items()
    #black is 10 less than pink

    for black1 in problem.getSolutions():
        if(black1["colors"] == "black"):
            possibleBlack = False
            for pink1 in problem.getSolutions():
                if(pink1["colors"] == "pink"):
                    if(pink1["distances"] - black1["distances"] == 10):
                        possibleBlack == True
            if(not possibleBlack):
                problem.addConstraint(lambda a, b: not(a == black1["distances"] and b == black1["colors"]), ("distances", "colors"))

    problem.addConstraint(AllDifferentConstraint())

    print len(problem.getSolutions())
    for answer in problem.getSolutions():
        print answer

    #need all different between possible sets





if (__name__ == "__main__"):
    main()
