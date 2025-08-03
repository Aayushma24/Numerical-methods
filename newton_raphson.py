def f(x):
    return x**3+2*x**2-5
def derivative(x):
    return 3*x**2+4*x
tolerance=0.001
x0=int(input("Enter the initial guess"))
while True:
    x1=x0-f(x0)/derivative(x0)
    print(f"The output  is: {x1:.4f}")
    if(abs(x1-x0)<= tolerance):
        break
    else:
        x0=x1





