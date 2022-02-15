
def star(row):
    for ele in range(0,row+1):
        for i in range(ele):
            print("*",end = ' ')
        print()
star(5)