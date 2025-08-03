def f(x):
    return x**3+2*x**2-5
x0=int(input("Enter the first guess"))
x1=int(input("Enter the second guess"))
E= 0.0001
if f(x0)*f(x1)<0:
    while True:

        x=(x0+x1)/2
        if(abs(f(x))<= E or abs(x1-x0)<= E):
            break
        if x<0:
            x0=x
        else:
            x1=x
        print(f"Value of x is:{x:.4f}")


