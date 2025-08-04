import math
def f(x):
    return math.cos((math.pi*x)/2) + 5
def simpson_third(a,b,n):
    h= (b-a) / n
    result = f(a)+ f(b)
    
    for i in range(1,n):
        x = a + i*h
        if i%2==0:
            result+=f(x)*2
        else:
            result+=f(x)*4
    result*=(h/3)
    return result
   
a=0
b=4
n=8

solution = simpson_third(a,b,n)
print(f"Value of Simpson is {solution:.4f}")

    
