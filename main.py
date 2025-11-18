import numpy as np

# -------------------------------
# 長方形近似
# -------------------------------
def Rectangle(N):
    x = np.arange(N) / N
    y = np.sqrt(1 - x**2)
    return 4 * np.sum(y) / N

# -------------------------------
# 台形近似
# -------------------------------
def Trapezoid(N):
    x = np.linspace(0, 1, N+1)
    y = np.sqrt(1 - x**2)
    h = 1 / N
    integral = (h/2) * (y[0] + 2*np.sum(y[1:N]) + y[N])
    return 4 * integral

# -------------------------------
# シンプソン則
# -------------------------------
def Simpson(N):
    if N % 2 == 1:
        raise ValueError("Simpson の公式では N は偶数である必要があります")
    
    x = np.linspace(0, 1, N+1)
    y = np.sqrt(1 - x**2)
    h = 1 / N

    # 奇数インデックスの値は4倍
    odd_sum = np.sum(y[1:N:2])
    # 偶数インデックスの値は2倍
    even_sum = np.sum(y[2:N-1:2])

    integral = (h/3) * (y[0] + 4*odd_sum + 2*even_sum + y[N])
    return 4 * integral

# -------------------------------
# 動作確認
# -------------------------------
if __name__ == "__main__":
    N = 100000
    print("Rectangle(100000) =", Rectangle(N))
    print("Trapezoid(100000) =", Trapezoid(N))
    print("Simpson(100000)   =", Simpson(N))
    print("NumPy π           =", np.pi)
