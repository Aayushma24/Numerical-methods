def linear_regression(x,y):
    n=len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i]*y[i] for i in range(n))
    sum_x2 = sum(x[i]*x[i] for i in range(n))
    b = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    a = (sum_y - b*sum_x) / n
    return a,b

x_values = [1,2,3,4,5]
y_values = [2,4,5,4,5]

a,b = linear_regression(x_values,y_values)
print(f"Regression Line y={a:.2f}+ {b:.2f}x")

x_input = 6
y_predict = a + b * x_input
print(f"Predicted value of y at x = {x_input} is {y_predict:.2f} ")

