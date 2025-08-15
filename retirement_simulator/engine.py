"""Retirement Monte Carlo simulator (vectorized).

Provides a fast, vectorized `run_simulation` that generates trials in bulk using
NumPy. The function returns a small dataclass with final values and a success rate.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from typing import Optional


@dataclass
class SimulationResult:
    trials: int
    success_rate: float
    final_values: np.ndarray


def run_simulation(
    starting_balance: float,
    annual_contribution: float,
    withdrawal: float,
    years: int,
    expected_return: float = 0.06,
    volatility: float = 0.15,
    trials: int = 10_000,
    random_seed: Optional[int] = 42,
) -> SimulationResult:
    """Run a Monte Carlo simulation using yearly Geometric Brownian Motion.

    This implementation is vectorized across trials for performance. Contributions
    are applied at the start of each year and withdrawals at the end.

    Returns
    -------
    SimulationResult
        Contains the number of trials, success rate (fraction of trials with final
        balance > 0), and the array of final values.
    """
    rng = np.random.default_rng(random_seed)

    # Draw standard normal random variables: shape (years, trials)
    z = rng.standard_normal(size=(years, trials))

    mu = expected_return
    sigma = volatility
    dt = 1.0

    # Initialize balances: shape (trials,)
    balances = np.full(trials, starting_balance, dtype=float)

    for year in range(years):
        # Apply contribution at start of year
        balances += annual_contribution

        # GBM yearly step: multiply by exp((mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*z)
        factors = np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z[year])
        balances = balances * factors

        # Apply withdrawal at end of year
        balances -= withdrawal

        # Floor at zero — once zero it stays zero
        np.maximum(balances, 0.0, out=balances)

    final_values = balances
    success_rate = float(np.count_nonzero(final_values > 0) / trials)
    return SimulationResult(trials=trials, success_rate=success_rate, final_values=final_values)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run a vectorized retirement Monte Carlo simulation")
    parser.add_argument("--start", type=float, default=500_000.0, help="Starting balance")
    parser.add_argument("--contrib", type=float, default=10_000.0, help="Annual contribution")
    parser.add_argument("--withdraw", type=float, default=40_000.0, help="Annual withdrawal during retirement")
    parser.add_argument("--years", type=int, default=30, help="Number of years to simulate")
    parser.add_argument("--trials", type=int, default=5000, help="Number of trials to run")
    args = parser.parse_args()

    res = run_simulation(starting_balance=args.start, annual_contribution=args.contrib,
                         withdrawal=args.withdraw, years=args.years, trials=args.trials)
    print(f"Trials: {res.trials}")
    print(f"Success rate: {res.success_rate:.2%}")
    print(f"Median final value: {np.median(res.final_values):,.2f}")
