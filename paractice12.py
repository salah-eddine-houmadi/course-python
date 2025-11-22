#problem 

def find_gcd(a,b):
    if b == 0:
        return a 
    else :
        return find_gcd(b, a % b)

print(find_gcd(1,2))

#problem 

def is_palindrome(string):
	string = string.lower()
	if len(string) <= 1:
		return True
	elif string[0] != string[-1]:
		return False
	else:
		return is_palindrome(string[1:-1])
	
print(is_palindrome("Amazing"))

#problem 

def print_pattern(n):
	if n == 1:
		print("*")
	else:
		print("*" * n)
		print_pattern(n-1)	
    

print(print_pattern(4))

#problem 

def convert_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    else:
        return (convert_to_binary(decimal_num // 2) + str(decimal_num % 2)).lstrip("0")


print(convert_to_binary(5))

#problem 

def binary_search(seq, low, high, elem):
	if low > high:
		return -1
	else:
		middle = (low + high)//2

		if elem == seq[middle]:
			return middle
		elif elem < seq[middle]:
			return binary_search(seq, low, middle-1, elem)
		else:
			return binary_search(seq, middle+1, high, elem)
		
my_list = [1,2,3,4]

print(binary_search(my_list,0, len(my_list),0))