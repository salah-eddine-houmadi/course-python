#problem
listA = [1,2,3,4]
listB = [1,2]

difference = []

for elem in listA:
    if elem not in listB:
        difference.append(elem)
    
print(difference)

#problem
pointA = [3, 4, 5]
pointB = [1, 3, 5]

distance = (
    (pointA[0] - pointB[0]) ** 2 +
    (pointA[1] - pointB[1]) ** 2 +
    (pointA[2] - pointB[2]) ** 2
) ** (1/2)

print(distance)

#problem
listA = [1,4,5]
listB = [3,4,5]

common_elem = []

for elem in listA:
    if elem in listB:
        common_elem.append(elem)

print(common_elem)

#problem
my_list = [1,2,3,4]
if len(my_list) > 1:
    sorted_list = sorted(my_list)
    print(sorted_list[-2])
else:
    print(None)

#problem
my_list = [1,2,3,4]
if len(my_list) > 1:
    sorted_list = sorted(my_list)
    print(sorted_list[1])
else:
    print(None)

#problem

my_list = ["a","a","b","c","a","b"]

freq_dict = {}

for elem in my_list:
    if elem not in freq_dict:
        freq_dict[elem] = 1
    else:
        freq_dict[elem] += 1

print(freq_dict)

#problem

my_list = [[1,2,3], [4,5,6],[7,8,9]]
flat_list = []

for elem in my_list:
    if isinstance(elem, list):
        for nested_elem in elem:
            flat_list.append(nested_elem)
    else:
        flat_list.append(elem)

print(flat_list)

#problem

import itertools 

my_list = [1, 2, 3]
permutations = list(itertools.permutations(my_list))

for permutation in permutations:
    print(permutation)