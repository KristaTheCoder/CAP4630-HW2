from pulp import *

prob = pulp.LpProblem("test1", pulp.LpMinimize)


colors = ["black", "blue", "pink", "silver"]
distances = [15,25, 35, 45]


#variables
Ella = LpVariable.dicts("ella", (colors, distances), 0, 1, LpInteger)
Henrietta =LpVariable.dicts("henrietta", (colors, distances), 0, 1, LpInteger)
Omar = LpVariable.dicts( "omar", (colors, distances), 0,1, LpInteger)
Valerie = LpVariable.dicts("valerie", (colors, distances), 0,1, LpInteger)
students = [Ella, Henrietta, Omar, Valerie]
prob += 0
for color in colors:
    for distance in distances:
        for student in students:
            prob += lpSum(student[color][distance]) == 1, ""





# for distance in distances:
#     prob += choices["Henrietta"]["silver"][distance] == 3, ""

prob.writeLP("planes.lp")

# The problem is solved using PuLP's choice of Solver
print len(prob.variables())
prob.solve()
print prob.variables()
