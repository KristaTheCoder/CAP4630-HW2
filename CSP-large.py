from constraint import *
'''
The Daily Ray is either the vessel that went to Rainbow Reef or Captain Romero's Vessel
'''
def hint1(boat, location, captain):
    if(boat == "Daily Ray" and not ((location == "Rainbow Reef") != (captain == "Romero" ))):
        return False
    return True
'''
The vessel that went to Rainbow Reef saw fewer manatees than the Watery Pete
'''
def hint2(boat, location, manatee, WPboat_manatees):
    if(location == "Rainbow Reef"):
        #The watery pete did not go to rainbow reef
        if(boat == "Watery Pete"):
            return False
        #we Know WP is #3
        if(manatee >= WPboat_manatees):
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

'''
We know Ella is 10 more than the black plane
'''
def hint5a(distance0, color, distance):
     if(color == "black"):
         if(distance0 - distance == 10):
             return True
         return False
     else:
         return True

'''
Prints final set of answers for the CSP
'''
def answer_set(x):
    Ella = []
    Henrietta = []
    Omar = []
    Valerie = []
    answer_list = [Ella, Henrietta, Omar, Valerie]
    for a in x:
        if a[-1] == "0":
            Ella.append(x[a])
        if a[-1] == "1":
            Henrietta.append(x[a])
        if a[-1] == "2":
            Omar.append(x[a])
        if a[-1] in "3":
            Valerie.append(x[a])
    for person in answer_list:
        print person
def main():

    problem = Problem()
    boats = ["Daily Ray", "Foxy Roxy", "Samantha", "Watery Pete"]
    captains = ["Armstrong", "Jacobson", "Romero", "Yang"]
    locations = ["Arno's Spit", "Betty Beach", "Rainbow Reef", "Trey's Tunnel"]
    manatees = [3, 4, 5 ,6]

    for i in range(len(boats)):
        problem.addVariable("boats" + str(i), boats)
        problem.addVariable("captains" + str(i), captains)
        problem.addVariable("locations" + str(i), locations)
        problem.addVariable("manatees" + str(i), manatees)


    problem.addConstraint(AllDifferentConstraint())
    #boats is now the identifier
    problem.addConstraint(lambda a, b, c, d: a == "Daily Ray" and b == "Foxy Roxy" and c == "Samantha" and d == "Watery Pete", ("boats0", "boats1", "boats2", "boats3"))

    #FIXME: change for new problem all below
    for i in range(len(boats)):
        problem.addConstraint(FunctionConstraint(hint1), ["boats" + str(i), "locations" + str(i), "captains" + str(i)])
        problem.addConstraint(FunctionConstraint(hint2), ["boats" + str(i), "locations" + str(i), "manatees" + str(i), "manatees3"])
        # problem.addConstraint(FunctionConstraint(hint3a), ["students" + str(i), "colors" + str(i), "distances" + str(i)])
        # problem.addConstraint(FunctionConstraint(hint4), ["students" + str(i), "colors" + str(i), "distances" + str(i)])
        # problem.addConstraint(FunctionConstraint(hint5), ["students" + str(i), "colors" + str(i), "distances" + str(i)])

    #check within 10 of eachother
    # for i in range(len(colors)):
    #     problem.addConstraint(FunctionConstraint(hint5a), ["distances0", "colors" + str(i), "distances" + str(i)])

    print len(problem.getSolutions())
    # for answer in problem.getSolutions():
    #     answer_set(answer)


if (__name__ == "__main__"):
    main()
