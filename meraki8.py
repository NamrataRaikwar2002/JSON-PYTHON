import json

a=[["neelam","programer","24","2400",],[
    'komal',"trainer","24","20000"],["anuradha","HR","25","40000"],["Abhishek","manager","29","63000"] ]
b=["name","designation","age","salary"]
c=["emp1","emp2","emp3","emp4"]
d={}
l=[]
for i in range(len(a)):
    for j in  range(i+1):
        for i in range(i+1):
            for m in range(i+1):
                d[c[i]]={b[j]:a[i][j] for j in range(len(a))}
f=json.dumps(d)
print(type(f))
with open ("meraki8.json","w+") as file1:
    json.dump(d,file1,indent=4)




    
    

    

