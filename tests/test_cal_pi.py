import numpy as np
from main import Rectangle

def test_pi_approximation_accuracy():
    """
    区分求積法による円周率近似の精度テスト
    numpy の π を基準に、誤差が指定以下なら合格
    """
    # 区分数を指定（多いほど精度が上がる）
    n_intervals = 1_000

    # πを近似
    pi_estimate = Rectangle(n_intervals)

    # numpyの真の値
    pi_true = np.pi

    # 誤差
    error = abs(pi_estimate - pi_true)

    # 許容誤差（区分数に応じて調整可能）
    tolerance = 1e-6

    # テスト条件
    assert error < tolerance, f"誤差が許容値を超えています: {error}"