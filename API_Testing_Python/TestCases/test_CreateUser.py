#POST---we are using post to create a new resource to the server
#Our base modules are..
import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

def test_create_new_user():
    #STEPS
    #We need to open request body from API URL(under the POST request that we want to made a change,is body form)
    #When we find it we are going to copy it and paste the form into notepad++ or some other text editor
    #Then we make a change put .json(with that we made a json file) and save it
    #Read input from json file
    file = open("path of the JSON file that we make", "r") #<== r is READ mode
    #To read complete content of file
    file.read()
    json_input = file.read()#This content is simply a string for us so we need to put it into JSON format
    #To PARSE data into JSON format we need to do following...
    request_json = json.loads(json_input)
    #For checking just print it
    #print(request_json)
    #Sending with POST request to the server(POST request with json input body)
    requests.post(url, request_json) #<==My data is request_json variable(our request body in the form of JSON file)
    #Our response object we are going to put in variable
    response = requests.post(url, request_json)
    #Checking content of the response
    print(response.content)
    #To validate response code
    assert response.status_code == 201
    #Fetching header from Response
    print(response.headers)
    #If we add .get() after we are going to fetch specific header(or some other value) ...
    print(response.headers.get('Content-Length')) #<==Content-Length is our specific header
    #In response we get ID,to get that ID we ned to PARSE response to JSON format
    response_json = json.loads(response.text)
    #Picking ID using Json Path
    jsonpath.jsonpath(response_json, 'id')#<==It will return list(always return a list)
    id = jsonpath.jsonpath(response_json, 'id')
    #Fetching first item in the list
    print(id[0])


    #TO EXECUTE TEST CASE GO TO TERMINAL SET UP THE PATH ...API_Testing_Python>pytest -v TestCases HIT ENTER(-v for detail information)