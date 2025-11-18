import numpy as np

# 台形近似でπを求める関数
def Trapezoid(N):
    x = np.linspace(0, 1, N+1)  # 0 〜 1 を N 等分 (N+1 点)
    y = np.sqrt(1 - x**2)
    
    # 台形公式: (h/2) * (f0 + 2*sum(f1...fN-1) + fN)
    h = 1 / N
    integral = (h / 2) * (y[0] + 2*np.sum(y[1:N]) + y[N])
    
    pi = 4 * integral
    return pi

# 出力
print("Trapezoid(100)     =", Trapezoid(100))
print("Trapezoid(1000)    =", Trapezoid(1000))
print("Trapezoid(10000)   =", Trapezoid(10000))
print("Trapezoid(100000)  =", Trapezoid(100000))
print("Trapezoid(1000000) =", Trapezoid(1000000))
