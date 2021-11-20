d= {
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
import json
max=0
d1={}
d2={}
for k in d:
    d1[int(k)]=d[k]
for i in d1:
    if i>max:
        max=i
        val=d1[i]
for j in range(max+1):
    if j in d1:
        d2[str(j)]=d1[j]
pytojson=json.dumps(d2)
print(pytojson)
print(type(pytojson))









