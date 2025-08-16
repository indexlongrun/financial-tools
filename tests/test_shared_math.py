from shared_logic.math_utils import real_return


def test_real_return():
    # --- Inputs ---
    nominal_return = 0.06
    inflation_rate = 0.02
    print(f"\n--- Test: test_real_return ---")
    print(f"Input: nominal_return = {nominal_return}")
    print(f"Input: inflation_rate = {inflation_rate}")

    # --- Execution ---
    actual_return = real_return(nominal_return, inflation_rate)
    expected_return = (1 + nominal_return) / (1 + inflation_rate) - 1

    # --- Output & Verification ---
    print(f"Output: actual_return = {actual_return}")
    print(f"Output: expected_return = {expected_return}")
    assert abs(actual_return - expected_return) < 1e-12
    print("Result: PASS")
