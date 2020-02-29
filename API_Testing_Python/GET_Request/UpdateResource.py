#PUT---we are using put for updating resources to the server
#Our base modules are..
import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users/2"


#STEPS

#We need to open request body from API URL(under the PUT request that we want to made a change,is body form)

#When we find it we are going to copy it and paste the form into notepad++ or some other text editor

#Then we make a change put .json(with that we made a json file) and save it

#Read input from json file
file = open("path of the JSON file that we fill with updates", "r") #<== r is READ mode

#To read complete content of file
file.read()
json_input = file.read()#This content is simply a string for us so we need to put it into JSON format

#To PARSE data into JSON format we need to do following...
request_json = json.loads(json_input)

#For checking just print it
#print(request_json)

#Sending with PUT request to the server(PUT request with json input body)
requests.put(url, request_json) #<==My data is request_json variable(our request body in the form of JSON file)

#Our response object we are going put in variable
response = requests.put(url, request_json)

#To validate response code
assert response.status_code == 201

#PARSE response content
response_json = json.loads(response.text)

#For fetching content we are using Json Path
jsonpath.jsonpath(response_json, 'updated content')#<==It will return list(always return a list)

updated = jsonpath.jsonpath(response_json, 'updated content')
print(updated[0])
