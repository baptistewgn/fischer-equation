# Understanding the Fisher Equation: When to Use the Exact Formula for Real Interest Rates?

## Overview

This repository provides a detailed analysis of the Fisher Equation and its implications for estimating real interest rates. Using Python and Jupyter Notebook, the project explores the conditions under which the exact formula becomes essential compared to the common approximation:

$$
r \approx i - \pi
$$

While this approximation works in low-inflation environments, our analysis shows its limitations as inflation rises or the gap with the nominal rate widens. By visualizing these differences using heatmaps, the project highlights the importance of precision in financial decision-making.

## Key Insights

- Demonstrates the limitations of approximations in high-inflation scenarios.
- Visualizes the difference between exact and approximate methods for better comprehension.
- Helps inform more accurate financial and investment decisions.

## Repository Contents

- **`fischer-equation.ipynb`**: The Jupyter Notebook containing the full analysis, visualizations, and code.
- **`\codes`**: The folder containing the codes used for the analysis in R and Pyhton.
- **`\graphs`**: The folder containing the graphs created fot the analysis.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fisher-equation-analysis.git
   ```
2. Open the Jupyter Notebook:
   ```bash
   jupyter notebook fischer-equation.ipynb
   ```
3. Run the notebook to view the analysis and interact with the code and visualizations.

### Requirements

- Python 3.8 or higher
- Jupyter Notebook
- Required Python libraries:
  - NumPy
  - Matplotlib
  - Seaborn

Install the dependencies using:
```bash
pip install numpy matplotlib seaborn
```

## Results and Visualizations

The notebook includes:
- **Heatmaps** showing the error between the exact and approximate formulas across a range of nominal interest rates and inflation rates.
- **Key takeaways** summarizing when and why the exact Fisher Equation should be used.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests if you have ideas for improving the analysis or visualizations.
