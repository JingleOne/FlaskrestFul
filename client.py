import requests

'''for get requests, don't use data=
    for path requests, use data ='''

BASE = "http://127.0.0.1:5000"

response = requests.put(
    BASE + "/Note", data={"noteID": 1, "noteName": "grocery"})
print(response.json())
input()
response = requests.put(
    BASE + "/Note", data={"noteID": 2, "noteName": "Target"})
print(response.json())
input()
response = requests.put(
    BASE + "/Note", data={"noteID": 3, "noteName": "school"})
print(response.json())
input()

response = requests.patch(
    BASE + "/Note", data={"noteID": 3, "noteName": "car"})
print(response.json())
input()
response = requests.delete(
    BASE + "/Note", data={"noteID": 1})
print(response.json())
input()
response = requests.get(BASE + "/Note")
print(response.json())
input()




response = requests.put(BASE + "/Todo/1",data={"todoTask": "buy milk","todoNoteID":1})
print(response.json())
input()

response = requests.get(BASE + "/Todo/1")
print(response.json())
input()

response = requests.put(BASE + "/Todo/2",data={"todoTask": "buy juice","todoNoteID":1})
print(response.json())
input()

response = requests.get(BASE + "/Todo/2")
print(response.json())
input()

response = requests.put(BASE + "/Todo/3",data={"todoTask": "buy gift card","todoNoteID":2})
print(response.json())
input()


response = requests.get(BASE + "/Note")
print(response.json())
input()



response = requests.put(BASE + "/Todo/4",data={"todoTask": "study","todoNoteID":3})
print(response.json())
input()


response = requests.patch(BASE + "/Todo/4", data={"todoTask":"game gang"})
print(response.json())
input()



response = requests.get(BASE + "/Note")
print(response.json())
input()

response = requests.delete(BASE+"/Note", data={"noteID":1})
print(response.json())
input()

response = requests.get(BASE + "/Note")
print(response.json())
input()
