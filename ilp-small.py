from pulp import *

prob = pulp.LpProblem("test1", pulp.LpMinimize)

#possible values are 1 impossible are 0
students = ["Ella", "Henrietta", "Omar", "Valerie"]
colors = ["black", "blue", "pink", "silver"]
distances = [15,25, 35, 45]


Boxes =[]
for student in students:
    for color in colors:
        for distance in distances:
            #intialize coordinates of boxes in 3D array
            Boxes += [[(student,color, distance)]]

# 3D array of all possible options
print Boxes

choices = LpVariable.dicts("Choice",(students,colors,distances),0,1,LpInteger)
prob += 0

# A constraint ensuring that only one value can be in each square is created
#this may not be necessary initially set to all possible solutions
for student in students:
    for color in colors:
        for distance in distances:
           prob += lpSum([choices[student][color][distance]]) == 1, ""

#There can only be one true solution in each
for student in students:
    for color in colors:
        for distance in distances:
            #hint 1
            if((student == "Henrietta") != (distance == 35)):
                prob += choices[student][color][distance] == 0, ""
            #hint 2
            if((student == "Henrietta") != (color == "silver")):
                prob += choices[student][color][distance] == 0, ""



# for distance in distances:
#     prob += choices["Henrietta"]["silver"][distance] == 3, ""

prob.writeLP("planes.lp")

# The problem is solved using PuLP's choice of Solver
print len(prob.variables())
prob.solve()
print len(prob.variables())

for student in students:
    for color in colors:
        for distance in distances:
            if(value(choices[student][color][distance]) == 1):
                print choices[student][color][distance]
