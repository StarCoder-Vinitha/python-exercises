def s(name):
    l= name.maketrans('s','c')
    s = name.translate(l)
    return s
name='python'
print(s(name))