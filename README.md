<h1>Restful Note API<h1>

In this repo, I used python flask to build a simple todo list web API that can be tested using tools like postman

There are two endpoints, 
/Note and /Todo/todo_id 

todo_id is an integer that is unique for every todo

For the /Note endpoint, users can use 
the get request to list  all the todos in every note 
the put and patch requests with {"noteID":integer, "noteName":String} as data parameter to make a new note and update an existing note
the delete request with {"noteID": integer} as data to delete an existing note. All the todos within that note will also be deleted as well




 
