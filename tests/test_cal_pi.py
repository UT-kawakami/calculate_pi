import numpy as np
from main import rectangle_integration, trapezoid_integration, simpson_integration

def test_rectangle_pi_accuracy():
    """
    長方形近似によるπの近似精度テスト
    許容誤差は1e-4とする
    """
    intervals = 10_000
    pi_estimate = rectangle_integration(intervals)
    error = abs(pi_estimate - np.pi)
    assert error < 1e-4, f"[Rectangle] 誤差が大きすぎます: {error}"

def test_trapezoid_pi_accuracy():
    """
    台形近似によるπの近似精度テスト
    許容誤差は1e-6とする
    """
    intervals = 10_000
    pi_estimate = trapezoid_integration(intervals)
    error = abs(pi_estimate - np.pi)
    assert error < 1e-6, f"[Trapezoid] 誤差が大きすぎます: {error}"

def test_simpson_pi_accuracy():
    """
    シンプソン則によるπの近似精度テスト
    許容誤差は1e-7とする
    """
    intervals = 10_000  # 偶数必須
    pi_estimate = simpson_integration(intervals)
    error = abs(pi_estimate - np.pi)
    assert error < 1e-7, f"[Simpson] 誤差が大きすぎます: {error}"
