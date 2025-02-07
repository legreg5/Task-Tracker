import cmd
import json
from pathlib import Path



#class
class TaskTracker(cmd.Cmd):
    """Simple command processor example."""
    
    def do_add(self, line):
        print ("hello",line)
    
    def do_update(self, line):
        print ("hello",line)
        
    def do_delete(self, line):
        print ("hello",line)
        
    def do_list(self, line):
        print ("hello",line)

    def do_(self, line):
        return True
    

# create dictionary
task_details ={ 
    "id" : 0, 
    "name" : "test1", 
    "status" : False, 
    } 

# create 

#create json 
def createjson(myDictionary):
    # Convert and write JSON object to file
    with open("tasks.json", "w") as outfile: 
        json.dump(myDictionary, outfile)

#check if json file exist
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

#create json if file path does not exist 
def checkOrCreateJsonfile():
    if jsonExist():
        print('raoul')
    else:
        createjson(task_details)

#create dictionary function
def addTodictionary(dictionary,id,name,status):
    new_dictionary = dict(old_dictionary, key=value)







checkOrCreateJsonfile()
# creat a task dictionary
    #determine the attributes of a task
# covert dictionary to JSON
    #structure 
# create a function that can look what the last id is and asign a new id +1 
# create json file 
# write to the json file 
# save json file 
# read json file 
# update json file 
# delete record jason file  
# add the json file to 




# # Open the JSON file
# with open('tasks.json') as f:
#     data = json.load(f,parse_int=True)

# # data.pop('1')
# # data.update({'1':'tasks1'})

# print(data)


    
# if isinstance(data, (list)):
#     print("yes")

# Print the data (it will be stored as a Python dictionary)
# pprint.pp(data)


app = TaskTracker()

app.onecmd("add Alice")






#001 INITIATE DATA function
    #this function will check if json exist in directory
        #give path of directory 
        #if json exist in directory  #001a
            #read in json
            #conver json to list of dictionars
            #return list with dictionaries
        #else #001b
            #create json file in directory
            #create placeholder list
            #save data function (placeholder list) #002
            #return empty list 


#002 SAVE DATA function(list with dictionaries)
#covert list to json
#save json file in directory


#003 GET ID FUNCTION(id )
#list of dictionaries = #initiate() #001a or #001b
#if list of dictionarie[id] #003a
    # return list of dictionary id
#else
    # create empty dictionary #003b
    # print task with id not found  
    # return empty 
    

# https://www.geeksforgeeks.org/args-kwargs-python/   
#004 UPDATE DATA FUNCTION 
#update tasks (id,**updates)
    #updatetaskdictionary = list with dictionaries[id]
    #for keys in updates.key:
        updatetaskdictionary
        
        
#101
#ADD TASK(taskname)
#task status = not started
#create dictionary {id,description,status}
#initiate data #001
#create date "created date"
#create date "modified date"
#add tasks (id,description,status,createdAt,updatedAt)
#save task info in a list of dictionary
#save data #002 


#102
#UPDATE TASK NAME (id)
#initiate data #001
#get id 
#search task#003 
#update name 
#update "modified date"
#Save data function #002

#103
#UPDATE TASK PROGRESS TO IN PROGRESS(id)
#initiate data #001
#get id 
#search task#003 
#update task 
#update "modified date"
#Save data function #002

#104
#UPDATE TASK PROGRESS TO DONE (id)
#initiate data #001
#get id 
#search task#003 
#update task 
#update "modified date"
#Save data function #002

#104
#DELETE TASK
#initiate data #001
#get id 
#search task#003 
#update task 
#update "modified date"
#Save data function #002

#105
#show all tasks
#initiate data #001
#print (list with dictionaries)


#LIST TASK
#check if json exist 
    #create json / skipp
#read in json
#conver json to list of dictionars



