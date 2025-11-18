import numpy as np

def rectangle_integration(num_intervals: int) -> float:
    """
    長方形近似による π の近似計算
    区間 [0,1] を num_intervals 等分し、関数 sqrt(1-x^2) の面積を計算
    """
    x_values = np.arange(num_intervals) / num_intervals
    y_values = np.sqrt(1 - x_values**2)
    area = 4 * np.sum(y_values) / num_intervals
    return area

def trapezoid_integration(num_intervals: int) -> float:
    """
    台形近似による π の近似計算
    """
    x_values = np.linspace(0, 1, num_intervals + 1)
    y_values = np.sqrt(1 - x_values**2)
    step = 1 / num_intervals
    area = (step / 2) * (y_values[0] + 2 * np.sum(y_values[1:-1]) + y_values[-1])
    return 4 * area

def simpson_integration(num_intervals: int) -> float:
    """
    シンプソン則による π の近似計算
    num_intervals は偶数である必要があります
    """
    if num_intervals % 2 != 0:
        raise ValueError("num_intervals must be even for Simpson's rule")

    x_values = np.linspace(0, 1, num_intervals + 1)
    y_values = np.sqrt(1 - x_values**2)
    step = 1 / num_intervals

    odd_sum = np.sum(y_values[1:num_intervals:2])
    even_sum = np.sum(y_values[2:num_intervals-1:2])

    area = (step / 3) * (y_values[0] + 4 * odd_sum + 2 * even_sum + y_values[-1])
    return 4 * area

def main():
    intervals = 10_000
    print(f"Rectangle ({intervals} intervals): {rectangle_integration(intervals)}")
    print(f"Trapezoid ({intervals} intervals): {trapezoid_integration(intervals)}")
    print(f"Simpson   ({intervals} intervals): {simpson_integration(intervals)}")
    print(f"NumPy π: {np.pi}")

if __name__ == "__main__":
    main()
