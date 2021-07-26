import json
from ast import literal_eval


filename = 'evan.json'

# JSON data:
with open(filename, 'r') as file:
    uInfo = json.load(file)
    uInfo = literal_eval(uInfo)
# python object to be appended
    y = {"name":110096}
    e = {"pins":110096}



    # appending the data
    uInfo.update(y)
    uInfo.update(e)

    # the result is a JSON string:
    a = json.dumps(uInfo)

    print(a)

    with open(filename, 'w') as file:
        json.dump(a, file)

