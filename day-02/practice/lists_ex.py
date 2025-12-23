
#list- collection of different data types ex: int, str, float, bool
#list is mutable - changable
#list is ordered - index based

a = 1 #int 
print(type(a))
#if we write a= 2 then it will override the previous value of a
#therefore we use list to store multiple values

b= [] #empty list
b.append(2) #adding value to list using append method
b.append(3.5) #adding float value
b.append("hello") #adding string value
b.append(True) #adding boolean value
print(type(b)) 
print(b) #printing entire list

c= [1, 2, 3, True, 5.6] #list banane ka 1st tareeka
c.append(0)
print(type(c))
print(c)

clouds = list() # LIST banane ka 2sra tareeka
print(type(clouds))

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append("ibm")
clouds.append("alibaba")
clouds.append("utho")
print(clouds)

print("World Leader for Cloud Service Provider is:",clouds[0]) #index - from 0
print("Indian Cloud Service Provider is:",clouds[-1]) #"-" means index starting from end

print("Length of list is:", len(clouds)) #len()- lenght of list
print(" ")
print(dir(clouds)) #dir()- to see all the methods available for list
print(" ")
print(clouds.extend.__doc__) #extend.__doc__ - to see the documentation of extend() method
print(" ")
print(clouds.append.__doc__) #append.__doc__ - to see the documentation of append() method
print(" ")
print(clouds.__doc__) #__doc__ - to see the documentation of list
print(" ")
clouds.extend(["digitalocean", "linode"]) #extend()- to add multiple values to list at once
print(clouds)

# iterate a list
for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud} Market Leader + coverd in course")
    elif cloud == "utho":
        print(f"{cloud} Indian Cloud")
    elif cloud == "azure" or cloud == "gcp":
        print(f"{cloud} DevOps - Zero To Hero Me vo bhi cover karoonga")
    else:
        print(f"{cloud} baaki nahi honge")