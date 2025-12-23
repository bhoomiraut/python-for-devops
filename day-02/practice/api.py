import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1" # server URL (API)

response = requests.get(url=api_url) #url= parameter

print(dir(response))
print(response.status_code)

for key,value in response.json().items():
    if key == "userId":
        if value in [1,2,3]:
            print("User found") 
        else:
            print("User not found")

#for key, value in response.json().items():
#    if key == "completed":
#        if value == False:
#            print("The data is not completed in server")