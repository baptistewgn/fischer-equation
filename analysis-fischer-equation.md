# Relationship between the interest rate and inflation: The risk of overestimating real returns in Fisher's relation

---

# Table of Contents
1. [Introduction](#Introduction)  
2. [The Fisher Equation](#The-Fisher-Equation)  
3. [The Approximation of the Fisher Equation](#The-Approximation-of-the-Fisher-Equation)  
   - [Justification of the Approximation](#Justification-of-the-Approximation)  
   - [Validity of the Approximation: A Quantitative Examination](#Validity-of-the-Approximation:-A-Quantitative-Examination)  
4. [Influence of Nominal Rate](#Influence-of-Nominal-Rate)  
5. [Conclusion](#Conclusion)  
6. [Glossary](#Glossary)  
7. [Appendix - Fisher Equation: Origin and Derivation](#Appendix---Fisher-Equation:-Origin-and-Derivation)  

---

<a id="Introduction"></a>

# Introduction

The Fisher relationship, proposed by Irving Fisher in 1930, establishes a fundamental link between the nominal interest rate, the real interest rate, and the inflation rate. This relationship, often used in macroeconomics and finance, helps understand how inflation expectations influence real interest rates. For investors, mastering this relationship is crucial in making financial decisions, particularly concerning asset selection and the evaluation of expected real returns.

In a given economic context, investors seek to maximize their returns while minimizing risks. Understanding the Fisher relationship allows them to anticipate the impact of inflation on their future returns. For example, if an investor anticipates high inflation, they must ensure that the nominal interest rate offered by an investment is sufficiently high to maintain a positive real return, which implies adjusting their expectations accordingly.

The choice of the appropriate formula to estimate the real interest rate depends on the macroeconomic context, particularly the expected level of inflation. In a low inflation situation, the simplified approximation $r \approx i - \pi$ is often sufficient to estimate the real return of an investment. This method, simple and quick, allows evaluations without resorting to complex calculations. However, when inflation is higher, this approximation can become inaccurate and lead to errors in estimating real returns. In such cases, using the exact Fisher formula is recommended to obtain a more precise estimate, which is essential to avoid underestimating risks or misanticipating returns.

**Which formula should be used to accurately estimate the real interest rate in different macroeconomic scenarios, and how does this accuracy impact investment decisions?**

The choice between the approximation and the exact Fisher formula is not trivial. A poor estimation of the real interest rate can lead to suboptimal investment decisions, such as underestimating the risks associated with higher than expected inflation or misanticipating real returns. This document therefore explores (or at least provides a non-exhaustive overview of) the conditions under which the Fisher approximation is admissible and identifies situations where it can lead to significant errors.

<a id="The-Fischer-Equation"></a>

# The Fisher Equation

The basic equation proposed by Fisher is expressed as follows:

$$

(1+i) = (1+r)(1+\pi)\\

$$

with $i$ the nominal interest rate, $r$ the real interest rate and $\pi$ the expected inflation rate (regardless of its calculation method).

This equation can be rearranged to express the real interest rate $r$ as follows:

$$
(1+i) = (1+r)(1+\pi)\\(1+r) = \frac{(1+i)}{(1+\pi)}\\
$$

Expanding, we obtain:

$$

r = \frac{(1+i)}{(1+\pi)}-1

$$

This exact relationship shows that the real interest rate is influenced by the nominal interest and inflation rates.

The origin and derivation of the Fisher equation can be found in the *appendix*. It will be considered as accepted in this document.

<a id="The-Approximation-of-the-Fisher-Equation"></a>

# The Approximation of the Fisher Equation

In a low inflation context (i.e. $\pi \approx 0$), the Fisher equation can be simplified, giving rise to an often-used approximation:

$$

i \approx r + \pi\\

$$

Or equivalently:

$$

r \approx i - \pi

$$

So, where does this approximation come from? And can it be considered reliable?

<a id="Justification-of-the-Approximation"></a>

# Justification of the Approximation

The approximation is based on the fact that when the inflation rate $\pi$ is close to zero, the product $r \times \pi$ becomes negligible in the expansion of the original equation:

$$
(1+i) = (1+r)(1+\pi)\\
(1+i) = 1 + \pi + r + r \times \pi\\
i = \pi + r + \overbrace{r \times \pi}^{\approx 0}\\
$$

This allows us to simplify the equation to:

$$
i \approx r + \pi
$$

We see here that, mathematically speaking, this approximation is admissible, but then, to what extent?

<a id="Validity-of-the-Approximation:-A-Quantitative-Examination"></a>

# Validity of the Approximation: A Quantitative Examination

## Numerical Analysis

To evaluate the validity of this approximation, consider a numerical example by setting $i = 0.1$ (a nominal rate of 10%) and calculating the real rate $r$ with the approximation and the exact formula. We then evaluate the difference $\Delta$ between these two results for different levels of inflation $\pi$.

<center>

**Results Table**

| $\pi$ | $r_{approx.}$ | $r_{real}$ | $\Delta$ (in pp) |
| --- | --- | --- | --- |
| 0.5% | 9.50% | 9.45% | 0.05 |
| 1.0% | 9.00% | 8.91% | 0.09 |
| 1.5% | 8.50% | 8.37% | 0.13 |
| 2.0% | 8.00% | 7.84% | 0.16 |
| 2.5% | 7.50% | 7.32% | 0.18 |
| 3.0% | 7.00% | 6.80% | 0.20 |
| 3.5% | 6.50% | 6.28% | 0.22 |
| 4.0% | 6.00% | 5.77% | 0.23 |
| 4.5% | 5.50% | 5.26% | 0.24 |
| 5.0% | 5.00% | 4.76% | 0.24 |
| 5.5% | 4.50% | 4.27% | 0.23 |
| 6.0% | 4.00% | 3.77% | 0.23 |
| 6.5% | 3.50% | 3.29% | 0.21 |
| 7.0% | 3.00% | 2.80% | 0.20 |
| 7.5% | 2.50% | 2.33% | 0.17 |
| 8.0% | 2.00% | 1.85% | 0.15 |
</center>

Formulas used:

$$
r_{real} = \frac{(1+i)}{(1+\pi)}-1\\
r_{approx.} \approx i - \pi\\
\Delta = |r_{approx.}-r_{real}|
$$
The results show that for a low inflation rate (e.g. $0.005 \leq \pi \leq 0.02$), the approximation is acceptable with a maximum deviation of 0.16 percentage points (pp). However, as inflation increases (e.g. $0.025 \leq \pi \leq 0.055$), the deviation $\Delta$ increases, reaching 0.24 pp. Finally, when the inflation rate becomes high (e.g. $\pi > 0.055$), the accuracy of the approximation increases (e.g. $\Delta$ decreases).

## Graphical Analysis

For clearer visualization, we can graphically represent the curves of $r_{approx.}$, $r_{real}$, and $\Delta$ as a function of $\pi$. This graph shows that the approximation becomes less accurate for higher levels of inflation but becomes accurate again for even higher inflation rates.

![fig1-2](fischer-equation/graphs/fig1-2.png)

These results can lead us to the following hypotheses:
<center>

| Value of $\pi$ | Hypothesis |
| --- | --- |
| Low (e.g. $0.005≤ \pi ≤ 0.02$) | $r_{approx.} \approx r_{real}$ |
| Medium (e.g. $0.025≤ \pi ≤ 0.055$) | $r_{approx.} \neq r_{real}$ |
| High (e.g. $\pi > 0.055$) | $r_{approx.} \approx r_{real}$ |
</center>

<a id="Influence-of-Nominal-Rate"></a>

# Influence of Nominal Rate

The previous analysis assumes a fixed nominal rate of $i = 0.1$. It is interesting to examine the impact of increasing $i$ on the accuracy of the approximation. Let’s redo the same calculations for $i = 0.2$.

![fig3-4](fischer-equation/graphs/fig3-4.png)

The results show that for a higher nominal rate (e.g. $i = 0.2$), the deviation $\Delta$ between $r_{approx.}$ and $r_{real}$ tends to increase with inflation, suggesting that the approximation becomes less reliable in a high-interest-rate context.

In this case, we can clearly see that our previous hypothesis that in a high-rate environment, $r_{approx.} \approx r_{real}$ seems false (at least for $\pi \in [0;0.1]$). Indeed, in this case, $r_{approx.}$ and $r_{real}$ seem to diverge when $\pi \mapsto \infty$. In other words, in this scenario, $\Delta$ increases as $\pi$ increases.

Returning to our relation $r = \frac{(1+i)}{(1+\pi)}-1$, we understand that $r$ depends on two variables, $i$ and $\pi$.

Let’s now see how our variable $r$ behaves based on the values of $i$ and $\pi$.

![fig5](fischer-equation/graphs/fig5.png)

The graph highlights different scenarios based on the relationships between inflation and the nominal interest rate. In areas marked by a gradient of green and yellow, where inflation is high and the nominal rate is low, the tracking error between the exact Fisher formula and its approximation becomes significant. This indicates that, under these conditions, the approximation is not precise enough to correctly estimate the real interest rate.

Conversely, when inflation is low or close to the nominal rate (e.g., along the diagonal of the heatmap), the approximation seems adequate and can provide a reasonable estimate of the real interest rate. However, when the nominal rate remains low but inflation becomes moderate, the precision of the approximation decreases, as shown by the blue areas to the right of the graph.

In summary, the accuracy of the real interest rate estimate strongly depends on the relationship between inflation and the nominal rate. When these two variables are close, the approximation $r \approx i - \pi$ remains reliable. However, as the gap between $i$ and $\pi$ widens, the error ($\Delta$) between the exact formula and the approximation increases significantly, as illustrated by the blue and yellow areas above the diagonal.

<a id="Conclusion"></a>

# Conclusion

The Fisher relationship provides an essential framework for understanding how real interest rates react to changes in inflation and nominal interest rates. As the quantitative and graphical analysis shows, the simplified approximation $r \approx i - \pi$ can be adequate in low inflation contexts, where the gap between the nominal interest rate and the inflation rate is small. However, when inflation is high or this gap becomes significant, using the exact Fisher formula becomes imperative to avoid substantial errors in estimating the real interest rate.

These errors can have significant consequences on investment decisions. An imprecise estimate of the real interest rate can lead to a poor evaluation of future returns, thereby compromising the profitability of investments. Therefore, investors must be attentive to the macroeconomic context and choose the appropriate estimation method for the real interest rate, based on the expected inflation and prevailing nominal rates.

---

<a id="Glossary"></a>

# Glossary

**Nominal Interest Rate**

> The nominal interest rate is the stated or contractual rate of return on an investment or loan, without adjustment for inflation.

**Real Interest Rate**

> The real interest rate is the rate of return on an investment or loan adjusted for inflation. It measures the additional purchasing power an investor gains after accounting for inflation.

**Inflation**

> Inflation is the general and sustained increase in the prices of goods and services in an economy over a given period. It results in a decrease in the purchasing power of money, as the same amount of money buys fewer goods and services than before. The inflation rate is generally expressed as a percentage and is often measured by indices such as the Consumer Price Index (CPI).

---

<a id="Appendix---Fisher-Equation:-Origin-and-Derivation"></a>

# Appendix - Fisher Equation: Origin and Derivation

The Fisher equation, proposed by economist Irving Fisher in 1930 in his book "The Theory of Interest" arose from the need to understand how inflation expectations influence nominal and real interest rates. Fisher sought to establish a relationship that could decompose the nominal interest rate into two components: the real interest rate and the anticipated inflation rate. This relationship proved fundamental for economic theory, particularly in finance and monetary policy.

The Fisher equation is based on the idea that the nominal interest rate $i$ represents the compensation that investors demand not only for deferring current consumption (measured by the real interest rate $r$) but also to compensate for the erosive effect of anticipated future inflation (measured by the inflation rate $\pi$).

The basic equation can be derived as follows:

1. Consider an amount of money $P$ invested today for a period of one year. At the end of this period, the future nominal value of this investment, accounting for the nominal interest rate $i$, is given by:
    
$$

FV = P \times (1 + i)

$$
    
2. To express this value in real terms (i.e., adjusting for inflation), we must account for the inflation rate $\pi$. If inflation is positive, the purchasing power of money decreases, and the future real value $FV_{adjusted}$ of the investment is given by:
    
$$

FV_{adjusted} = \frac{P \times (1 + i)}{1 + \pi}

$$
    
3. The future real value must also equal the initial value $P$ multiplied by the purchasing power increase factor, which is represented by the real rate $r$:
    
$$

FV_{real} = P \times (1 + r)

$$
    
4. By equating the two expressions $(2.)$ and $(3.)$ of the future real value, we get:
    
$$
    
    P \times (1 + r) = \frac{P \times (1 + i)}{1 + \pi}
    
$$
   
Here, a negative one-to-one relationship between inflation and purchasing power is considered. In other words, when inflation increases by 1 point, purchasing power decreases by 1 point for a given $P$. By definition, $r$ is already "adjusted" for inflation, which allows for the equality of $(2.)$ and $(3.)$.
    
5. By simplifying, canceling $P$ from both sides, and rearranging the terms, we get the complete Fisher equation:
    
$$
    (1 + r) = \frac{(1 + i)}{(1 + \pi)}
$$
    
Or, in an even more explicit form:
    
$$
    r = \frac{(1 + i)}{(1 + \pi)} - 1
$$
    
This equation shows that the real interest rate $r$ is determined by the nominal interest rate $i$ adjusted for inflation $π$. It highlights how inflation directly impacts the real return on investments.