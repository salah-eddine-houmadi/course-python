#problem

num = 1

if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")

#problem

text = "Score: 36"

if not text:
	print("Empty String")
else:
	for char in text.lower():
		if char in ("a", "e", "i", "o", "u"):
			print(f"{char} is a vowel")
		elif not char.isalpha():
			print(f"{char} is not a letter")
		else:
			print(f"{char} is a consonant")
			
#problem

a = 1
b = 3
c = 4

if (a>=b) and (a>=c):
	print(a)
elif b >= a and b >= c:
	print(b)
else:
	print(c)
	
#problema 
a = 1
b = 3
c = 4

if (a<=b) and (a<=c):
	print(a)
elif (b <= a) and (b <= c):
	print(b)
else:
	print(c)
	
#problema 

season_num = 2

if season_num == 1:
	print("Spring")
elif season_num == 2:
	print("Summer")
elif season_num == 3:
	print("Fall")
elif season_num == 4:
	print("Winter")
else:
	print("Please enter a valid number")
	
#problema 

a = 1
b = 2
c = 1

if (a == b) and (b==c):
	print("Equal")
else:
	print("Not Equal")