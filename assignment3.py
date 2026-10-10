from math import exp

def function(x):
    return exp(-x**2)

def composite_trapezoidal(f, interval, n):
    h = (interval[1] - interval[0]) / n
    S = f(interval[1]) + f(interval[0])

    for i in range(1, n):
        x = interval[0] + i*h
        S = S + 2*f(x)

    I = (h/2)*S
    return I

def composite_simpson(f, interval, n):
    h = (interval[1] - interval[0]) / n
    x0 = interval[0]
    I = f(x0)

    for i in range(1,n):
        xi = interval[0]+i*h
        if i%2!=0 :
            I = I+4*f(xi)
        else:
            I = I+2*f(xi)

    xn = interval[1]
    I = I+f(xn)
    I = I*h/3
    return I

print("Trapezoidal rule : ",composite_trapezoidal(function, (0,1), 1))
print("Composite trapezoidal rule with 4 points : ",composite_trapezoidal(function, (0,1), 4))
print("Composite trapezoidal rule with 6 points : ",composite_trapezoidal(function, (0,1), 6))
print("============")
print("Simpson rule : ",composite_simpson(function, (0,1), 2))
print("Composite simpson rule with 4 points : ",composite_simpson(function, (0,1), 4))
print("Composite simpson rule with 6 points : ",composite_simpson(function, (0,1), 6))