#GET Request
#PICK Response
#DISPLAY Response

# To make a request to the server and to get response to the server we NEED requests module
import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

#To make request we are going to use
reqests.get(url)

#We get some response so we are going to put that response into the variable
response = reqests.get(url)

#Now we print what we got
print(response)

#Display Response Content
print(response.content)

#Display Header of the Response
print(response.headers)

#Parse Response to Json format ro that we NEED json module
json.loads(response.text)

#Now we put that into the variable
json_response = json.loads(respose.text)

#Response in the form of JSON
print(json_response)

#Now if we want to access to a specific value in our response in JSON we NEED jsonpath module
jsonpath.jsonpath(json_response,"total_pages") #<==In this case our value is 'total_pages'

#I am going to store value that we get into the variable
pages = jsonpath.jsonpath(json_response,"total_pages") #<==We get our response in form of a list in this case we got just one value
print(pages[0]) #<==We are printing first value in our list

#If we want to check our response ASSERT is the way to do that
assert pages[0] == 4 #<==If we put wrong value we are going to get AssertionError(we are comparing actual result with expected result)