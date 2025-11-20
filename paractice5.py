#problem
my_dist = {"a":1, "b" :2 , "c":3}
key = "d"

print(key in my_dist)

#problem
my_dict = {"January": 45, "February": 56, "March": 67}

new_key = "April"
new_value = 67

if new_key not in my_dict:
	my_dict[new_key] = new_value

print(my_dict)

#problem
my_dist1 = {"a":1,"b":2, "c":3}
my_dist2 = {"c":4,"d":6, "e":8}

final_dict = my_dist1 | my_dist2

print(final_dict)

#problem

my_dist = {"a":4,"b":4,"c":4}
num_unique_values = len(set(my_dist.values()))

if num_unique_values == 0:
	print("Empty")
elif num_unique_values == 1:
	print(True)
else:
	print(False)
	
#problem
my_dict = {"a": 4, "b": 3, "c": 7}

if my_dict:
	max_value = max(set(my_dict.values()))
	print(max_value)
else:
	print(None)

#problem
my_dict = {"a": 4, "b": 3, "c": 7}

if my_dict:
	min_value = min(set(my_dict.values()))
	print(min_value)
else:
	print(None)