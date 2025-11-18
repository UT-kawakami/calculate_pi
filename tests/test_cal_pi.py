import numpy as np
from main import Rectangle, Trapezoid

def test_rectangle_pi_accuracy():
    """
    長方形近似(Rectangle) による π の精度テスト
    """
    n_intervals = 10_000

    pi_estimate = Rectangle(n_intervals)
    pi_true = np.pi
    error = abs(pi_estimate - pi_true)

    # 長方形近似は O(1/N) 精度なので少し緩めに
    tolerance = 1e-4

    assert error < tolerance, f"Rectangle 法の誤差が許容値を超えています: {error}"


def test_trapezoid_pi_accuracy():
    """
    台形近似(Trapezoid) による π の精度テスト
    """
    n_intervals = 10_000

    pi_estimate = Trapezoid(n_intervals)
    pi_true = np.pi
    error = abs(pi_estimate - pi_true)

    # 台形法は O(1/N^2) なので非常に精度が高い
    tolerance = 1e-6

    assert error < tolerance, f"Trapezoid 法の誤差が許容値を超えています: {error}"
