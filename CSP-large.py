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
The Boat that went to Rainbow Reef, Captain Yang's boat, and the Samantha are three different boats
'''
def hint3(boat, location, captain):
    #They are all mutually exlusive
    if(boat == "Samantha" and (location == "Rainbow Reef" or captain == "Yang")):
        return False
    if(location == "Rainbow Reef" and (boat == "Samantha" or captain == "Yang")):
        return False
    if(captain == "Yang" and (boat == "Samantha" or location == "Rainbow Reef")):
        return False
    return True


'''
The vessel that went to Betty Beach saw 2 more manatees than the boat that went to Rainbow Reef
'''
def hint4(student, color, distance):
    # try making a set intersection later come back to this

    return True

'''
The vessel that saw 5 manatees didn't go to Arno's Spit
'''
def hint5(location, manatee):
    #Ella's plane when 10 feet further than black plane so Ella's is pink
    if(manatee == 5 and location == "Arno's Spit"):
        return False
    return True

'''
The boat that saw 3 manatees is either Captain Yang's boat or the Samantha
'''
def hint6(boat, manatee, captain):
     if(manatee == 3):
         #One or the other
         if((captain == "Yang") != (boat == "Samantha")):
             return True
         return False
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
        problem.addConstraint(FunctionConstraint(hint3), ["boats" + str(i), "locations" + str(i), "captains" + str(i)])
        # problem.addConstraint(FunctionConstraint(hint4), ["students" + str(i), "colors" + str(i), "distances" + str(i)])
        problem.addConstraint(FunctionConstraint(hint5), ["locations" + str(i), "manatees" + str(i)])
        problem.addConstraint(FunctionConstraint(hint6), ["boats" + str(i), "manatees" + str(i), "captains" + str(i)])
    #check within 10 of eachother
    # for i in range(len(colors)):
    #     problem.addConstraint(FunctionConstraint(hint5a), ["distances0", "colors" + str(i), "distances" + str(i)])

    print len(problem.getSolutions())
    # for answer in problem.getSolutions():
    #     answer_set(answer)


if (__name__ == "__main__"):
    main()
