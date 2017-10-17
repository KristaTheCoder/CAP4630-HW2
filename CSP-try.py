from constraint import *

#set-up problem
problem = Problem()
problem.addVariable("students", ["Ella", "Henrietta", "Omar", "Valerie"])
problem.addVariable("colors", ["black", "blue", "pink", "silver"])
problem.addVariable("distances", [15, 25, 35, 45])

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

def hint3b():
    #find max distance
    maxSilverDist = 0
    for instance in problem.getSolutions():
        if((instance.get("colors") == "silver") and (instance.get("distances") > maxSilverDist)):
            maxSilverDist = instance.get("distances")
    return maxSilverDist

#find all distances ahead of silver plane
def hint3c(student, distance):
    if(student == "Omar" and distance <= silverMax):
        return False
    return True
'''
Ella's design went 10 feet farther than the black plane
TODO account for distance portion
'''
def hint4(student, color, distance):
    ## Ella's plane is not the black plane
    if (student == "Ella" and color == "black"):
        return
    #Ella's plane is not the slowest plane
    if (student == "Ella" and distance != 15):
        return
    return True

'''
FIXME
The pink plane went 10 feet further than the black plane
TODO: make sure that the final anwers are within 10 of eachother
'''

def hint5(color, distance):
    #neither color can hold most extreme value
    if(color == "pink" and distance == 15):
        return False
    if(color == "black" and distance == 45):
        return False
    return True



def main():

    problem.addConstraint(FunctionConstraint(hint1), ["students", "distances"])
    problem.addConstraint(FunctionConstraint(hint2), ["students", "colors"])
    problem.addConstraint(FunctionConstraint(hint3a), ["students", "colors", "distances"])
    silverMax = hint3b()
    problem.addConstraint(FunctionConstraint(hint3c), ["students", "distances"])
    problem.addConstraint(FunctionConstraint(hint4), ["students", "colors", "distances"])
    problem.addConstraint(FunctionConstraint(hint5), ["colors", "distances"])
    print len(problem.getSolutions())
    for answer in problem.getSolutions():
        print answer
    print " "

    print len(problem.getSolutions())
    for answer in problem.getSolutions():
        print answer

#set global variables
silverMax = 0
blackMax = 0
pinkMin = 45

if (__name__ == "__main__"):
    main()
