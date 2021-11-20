import json
d={"name": "David","class":"I","age": 6 }
print(type(d))
pytojson=json.dumps(d)
print(pytojson)
print(type(pytojson))

