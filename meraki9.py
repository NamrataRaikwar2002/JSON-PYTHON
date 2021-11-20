import json
shopping={
    "shopping_list":
        { 
            "c":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
item=input("which item you want to buy? ")
quantity=int(input("how many item you want? "))
for i in shopping:
    for j in shopping[i]:
        if j==item:
            q=int(shopping[i][j])-quantity
            shopping[i][j]=str(q)
else:
    if item not in shopping[i]:
        print(item,"not in list")
with open("meraki9.json","w+") as f:
    json.dump(shopping,f,indent=4)
