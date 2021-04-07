from Cage import *
from Animal import *
from Node import *
import numpy as numpy

fringe = []
cages = []
animals = []
assignment = []

number_of_cages, number_of_animals, number_of_vicinities = input().split()

neighbours_cage = [[] for x in range(int(number_of_cages))]
enemies = [[] for w in range(int(number_of_animals))]

conflicts = [[] for z in range(int(number_of_animals))]

cages_size = input().split()

animals_size = input().split()

for i in range(int(number_of_vicinities)):
    n = input().split()
    neighbours_cage[int(n[0]) - 1].append(int(n[1]) - 1)
    neighbours_cage[int(n[1]) - 1].append(int(n[0]) - 1)

for i in range(int(number_of_animals)):
    conflicts[i] = input().split()

for i in range(int(number_of_animals)):
    for j in range(int(number_of_animals)):
        if conflicts[i][j] == '0':
            enemies[i].append(j)

for i in range(int(number_of_animals)):
    animals.append(Animal(i, animals_size[i], enemies[i]))

for i in range(int(number_of_cages)):
    cages.append(Cage(i, cages_size[i], neighbours_cage[i]))

# assign enemies
for i in range(int(number_of_animals)):
    enemy = []
    for j in enemies[i]:
        enemy.append(animals[j])

    animals[i].enemies = enemy

# assign neighbours
for i in range(int(number_of_cages)):
    neighbour = []
    for j in neighbours_cage[i]:
        neighbour.append(cages[j])

    cages[i].Neighbour_cages = neighbour


def having_confilict(check_cage, check_animal, assignment):
    if check_cage.size < check_animal.size:
        return True
    # checking neighbour each cage have enemy with assignment
    for a in check_cage.Neighbour_cages:
        for b in assignment:
            if a == b[0]:
                if b[1] in check_animal.enemies:
                    return True
    return False


def order_domain_values(assignment):
    new_domain = animals.copy()
    for index in assignment:
        if index[1] in new_domain:
            new_domain.remove(index[1])
    return new_domain


def is_complete(assignment):
    return len(assignment) == int(number_of_cages)


def select_unassigned_varibles(node):
    new_cage = cages.copy()
    count = int(number_of_cages)
    domain = numpy.copy(node.domain)
    for ite in node.assignment:
        if ite[0] in new_cage:
            domain[ite[0].number] = None
    number = 100
    index = 1
    for it in range(count):
        if domain[it] is not None:
            if len(domain[it]) < number:
                number = len(domain[it])
                index = it
    return new_cage[index]


def gettingNewDomain(preNode, temp):
    newDoamin = preNode.domain.copy()
    newDoamin[temp[0].number] = temp
    return newDoamin


def forwardChecking(node,assignment):
    new_ass = assignment.copy()
    old_ass = node.assignment.copy()
    for i in node.domain:
        for assignment[1] in i:
            print(numpy.argwhere(j))
            # numpy.delete(domain , numpy.argwhere())




def recursive_backtracking(node):
    if is_complete(node.assignment):
        return node.assignment
    Current_cage = select_unassigned_varibles(node)
    for Current_animal in order_domain_values(node.assignment):
        if not having_confilict(Current_cage, Current_animal, node.assignment):
            temp = [Current_cage, Current_animal]
            new_assignment = node.assignment.copy()
            new_assignment.append(temp)
            new_node = Node(node, new_assignment, gettingNewDomain(node, temp))
            result = recursive_backtracking(new_node)
            if result is not None:
                return result
        if [Current_cage, Current_animal] in node.assignment:
            node.assignment.remove([Current_cage, Current_animal])
    return None


def backtracking():
    domain1 = [[0 for x in range(int(number_of_cages))] for y in range(int(number_of_animals))]
    for i in range(int(number_of_cages)):
        domain1[i] = animals.copy()
    node = Node(None, [], domain1)
    return recursive_backtracking(node)


backtracking1 = backtracking()
for b in backtracking1:
    print(b[0].number, ": ", b[1].number)

'''
6 6 5
1 2 4 2 3 3
3 1 2 1 2 2
1 2
2 3
3 4
4 5
4 6
1 0 1 0 1 1
0 1 0 0 1 0
1 0 1 1 1 1
0 0 1 1 1 0
1 1 1 1 1 1
1 0 1 0 1 1
'''
