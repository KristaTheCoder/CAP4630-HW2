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
        return
    if(student != "Henrietta" and distance == 35):
        return
    return True
'''
Henrietta's deisgn was silver
'''
def hint2(student, color):
    if(student == "Henrietta" and color != "silver"):
        return
    if(student != "Henrietta" and color == "silver"):
        return
    return True

'''
FIXME
Omar's design went somewhat farther than the silver airplane.
'''
def hint3a(student, color, distance):
    #Omar does not have the silver plane
    if(student == "Omar" and color == "silver"):
        return
    #Silver plane cannot be the farthest
    if(color == "silver" and distance == 45):
        return
    #Omar's plane is not the shortest
    if(student == "Omar" and distance == 15):
        return
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
        return
    if(color == "black" and distance == 45):
        return
    return True

#pink is at most 10 feet further from farthest black plane
def hint5b():
    maxBlackDist = 0
    for instance in problem.getSolutions():
        if((instance.get("colors") == "black") and (instance.get("distances") > maxBlackDist)):
            maxBlackDist = instance.get("distances")
    return maxBlackDist

#black is at most 10 feet less than pink
def hint5c():
    minPinkDist = 45
    for instance in problem.getSolutions():
        if(instance.get("colors") == "pink"):
            minPinkDist = min(instance.get("distances"), minPinkDist)
    return minPinkDist

def hint5d(color, distance):
    if(color == "pink" and distance > (blackMax + 10)):
        return
    if(color == "black" and distance < (pinkMin - 10)):
        return
    return True

def main():

    problem.addConstraint(FunctionConstraint(hint1), ["students", "distances"])
    problem.addConstraint(FunctionConstraint(hint2), ["students", "colors"])
    problem.addConstraint(FunctionConstraint(hint3a), ["students", "colors", "distances"])
    silverMax = hint3b()
    problem.addConstraint(FunctionConstraint(hint3c), ["students", "distances"])
    problem.addConstraint(FunctionConstraint(hint5), ["colors", "distances"])
    blackMax = hint5b()
    pinkMin = hint5c()
    problem.addConstraint(FunctionConstraint(hint5d), ["colors", "distances"])



    print len(problem.getSolutions())
    print problem.getSolutions()

#set global variables
silverMax = 0
blackMax = 0
pinkMin = 45

if (__name__ == "__main__"):
    main()
