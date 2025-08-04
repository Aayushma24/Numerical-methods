import math
def f(x):
    return math.cos((math.pi*x)/2) + 5
def simpson_third_eigth(a,b,n):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 Rule.")
    h= (b-a) / n
    result = f(a)+ f(b)
    
    for i in range(1,n):
        x = a + i*h
        if i%3==0:
            result+=f(x)*2
        else:
            result+=f(x)*3
    result*=(3*h/8)
    return result
   
a=0
b=4
n=6

solution = simpson_third_eigth(a,b,n)
print(f"Value of Simpson_third_eighth is {solution:.0f}")

    
