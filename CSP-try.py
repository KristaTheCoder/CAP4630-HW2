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
    return student, distance
'''
Henrietta's deisgn was silver
'''
def hint2(student, color):
    if(student == "Henrietta" and color != "silver"):
        return
    if(student != "Henrietta" and color == "silver"):
        return
    return student, color

'''
FIXME
Omar's design went somewhat farther than the silver airplane.
This means he did not have the silver plane.
'''
def hint3a(student, color, distance):
    if(student == "Omar" and color == "silver"):
        return
    return student, color, distance


'''
FIXME
The pink plane went 10 feet further than the black plane
TODO: make sure that the final anwers are within 10 of eachother
'''
#try preprocessing need to figure out how to check all other in set
def hint5(color, distance):
    if(color == "pink" and distance == 15):
        return
    if(color == "black" and distance == 45):
        return
    return color, distance


problem.addConstraint(FunctionConstraint(hint1), ["students", "distances"])
#Check that hint 1 constraints are working
print len(problem.getSolutions())

#check that hint2 constraints are working
problem.addConstraint(FunctionConstraint(hint2), ["students", "colors"])
print len(problem.getSolutions())


#check that hint5 constraint is working.
problem.addConstraint(FunctionConstraint(hint5), ["colors", "distances"])
print len(problem.getSolutions())
