def interpolation(x_values,y_values,x):
    n=len(x_values)
    result=0
    for i in range(n):
        f=y_values[i]
        for j in range(n):
            if i!=j:
                f*=(x-x_values[j]) / (x_values[i]-x_values[j])
        result+=f
    return result
x_points=[]
y_points=[]
n=int(input("Enter the value of x/y points"))
for i in range(n):
    element1=float(input(f"Enter the {i+1} values of x"))
    x_points.append(element1)
for j in range(n):
    element2=float(input(f"Enter the {i+1} values of y")) 
    y_points.append(element2) 

x_to_determined=float(input("Enter the value of x for which y to be determined"))
solution=interpolation(x_points,y_points,x_to_determined)
print(f"The solution at x = {x_to_determined} using Lagrange interoplation is{solution:.4f} ")
    
    
    



    
     
    
    