# age = 32

# if(age>18):
#     print("you can drive")

age = int(input("Enter your age :"))

if(age>18):
    print("You can drive")
elif(age == 18):
    print("lets schedule an interview")
elif(age == 0):
    print("hey you are just born")
else:
    print("You cannot drive")

print("End of program")