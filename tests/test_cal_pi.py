import numpy as np
from main import Rectangle, Trapezoid, Simpson

def test_rectangle_pi_accuracy():
    N = 100_000
    pi_est = Rectangle(N)
    error = abs(pi_est - np.pi)
    assert error < 1e-4, f"Rectangle 誤差が大きい: {error}"

def test_trapezoid_pi_accuracy():
    N = 100_000
    pi_est = Trapezoid(N)
    error = abs(pi_est - np.pi)
    assert error < 1e-6, f"Trapezoid 誤差が大きい: {error}"

def test_simpson_pi_accuracy():
    N = 100_000  # 偶数にする
    pi_est = Simpson(N)
    error = abs(pi_est - np.pi)
    assert error < 1e-7, f"Simpson 誤差が大きい: {error}"
