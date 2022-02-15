def my_func():
    yield 1            
    yield 2            
    yield 3            

for value in my_func(): 
    print(value)