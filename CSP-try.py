from constraint import *
problem = Problem()
problem.addVariable("students", ["Ella", "Henrietta", "Omar", "Valerie"])
problem.addVariable("colors", ["black", "blue", "pink", "silver"])
problem.addVariable("distances", [15, 25, 35, 45])
print len(problem.getSolutions())

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
    if(color == "pink" and distance == 15):
        return
    if(color == "black" and distance == 45):
        return
    return True

def hint5b():
    maxBlackDist = 0
    for instance in problem.getSolutions():
        if((instance.get("colors") == "silver") and (instance.get("distances") > maxSilverDist)):
            maxSilverDist = instance.get("distances")
    return maxSilverDist

def main():
    problem.addConstraint(FunctionConstraint(hint1), ["students", "distances"])
    print len(problem.getSolutions())
    problem.addConstraint(FunctionConstraint(hint2), ["students", "colors"])
    print len(problem.getSolutions())
    problem.addConstraint(FunctionConstraint(hint3a), ["students", "colors", "distances"])
    print len(problem.getSolutions())
    problem.addConstraint(FunctionConstraint(hint3c), ["students", "distances"])
    print len(problem.getSolutions())
    problem.addConstraint(FunctionConstraint(hint5), ["colors", "distances"])
    print len(problem.getSolutions())

silverMax = hint3b()
blackMax = hint5b()
if (__name__ == "__main__"):
    main()
