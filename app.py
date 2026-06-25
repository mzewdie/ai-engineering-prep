import requests

print("requests imported successfully")


response = requests.get(
    "https://api.github.com/users/octocat"
)



print("Status:", response.status_code)

data = response.json()

print(f"The resonse as a json is: {data}")

print("Name:", data["name"])
print("E-Mail:",data["email"])
print("Location:", data["location"])
print("ID: ",data["id"])
print("Followers:", data["followers"])
print("Public repos:", data["public_repos"]) 


#import sys

#print(sys.executable)  

#print("Hello from VS Code")