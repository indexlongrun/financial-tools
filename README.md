
# IndexLongRun Financial Tools

A suite of open-source financial calculators and simulation engines designed for long-term planning. This project provides the core mathematical logic for the web tools available at [indexlongrun.com](https://www.indexlongrun.com).

## Philosophy

Our philosophy is built on three core principles:

1. **Transparency:** Financial planning shouldn't be a black box. All our calculations, assumptions, and methodologies are open for you to inspect, critique, and verify.
2. **Privacy-First:** We believe your financial data is yours alone. Our engines are designed to perform calculations without requiring personal data, and our web tools will never store your information without your explicit consent.
3. **Evidence-Based:** Our models are grounded in established financial theories and a long-term, passive investing approach.


## Repository Structure

This monorepo contains the logic for multiple financial tools. Each primary tool is organized in its own directory:

```
financial-tools/
├── notebooks/   # Jupyter notebooks to quickly run the logic
├── retirement_simulator/   # Monte Carlo simulator for traditional retirement
├── shared_logic/           # Common functions (e.g., inflation) used by multiple tools
└── ... (more tools coming soon)
```


## Featured Tool: Retirement Simulator

The core tool is a Monte Carlo simulator designed to assess the viability of long-term retirement plans.

### Simulation Methodology

To account for market uncertainty, the simulator runs thousands of randomized trials. This approach provides a range of possible outcomes and calculates the probability of success for your financial plan.

Portfolio values are projected using a **Geometric Brownian Motion** model:

$$
\Large P_{t+1} = P_t \times e^{(r - \frac{\sigma^2}{2}) + \sigma Z}
$$

Where:

- $P_{t+1}$: Portfolio value at the end of the year
- $P_t$: Portfolio value at the start of the year (after contributions/withdrawals)
- $r$: **Expected Annual Return**
- $\sigma$: **Annual Volatility** (standard deviation)
- $Z$: Random variable drawn from the standard normal distribution

For a detailed breakdown, see the README in `/retirement_simulator/`.


## Getting Started

Each tool in this repository can be run independently. The code is designed to be clear and easy to understand.

### Prerequisites

- Python 3.x
- NumPy

### Installation

```bash
pip install numpy
```

### Running a Simulation (Example: Retirement Simulator)

1. Navigate to the tool's directory:
	```bash
	cd retirement_simulator
	```
2. Run the primary engine script:
	```bash
	python engine.py
	```

Each engine script includes example parameters that you can modify to test different scenarios.
