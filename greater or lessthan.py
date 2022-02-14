def sample(x,y,z):
    if x>=0 and y>=0:
        print(x)
    elif x<0 and z>0:
        print(y)
    elif y<=0 and z>=0:
        print(y)
    else:
        pass
sample(1,4,2)