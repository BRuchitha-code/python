def squ():
    print("enter the side of square")
def rec(l,b):
    print("area of rec is:",l*b)
def circle():
    print("enter the raidus:")
    return 3.1*r*r
def tri(a,b):
    area=0.5*a*b
    print("area of triangle",area)


while(1):
    print("menu")
    print("square")
    print("rec")
    print("circle")
    print("tri")
    d=int(input("enter yor choice:"))
    if d==1:
        squ()
    elif d==2:
        l=int(input("enter the len of rec"))
        b=int(input("enter the breadth of rec"))
        rec(l,b)
    elif d==3:
        x=cir()
        print("radius of circle")
    elif d==4:
        b=int(input("enter the base of tri"))
        h=int(input("enetr the height of tri"))
        tri(b,h)
    elif d==5:
        print("exiting program")
    else:
        print("invalid choice")
        
        