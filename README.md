# ProbabilityLab

Practicing probability while teaching myself to code in Python.

## Experiments

### 1. Birthday Problem
Calculates the probability that at least two people in a group share
the same birthday.

The program compares a Monte Carlo simulation with the exact probability:

$$
P(\text{shared birthday})
=
1 - \frac{365 \cdot 364 \cdots (365-n+1)}{365^n}
$$

For n = 23:

- Exact probability: 0.5073
- Monte Carlo estimate: approximately 0.507
