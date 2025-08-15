from shared_logic.math_utils import real_return


def test_real_return():
    r = real_return(0.06, 0.02)
    assert abs(r - ((1.06/1.02) - 1)) < 1e-12
