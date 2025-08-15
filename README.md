# **IndexLongRun's Financial Tools**

A suite of open-source financial calculators and simulation engines designed for long-term planning. This project provides the core mathematical logic for the web tools available at [indexlongrun.com](https://www.indexlongrun.com).

Our philosophy is built on three core principles:

1. **Transparency:** Financial planning shouldn't be a black box. All our calculations, assumptions, and methodologies are open for you to inspect, critique, and verify.  
2. **Privacy-First:** We believe your financial data is yours alone. Our engines are designed to perform calculations without requiring personal data, and our web tools will never store your information without your explicit consent.  
3. **Evidence-Based:** Our models are grounded in established financial theories and a long-term, passive investing approach.

## **Repository Structure**

This repository is a monorepo containing the logic for various financial tools. Each primary tool is organized into its own directory.

/financial-tools  
|  
|-- 📁 /retirement\_simulator/   \# Monte Carlo simulator for traditional retirement  
|-- 📁 /shared\_logic/           \# Common functions (e.g., inflation) used by multiple tools  
|-- ... (more tools to come)

## **Tool: The Retirement Simulator**

Our core tool is a powerful Monte Carlo simulator designed to assess the viability of a long-term retirement plan.

### **Simulation Methodology**

To account for market uncertainty, we don't just predict one future; we simulate thousands of them. By running a large number of randomized trials, we can understand the range of possible outcomes and calculate the probability of success for your financial plan.

The value of the portfolio from one year to the next is calculated using a **Geometric Brownian Motion** model:


$$
\Large P_{t+1} = P_t \times e^{(r - \frac{\sigma^2}{2}) + \sigma Z}
$$


Where:

* P\_t+1 is the portfolio value at the end of the year.  
* P\_t is the portfolio value at the start of the year (after contributions or withdrawals).  
* r is the **Expected Annual Return**.  
* sigma (sigma) is the **Annual Volatility** (standard deviation).  
* Z is a random variable drawn from the standard normal distribution.

For a detailed breakdown of the process, please see the README.md file within the /retirement\_simulator/ directory.

## **How to Use This Engine**

Each tool within this repository can be run independently. The code is designed to be clear and easy to understand.

**Prerequisites:**

* Python 3.x  
* NumPy

**Installation:**

```pip install numpy```

**Running a Simulation (Example: Retirement Simulator):**

1. Navigate to the tool's directory.  
2. Run the primary engine script.

```cd retirement\_simulator```  
```python engine.py```

Each engine script is pre-filled with example parameters that you can modify directly to test different scenarios.
