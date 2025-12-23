#Get  the environment from user and print it

env = input("Please enter the environment (dev/stg/prod): ") #input() - to take input from user
for i in range(5):
    print("The user input Environment is:", env)

    #conditional statements - if, elif, else
    if env == "prod":
        print("Don't Deploy on Friday") #best practice of production
    elif env == "stg":
        print("Take Backup and Test well") #best practice of stagging
    else:
        print("Safe to deploy on any day")

# = - assignment operator
# == - comparison operator  

a = input("Enter your number 1: ")
b = int(input("Enter your number 2:")) #int()- type casting - changing data type
c = int(input("Enter your number 3:")) 

print(type(a)) #string
print(type(b)) #integer
print("Addition of a & b is:", int(a) + b) #type casting
print("Multiplication of b & c is:", b * c)
print("Subtraction of b & c is:", b - c)
print("Division of b & c is:", b/ c) #float
print("Floor Division of b & c is:", b // c) #integer
print("Modulus of b & c is:", b % c) #remainder

