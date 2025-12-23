for i in range(5): # Loop from 0 to 4
    print("Iteration:", i  ) # Print the current iteration number

num = int(input("Enter a number to print its table: ")) # Get user input for the number
for i in range(1, 11): # Loop from 1 to 10
    print(f"{num} x {i} = {num * i}") 

# string formatting "f" is used to embed expressions inside string literals.

name = input("Hey! Enter your name: ") 
print(f"Hello {name}, Let's learn python together!") #f - difference between "" and f"" is f allows embedding expressions

#suraj = "chand"
#while suraj == "chand": #while - jab tak condition true hai tab tak chalega
    #print("chand")    #without break statement it will be infinite loop
   # break     #to avoid infinite loop or exit condition


choice = input("Enter the choice (press q to quit):")

while choice!= "q": #loop will continue until user enters 'q'
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    choice = input("Enter the number for a table printing or q to quit: ")
print("You have exited the loop. Thank You!")
    