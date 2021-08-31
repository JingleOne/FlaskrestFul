""""Build a Restful API using a Python web framework i.e. Flask or Django. It
should allow a client to create a Todo Note, add Todos to a note, complete Todos for a note, list
all Todos and delete both Todos and Notes."""

import os
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
try:
    os.mkdir(os.getcwd()+'/db')
except FileExistsError:
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:////{os.getcwd()}/db/noteDatabase.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
noteDb = SQLAlchemy(app)


class NoteModel(noteDb.Model):
    noteID = noteDb.Column(noteDb.Integer, primary_key=True)
    noteName = noteDb.Column(noteDb.String(100), nullable=False)

    def __repr__(self):
        return f"NoteDB task = {noteName}"


noteDb.create_all()


note_putPatch_args = reqparse.RequestParser()
note_putPatch_args.add_argument(
    "noteID", type=int, help="Note id number is required", required=True)
note_putPatch_args.add_argument(
    "noteName", type=str, help="Note name field is required",  required=True)

note_get_args = reqparse.RequestParser()
note_get_args.add_argument("noteID", type=int, help="Note id number")

# note_patch_args = reqparse.RequestParser()
# note_patch_args.add_argument(
#     "noteID", type=int, help="Note id number is required", required=True)
# note_patch_args.add_argument(
#     "noteName", type=str, help="Note name field is required", required=True)

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
            match = NoteModel.query.get(args["noteID"])
            return match
        else:
            return NoteModel.query.all()

    @marshal_with(noteResourceField)
    def put(self):
        args = note_putPatch_args.parse_args()
        matched = NoteModel.query.get(args["noteID"])
        if matched:
            abort(409, message="Note ID taken")
        note = NoteModel(noteID=args["noteID"], noteName=args["noteName"])
        noteDb.session.add(note)
        noteDb.session.commit()
        return note, 201

    @marshal_with(noteResourceField)
    def patch(self):
        args = note_putPatch_args.parse_args()
        matched = NoteModel.query.get(args["noteID"])
        if not matched:
            abort(409, message="Note ID not found")
        matched.noteName = args["noteName"]
        noteDb.session.commit()
        return matched, 200

        # return {args["noteID"]: data[args["noteID"]]}

    @marshal_with(noteResourceField)
    def delete(self):
        args = note_delete_args.parse_args()
        matched = NoteModel.query.get(args["noteID"])
        if not matched:
            abort(409, message="Note ID not found")
        noteDb.session.delete(matched)
        noteDb.session.commit()
        return matched, 200


#todoData = {1: "buy milk", 2: "fix bank acc", 3: "assemble PC"}
# note_put_args.add_argument("todoID", type=int, help="Todo id number")
# note_put_args.add_argument("task", type=str, help="task for that todoID")


api.add_resource(Notes, "/Note")

if __name__ == "__main__":
    app.run(debug=True)
