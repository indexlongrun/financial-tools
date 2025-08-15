"""Simple script to run the retirement demo from project root."""
from retirement_simulator import run_simulation


def main():
    res = run_simulation(200_000, 10_000, 30_000, years=25, trials=2000, random_seed=3)
    print(f"Trials: {res.trials}")
    print(f"Success rate: {res.success_rate:.2%}")


if __name__ == "__main__":
    main()
