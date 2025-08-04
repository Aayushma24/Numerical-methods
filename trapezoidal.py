import math
def f(x):
    return math.cos(math.pi *x /2)+5


def trapezoidal(a,b,n):
    h = (b- a) /n
    result = (f(a) + f(b))/2
   
    for i in range(1,n):
        x = a +  i*h
        result += f(x)

    return result
a=0
b=4
n=4

solution = trapezoidal(a,b,n)
print(f"The area under the curve is {solution:.4f}")
       
    
 