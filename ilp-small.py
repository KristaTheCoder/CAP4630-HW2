from pulp import *

'''
Groups unique answer sets and prints results
'''
def group(num, prob):
    print "Set: ",  num + 1, "  "
    for var in prob.variables():
        if value(var) == num:
            print var

def problem1():
    prob = LpProblem("problem1")
    #Each variable belongs to 1 of 4 sets, hence 0 through 3
    distances = LpVariable.dicts("distance", [15,25,35,45], 0,3, LpInteger)
    students = LpVariable.dicts("student", ['Ella','Henrietta','Omar','Valerie'], 0,3, LpInteger)
    colors = LpVariable.dicts("color", ['black','blue','pink','silver'], 0,3, LpInteger)
    Vars = [distances, students, colors]
    prob += lpSum(Vars)

    #set one variable as identifier for an answer set
    prob += distances[15] == 0
    prob += distances[25] == 1
    prob += distances[35] == 2
    prob += distances[45] == 3

    #Ensures that each instance of each variable occurs exactly once
    for var in Vars:
        prob += lpSum(var) == 6

    prob += students['Henrietta'] == distances[35]
    prob += students['Henrietta'] == colors['silver']
    prob += students['Omar'] >= colors['silver']+1
    prob += students['Ella'] == colors['black']+1
    prob += colors['black'] == students['Ella']-1
    prob += colors['pink'] == colors['black']+1

    prob.solve()
    for i in range(4):
        group(i, prob)

def main():
    problem1()

if (__name__ == "__main__"):
    main()
