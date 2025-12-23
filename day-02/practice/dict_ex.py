
#dictionary- collection of key-value pairs


info = {
    "name" : "Bhoomi", #string
    "city" : "India", 
    "qualification": "B.Tech",
    "birth_date": 23,     #int
    "married": False, # Boolean
    "favourites" : ["teaching", "movies", 18]
}

print("I live in",info["city"])
print("I love ", info.get("favourite","Not Found")) 

info.update({"certifications": "AWS 2X"})

# print(dir(info))

for key,value in info.items(): 
    print(key,value)