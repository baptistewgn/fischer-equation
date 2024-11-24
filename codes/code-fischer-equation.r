# Set the nominal interest rate and range of inflation values
i <- 0.1  # Fixed nominal interest rate (10%)
pi <- seq(0, 0.1, 0.0001)  # Inflation values from 0% to 10%

# Exact Fisher Equation
y1 <- function(i, pi) {
  return((1 + i) / (1 + pi) - 1)
}

# Approximate Fisher Equation
y2 <- function(i, pi) {
  return(i - pi)
}

# Plot Exact vs. Approximate Fisher Equations
plot(pi, y1(i, pi), 
     main = "Is Fisher Approximation Correct?", 
     xlab = "Inflation Rate", 
     ylab = "Real Rate", 
     type = "l", col = "red")
lines(pi, y2(i, pi), col = "green")
legend('topright', inset = 0.05, c("Exact", "Approximation"), lty = 1, col = c("red", "green"))

# Delta Computation
y3 <- function(i, pi) {
  return(abs(y1(i, pi) - y2(i, pi)))
}

# Plot Delta Between Exact and Approximate Fisher Equation
plot(pi, y3(i, pi), 
     main = "Delta Between Fisher and Approximation", 
     xlab = "Inflation Rate", 
     ylab = "Delta", 
     type = "l")

# Real Rate Depending on Both Nominal and Inflation Rate

# Define the range of values for nominal interest rates i and inflation rates pi
i_seq <- seq(0, 0.5, by = 0.01)  # Nominal rates from 0% to 50%
pi_seq <- seq(0, 0.5, by = 0.01)  # Inflation rates from 0% to 50%

# Create a grid of values
grid <- expand.grid(i = i_seq, pi = pi_seq)

# Apply the delta function to the grid
grid$delta <- mapply(y3, grid$i, grid$pi)

# Visualize the Delta as a Heatmap
ggplot(grid, aes(x = i, y = pi, fill = delta)) +
  geom_tile() +
  scale_fill_viridis_c() +
  labs(title = "Heatmap of Delta Between Exact and Approximate Fisher Equation",
       x = "Nominal Rate",
       y = "Inflation Rate",
       fill = "Delta")