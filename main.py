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

db.create_all()

class Todo(db.Model):
    todoID = db.Column(db.Integer, primary_key=True)
    todoNoteID = db.Column(db.Integer, db.ForeignKey('note.noteID'),
        nullable=False)
    todoTask = db.Column(db.String(200), nullable=False)

db.create_all()




note_putPatch_args = reqparse.RequestParser()
note_putPatch_args.add_argument(
    "noteID", type=int, help=" id number is required", required=True)
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


class Notes(Resource):

    @marshal_with(noteResourceField)
    def get(self):
        args = note_get_args.parse_args()
        print("[DEBUGGINGGGGGGGG]", args)
        if args["noteID"]:
            match = Note.query.get(args["noteID"])
            return match
        else:
            return Note.query.all()

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

        # return {args["noteID"]: data[args["noteID"]]}

    @marshal_with(noteResourceField)
    def delete(self):
        args = note_delete_args.parse_args()
        matched = Note.query.get(args["noteID"])
        if not matched:
            abort(409, message="Note ID not found")
        db.session.delete(matched)
        db.session.commit()
        return matched, 200

class Todos(Resource):
    pass


#todoData = {1: "buy milk", 2: "fix bank acc", 3: "assemble PC"}
# note_put_args.add_argument("todoID", type=int, help="Todo id number")
# note_put_args.add_argument("task", type=str, help="task for that todoID")


api.add_resource(Notes, "/Note")

if __name__ == "__main__":
    app.run(debug=True)
