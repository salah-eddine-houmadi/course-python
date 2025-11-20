#problem
my_dict = {
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 }

freq_dict = {}

for value in my_dict.values():
	if value in freq_dict:
		freq_dict[value] += 1
	else:
		freq_dict[value] = 1

print(freq_dict)

#problem

my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

new_dict = {}

for nested_list in my_list:
	key = nested_list[0] 
	value = nested_list[1]
	new_dict[key] = value

print(new_dict)

#problem

my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}

max_sum = None

for list_value in my_dict.values():
	list_sum = sum(list_value)

	if max_sum is None:
		max_sum = list_sum
	elif max_sum < list_sum:
		max_sum = list_sum

print(max_sum)

#problem
my_string = "Hello, World"

freq_dict = {}

for char in my_string.lower():
	if char.isalpha():
		if char in freq_dict:
			freq_dict[char] += 1
		else:
			freq_dict[char] = 1

print(freq_dict)

#problem
my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}

for list_value in my_dict.values():
	list_value.sort()

print(my_dict)

#problem

product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}

new_list = []

for key, value in product_info.items():
	new_list.append([key, value])

print(new_list)

