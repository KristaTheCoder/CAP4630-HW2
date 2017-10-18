from constraint import *
import numpy

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

#Run recursive until down to 4 solutions
def sMax():
    maxSilverDist = 0
    for instance in problem.getSolutions():
        if((instance.get("colors") == "silver") and (instance.get("distances") > maxSilverDist)):
            maxSilverDist = instance.get("distances")
    return maxSilverDist

#find all distances ahead of silver plane
def hint3c(student, distance):
    global silverMax
    if(student == "Omar" and distance <= silverMax):
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

#Ella's distances:
def ellaDistances():
    global ellaD
    for instance in problem.getSolutions():
        if(instance["students"] == "Ella"):
            ellaD.insert(0, instance["distances"])


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
    problem.addConstraint(FunctionConstraint(hint1), ["students", "distances"])
    problem.addConstraint(FunctionConstraint(hint2), ["students", "colors"])
    problem.addConstraint(FunctionConstraint(hint3a), ["students", "colors", "distances"])
    problem.addConstraint(FunctionConstraint(hint4), ["students", "colors", "distances"])
    problem.addConstraint(FunctionConstraint(hint5), ["students", "colors", "distances"])

    #Greater than silver constraint
    global silverMax
    silverMax = sMax()
    problem.addConstraint(FunctionConstraint(hint3c), ["students", "distances"])

    global ellaD
    ellaDistances()
    problem.addConstraint(FunctionConstraint(hint5a), ["colors", "distances"])

    print len(problem.getSolutions())
    for answer in problem.getSolutions():
        print answer


#set global variables
silverMax = 0
ellaD = []
blackBack = []
if (__name__ == "__main__"):
    main()
