from pulp import *

'''
Groups unique answer sets and prints results
'''
def group(num, prob):
    print "Set: ",  num + 1, "  "
    for var in prob.variables():
        if value(var) == num:
            print var

def problem2():
    prob = LpProblem("problem2")
    b = ["Daily Ray", "Foxy Roxy", "Samantha", "Watery Pete"]
    c = ["Armstrong", "Jacobson", "Romero", "Yang"]
    l = ["Arno's Spit", "Betty Beach", "Rainbow Reef", "Trey's Tunnel"]
    m = [3, 4, 5 ,6]

    # Each variable belongs to 1 of 4 sets, hence 0 through 3
    boats = LpVariable.dicts("boats", b, 0,3, LpInteger)
    captains = LpVariable.dicts("captains", c, 0,3, LpInteger)
    locations = LpVariable.dicts("locations", l, 0,3, LpInteger)
    manatees = LpVariable.dicts("manatees", m, 0, 3, LpInteger)
    Vars = [boats, captains, locations, manatees]

    # Objective, all variables occur once
    prob += lpSum(Vars)

    # Set one variable as identifier for an answer set
    # use manatees as identifer because we will need the numerical ordering from the hints
    j = 0
    for i in manatees:
        prob += manatees[i] == j
        j += 1

    # Ensures that each instance of each variable occurs exactly once
    for var in Vars:
        prob += lpSum(var) == 6

    # Add Constraints from hints
    # The Daily Ray is either the vessel that went to Rainbow Reef or Captain Romero's vessel
    print len(prob.variables())
    #FIXME: hint s1
    # prob += boats["Daily Ray"] == locations["Rainbow Reef"] or captains["Romero"]
    #The vessel that went to Rainbow Reef saw fewer manatees than the WateryPete
    prob += locations["Rainbow Reef"] <= (boats["Watery Pete"] - 1) #Note program gets bitchy af when you don't use the <= instead of <
    prob += boats["Watery Pete"] >= (locations["Rainbow Reef"] + 1)
    #The boat that went to Rainbow Reef, Captain Yang's boat, and the Samantha are three different boats
    prob += locations["Rainbow Reef"] != captains["Yang"]
    prob += locations["Rainbow Reef"] != boats["Samantha"]
    prob += boats["Samantha"] != captains["Yang"]
    print len(prob.variables())

    prob.solve()
    print len(prob.variables())
    print("Status:", LpStatus[prob.status])
    for i in range(4):
        group(i, prob)

def main():
    problem2()

if (__name__ == "__main__"):
    main()
