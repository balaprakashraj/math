def equ(a,b,c,r):
    if type(a) is str:
        return a,r-(b+c)
    elif type(b)is str:
        return b,r-(a+c)
    elif type(c) is str:
        return c,r-(b+a)
    else:
        return r,a+b+c
print(equ(1,3,'v',6))
print(equ(1,'x',2,6))
print(equ('y',3,2,6))
print(equ(1,3,2,'r'))
