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
response = requests.get(BASE + "/Note")
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


# response = requests.put(BASE + "/Note/3")
# print(response.json())
# input()
# response = requests.put(BASE + "/Note/4")
# print(response.json())
# input()
# response = requests.get(BASE + "/Note")
# print(response.json())
