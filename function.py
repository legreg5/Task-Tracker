import cmd
import json
from pathlib import Path

#000 JSONFILE

#001 create json if file path does not exist 
def checkOrCreateJsonfile():
    if jsonExist(): # R:002
        print('raoul')
    else:
        createjson(task_details)

#002 check if json file exist
def jsonExist():
    # Create a path object
    path = Path('tasks.json')

    #check if path exist
    if path.exists():
        print("Path exists")
        return True
    else:
        print("Path does not exist")
        return False

#002 create json 
def createjson(myDictionary):
    # Convert and write JSON object to file
    with open("tasks.json", "w") as outfile: 
        json.dump(myDictionary, outfile)








# create dictionary
task_details ={ 
    "id" : 0, 
    "name" : "test1", 
    "status" : False, 
    } 

# create listofdictionary








#create dictionary function
def addTodictionary(dictionary,id,name,status):
    new_dictionary = dict(old_dictionary, key=value)

