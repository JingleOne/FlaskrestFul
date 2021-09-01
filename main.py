""""Build a Restful API using a Python web framework i.e. Flask or Django. It
should allow a client to create a Todo Note, add Todos to a note, complete Todos for a note, list
all Todos and delete both Todos and Notes."""

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///noteDatabase.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Note(db.Model):
    noteID = db.Column(db.Integer, primary_key=True)
    noteName = db.Column(db.String(100), nullable=False)
    todoList = db.relationship('Todo', backref='note', lazy=True)


class Todo(db.Model):
    todoID = db.Column(db.Integer, primary_key=True)
    todoNoteID = db.Column(db.Integer, db.ForeignKey('note.noteID'),
        nullable=False)
    todoTask = db.Column(db.String(200), nullable=False)

db.create_all()


note_putPatch_args = reqparse.RequestParser()
note_putPatch_args.add_argument(
    "noteID", type=int, help="Note id number is required", required=True)
note_putPatch_args.add_argument(
    "noteName", type=str, help="Note name field is required",  required=True)

note_get_args = reqparse.RequestParser()
note_get_args.add_argument("noteID", type=int, help="Note id number")

note_delete_args = reqparse.RequestParser()
note_delete_args.add_argument(
    "noteID", type=int, help="Note id number is required", required=True)

noteResourceField = {
    "noteID": fields.Integer,
    "noteName": fields.String
}

todoResourceField = {
    'todoID': fields.Integer,
    'todoNoteID':fields.Integer,
    'todoTask': fields.String
}



class Notes(Resource):

    @marshal_with(todoResourceField)
    def get(self):
        allTodos = list()
        for note in Note.query.all():
            allTodos.extend(Todo.query.filter_by(todoNoteID = note.noteID).all())
        return allTodos

    @marshal_with(noteResourceField)
    def put(self):
        args = note_putPatch_args.parse_args()
        matched = Note.query.get(args["noteID"])
        if matched:
            abort(409, message="Note ID taken")
        note = Note(noteID=args["noteID"], noteName=args["noteName"])
        db.session.add(note)
        db.session.commit()
        return note, 201

    @marshal_with(noteResourceField)
    def patch(self):
        args = note_putPatch_args.parse_args()
        matched = Note.query.get(args["noteID"])
        if not matched:
            abort(409, message="Note ID not found")
        matched.noteName = args["noteName"]
        db.session.commit()
        return matched, 200

    @marshal_with(noteResourceField)
    def delete(self):
        args = note_delete_args.parse_args()
        matched = Note.query.get(args["noteID"])
        if not matched:
            abort(409, message="Note ID not found")
        for todo in Todo.query.filter_by(todoNoteID = matched.noteID).all():
            db.session.delete(todo)
        db.session.delete(matched)
        db.session.commit()
        return matched, 200

todo_put_args = reqparse.RequestParser()
todo_put_args.add_argument(
    "todoTask", type=str, help="Note name field is required",  required=True)
todo_put_args.add_argument(
    "todoNoteID", type=int, help="Note ID field is required",  required=True)

todo_patch_args = reqparse.RequestParser()
todo_patch_args.add_argument(
    "todoTask", type=str, help="Note name field is required",  required=True)




class Todos(Resource):

    @marshal_with(todoResourceField)
    def get(self, todo_id):
        match = Todo.query.get(todo_id)
        if not match:
            abort(404,message="Todo not found")
        return match

    @marshal_with(todoResourceField)
    def put(self, todo_id):
        args = todo_put_args.parse_args()
        match = Todo.query.get(todo_id)
        if match:
            abort(400,message="Todo ID taken")
        noteMatch = Note.query.get(args["todoNoteID"])
        if not noteMatch:
            abort(404, message="Note ID not found")
        todo = Todo(todoNoteID=args["todoNoteID"], todoID=todo_id, todoTask=args["todoTask"])
        db.session.add(todo)
        db.session.commit()
        return todo, 201
    
    @marshal_with(todoResourceField)
    def patch(self, todo_id):
        args = todo_patch_args.parse_args()
        match = Todo.query.get(todo_id)
        if not match:
            abort(404,message="Todo ID not found")
        match.todoTask = args["todoTask"]
        db.session.commit()
        return match, 200
        

    @marshal_with(todoResourceField)
    def delete(self, todo_id):
        match = Todo.query.get(todo_id)
        if not match:
            abort(404,message="Todo ID not found")
        db.session.delete(match)
        db.session.commit()
        return match, 200



api.add_resource(Notes, "/Note")
api.add_resource(Todos, "/Todo/<int:todo_id>")

if __name__ == "__main__":
    app.run()
