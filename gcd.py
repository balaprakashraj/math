def gcd(a,b):
    t=min(a,b)
    while True:
      
        if a%t==b%t==0:

            return t
            break
        else:
            t=t-1
        
print(gcd(10,15))
