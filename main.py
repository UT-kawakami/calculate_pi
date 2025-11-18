import numpy as np

# 長方形近似
def Rectangle(N):
    x = np.arange(N) / N
    y = np.sqrt(1 - x**2)
    pi = 4 * np.sum(y) / N
    return pi

# 台形近似
def Trapezoid(N):
    x = np.linspace(0, 1, N+1)
    y = np.sqrt(1 - x**2)
    h = 1 / N
    integral = (h/2) * (y[0] + 2*np.sum(y[1:N]) + y[N])
    return 4 * integral

if __name__ == "__main__":
    print("Rectangle(100)     =", Rectangle(100))
    print("Rectangle(1000)    =", Rectangle(1000))
    print("Rectangle(10000)   =", Rectangle(10000))
    print("Rectangle(100000)  =", Rectangle(100000))
    print("Rectangle(1000000) =", Rectangle(1000000))

    print("Trapezoid(100)     =", Trapezoid(100))
    print("Trapezoid(1000)    =", Trapezoid(1000))
    print("Trapezoid(10000)   =", Trapezoid(10000))
    print("Trapezoid(100000)  =", Trapezoid(100000))
    print("Trapezoid(1000000) =", Trapezoid(1000000))
