"""SUM OF LIST AND AVERAGE OF MARKS:"""
"""a=["A","B","C","D"]
b=[[23,12,56,78],[78,43,98,42],[45,88,99,55]]
per=[]
for i in b:
    d=sum(i)//4
    per.append(d)
for i in range(3):
    print("{}.{}:{}%".format(i+1,a[i],per[i]))"""

"""STUDENT NAME WHOSE AREEAR IS 0 AND MARKS GREATER THAN 60"""
'''student=["anu","ani","bala","ravi","raju","jack"]
cgpa=[59,66,47,88,78,69]
arrear=[0,1,2,1,0,0]
for i in range(6):
    if arrear[i]==0 and cgpa[i] > 60:
        print(student[i])'''

"REMOVE DUPLICATES"
'''import random
list=[]
for i in range(5):
    d=random.randint(1,10)
    if d not  in list:
        list.append(d)
print(list)'''

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="       ")

        

    
