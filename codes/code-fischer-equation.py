# %pip install seaborn

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the nominal interest rate and range of inflation values
i = 0.1  # Fixed nominal interest rate (10%)
pi = np.arange(0, 0.1, 0.0001)  # Inflation values from 0% to 10%

# Exact Fisher Equation
def y1(i, pi):
    return (1 + i) / (1 + pi) - 1

# Approximate Fisher Equation
def y2(i, pi):
    return i - pi

# Delta Computation
def y3(i, pi):
    return np.abs(y1(i, pi) - y2(i, pi))

# Plot
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))
ax1.plot(pi, y1(i, pi), label="exact", c="green")
ax1.plot(pi, y2(i, pi), label="approx", c="red", ls=":")
ax1.set_title("Fig1. Real Rate depending on inflation for i = 10%")
ax1.set_ylabel("Real rate")
ax1.set_xlabel("Inflation rate")
ax1.legend(loc="lower left")
ax2.plot(pi, y3(i, pi), c="blue")
ax2.set_title("Fig2. Delta depending on inflation pi for i = 10%")
ax2.set_ylabel("Delta")
ax2.set_xlabel("Inflation rate")
plt.show()

# Set nominal rate to 20%
i = 0.2

# Plot
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))
ax1.plot(pi, y1(i, pi), label="exact", c="green")
ax1.plot(pi, y2(i, pi), label="approx", c="red", ls=":")
ax1.set_title("Fig3. Real Rate depending on inflation for i = 20%")
ax1.set_ylabel("Real rate")
ax1.set_xlabel("Inflation rate")
ax1.legend(loc="lower left")
ax2.plot(pi, y3(i, pi), c="blue")
ax2.set_title("Fig4. Delta depending on inflation pi for i = 20%")
ax2.set_ylabel("Delta")
ax2.set_xlabel("Inflation rate")
plt.show()

# Define the range of values for nominal interest rates (i) and inflation rates (pi)
i_seq, pi_seq = np.arange(0, 0.51, 0.01), np.arange(0, 0.51, 0.01)

# Compute the Delta grid
delta_grid = y3(*np.meshgrid(i_seq, pi_seq))

# Plot the Heatmap
sns.heatmap(
    delta_grid,
    xticklabels=np.round(i_seq[::10], 2),
    yticklabels=np.round(pi_seq[::10], 2),
    cmap="viridis", cbar_kws={'label': 'Delta'}, square=True
)
plt.title("Fig5. Delta Value Depending on Both i and pi")
plt.xlabel("Nominal Rate"); plt.ylabel("Inflation Rate")
plt.xticks(ticks=np.arange(0, len(i_seq), 10), labels=np.round(i_seq[::10], 1))
plt.yticks(ticks=np.arange(0, len(pi_seq), 10), labels=np.round(pi_seq[::10], 1))
plt.xlim(0, len(i_seq))  # Ensure the x-axis starts at 0
plt.ylim(0, len(pi_seq))  # Ensure the y-axis starts at 0
plt.show()