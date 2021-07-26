#txt = "apple#banana#cherry#orange"

#x = txt.split("#")

#print(type(x))

import json
from ast import literal_eval

with open("evan.json", 'r') as file:
    uInfo = json.load(file)
    uInfo = literal_eval(uInfo)
    name = uInfo['name']
    age = uInfo['age']
    country = uInfo['country']
    job = uInfo['job']
    print(uInfo)

length = len(uInfo)

print(length)

for key in json.loads('evan.json'):
    print(key)

with open('evan.json', 'w') as file:
    json.dump(str({"name": name, "age": age, "country": country, "job": job, "ok": "oka"}), file)