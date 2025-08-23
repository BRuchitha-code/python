import random
no=int(input("enter the number of teams:"))
teams=[]
for i in range(no):
    d=input("enter the team name:")
    teams.append(d)
meet=int(input("enter the no of meetings b\w two teams"))
matches=[]
for i in range(no-1):
    for j in range(i+1,no):
        for k in range(meet):
            matches.append([teams[i],teams[j]])
random.shuffle(matches)
for i in range(len(matches)):
    print("match {} : {} vs {}".format(i+1,matches[i][0],matches[i][1]))
        
    