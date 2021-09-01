<h1>Restful Note API</h1>

In this repo, I used python flask to build a simple todo list web API that can be tested using tools like postman. The main.py contains the implementation of the server side API methods, and the client.py is a test file for the main.py. It also provides some details as to how to use this API.

There are two endpoints, /Note and /Todo/todo_id 
ex: http://127.0.0.1:5000/Note and http://127.0.0.1:5000/Todo/1

I choose to include the todo_id as part of the endpoint because every CRUD operation on the todo database needs todo_id. 

todo_id is an integer that is unique for every todo

For the /Note endpoint, users can use 
the get request to list  all the todos in every note 
the put and patch requests with {"noteID":integer, "noteName":String} as data parameter to make a new note and update an existing note
the delete request with {"noteID": integer} as data to delete an existing note. All the todos within that note will also be deleted as well

For the /Todo/todo_id, users can use 
the get request will return the todo with the todo_id
the pull request with {"todoTask":String,"todoNoteID":Integer} as data parameter to make a new todo in an existing note. The todoNoteId is a foreign key in the Note database.
the patch request with  {"todoTask":String} as data parameter to update an existing todo. The todoTask will be updated(todo description). 
the delete request will remove the todo with the provided todo_id in the database.



 
