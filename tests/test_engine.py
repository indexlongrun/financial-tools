import numpy as np
from retirement_simulator.engine import run_simulation


def test_run_simulation_basic():
    # --- Inputs ---
    params = {
        "starting_balance": 100_000,
        "annual_contribution": 5_000,
        "withdrawal": 2_000,
        "years": 10,
        "expected_return": 0.05,
        "volatility": 0.1,
        "trials": 500,
        "random_seed": 1
    }
    print(f"\n--- Test: test_run_simulation_basic ---")
    for key, value in params.items():
        print(f"Input: {key} = {value}")

    # --- Execution ---
    res = run_simulation(**params)

    # --- Output & Verification ---
    print(f"Output: trials = {res.trials}")
    print(f"Output: success_rate = {res.success_rate:.2%}")
    print(f"Output: final_values (first 5) = {res.final_values[:5]}")
    assert res.trials == params["trials"]
    assert 0.0 <= res.success_rate <= 1.0
    assert isinstance(res.final_values, np.ndarray)
    print("Result: PASS")


def test_zero_volatility_predictable():
    # --- Inputs ---
    params = {
        "starting_balance": 50_000,
        "annual_contribution": 1_000,
        "withdrawal": 500,
        "years": 5,
        "expected_return": 0.03,
        "volatility": 0.0,
        "trials": 100,
        "random_seed": 2
    }
    print(f"\n--- Test: test_zero_volatility_predictable ---")
    for key, value in params.items():
        print(f"Input: {key} = {value}")

    # --- Execution ---
    res = run_simulation(**params)

    # --- Verification ---
    # 1. Calculate the expected final balance deterministically (year by year).
    # This replicates the simulation's logic without the random component.
    deterministic_balance = params["starting_balance"]
    for _ in range(params["years"]):
        deterministic_balance += params["annual_contribution"]
        # The Geometric Brownian Motion formula simplifies when volatility (sigma) is 0
        deterministic_balance *= np.exp(params["expected_return"])
        deterministic_balance -= params["withdrawal"]
    
    # 2. The simulation result for every trial should match this deterministic calculation.
    simulation_result = res.final_values[0]

    # --- Output ---
    print(f"Output: simulation_result (first 5) = {res.final_values[:5]}")
    print(f"Output: deterministic_balance (calculated) = {deterministic_balance:.2f}")
    print(f"Output: simulation_result (all trials) = {simulation_result:.2f}")
    
    # 3. Assert that the simulation's output is very close to the deterministic calculation.
    assert np.allclose(res.final_values, deterministic_balance)
    print("Result: PASS")
