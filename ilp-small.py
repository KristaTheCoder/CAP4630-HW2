from pulp import *

prob = pulp.LpProblem("test1", pulp.LpMinimize)

#create 3D array, possible values are -1, not available = 0, answer is 1

students = ["Ella", "Henrietta", "Omar", "Valerie"]
colors = ["black", "blue", "pink", "silver"]
distances = [15, 25, 35, 45]

    #  The boxes list is created, with the row and column index of each square in each box
    #Create 3D box of possible answers
# Squares =[]
# for i in range(len(students)):
#     for j in range(len(colors)):
#         for k in range(len(distances)):
#             #intialize coordinates of boxes in 3D array
#             Squares += [[(4*i+m,4*j+l, 4*k+ n) for m in range(4) for l in range(4) for n in range(4)]]

Boxes =[]
for student in students:
    for color in colors:
        for distance in distances:
            #intialize coordinates of boxes in 3D array
            Boxes += [[(student,color, distance)]]
            
print Boxes
