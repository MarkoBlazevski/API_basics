#Delete Resource
#Use DELETE method of API

# To make a request to the server and to get response to the server we NEED requests module
import requests

# API URL
url = "https://reqres.in/api/users/2"

#To delete user or something
requests.delete(url)

#Add response to a variable
response = requests.delete(url)

#To Fetch response code
print(response.status_code)

#For validation we need to check our status_code ASSERT is the way to do that

assert response.status_code == 204