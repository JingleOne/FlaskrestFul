import requests

'''for get requests, don't use data=
    for path requests, use data ='''

BASE = "http://127.0.0.1:5000"


print("adding grocery note")
response = requests.put(
    BASE + "/Note", data={"noteID": 1, "noteName": "grocery"})
print(response.json())
input()

print("adding target note")
response = requests.put(
    BASE + "/Note", data={"noteID": 2, "noteName": "Target"})
print(response.json())
input()

print("adding school note")
response = requests.put(
    BASE + "/Note", data={"noteID": 3, "noteName": "school"})
print(response.json())
input()

print("updating school note to play note")
response = requests.patch(
    BASE + "/Note", data={"noteID": 3, "noteName": "play"})
print(response.json())
input()

print("adding todo1 buy milk to note1")
response = requests.put(
    BASE + "/Todo/1", data={"todoTask": "buy milk", "todoNoteID": 1})
print(response.json())
input()

print("adding todo2 buy juice to note1")
response = requests.put(
    BASE + "/Todo/2", data={"todoTask": "buy juice", "todoNoteID": 1})
print(response.json())
input()

print("adding todo3 buy gift card to note2")
response = requests.put(
    BASE + "/Todo/3", data={"todoTask": "buy gift card", "todoNoteID": 2})
print(response.json())
input()

print("adding todo4 study to note3")
response = requests.put(
    BASE + "/Todo/4", data={"todoTask": "study", "todoNoteID": 3})
print(response.json())
input()

print("printing out current DB state")
response = requests.get(BASE + "/Note")
print(response.json())
input()

print("update todo4 study to play games")
response = requests.patch(
    BASE + "/Todo/4", data={"todoTask": "done studying play some games"})
print(response.json())
input()

print("printing out current DB state")
response = requests.get(BASE + "/Note")
print(response.json())
input()

print("delete todo 1 buy milk ")
response = requests.delete(
    BASE + "/Todo/1")
print(response.json())
input()

print("printing out current DB state")
response = requests.get(BASE + "/Note")
print(response.json())
input()

print("delete NOTE 1 with all the todos inside it")
response = requests.delete(
    BASE + "/Note", data={"noteID": 1})
print(response.json())
input()

print("printing out current DB state")
response = requests.get(BASE + "/Note")
print(response.json())
input()
