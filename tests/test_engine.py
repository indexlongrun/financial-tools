import numpy as np
from retirement_simulator.engine import run_simulation


def test_run_simulation_basic():
    res = run_simulation(starting_balance=100_000, annual_contribution=5_000, withdrawal=2_000, years=10,
                         expected_return=0.05, volatility=0.1, trials=500, random_seed=1)
    # basic sanity checks
    assert res.trials == 500
    assert 0.0 <= res.success_rate <= 1.0
    assert isinstance(res.final_values, np.ndarray)


def test_zero_volatility_predictable():
    # With zero volatility and fixed return, final_values should be identical across trials
    res = run_simulation(starting_balance=50_000, annual_contribution=1_000, withdrawal=500, years=5,
                         expected_return=0.03, volatility=0.0, trials=100, random_seed=2)
    assert np.allclose(res.final_values, res.final_values[0])
