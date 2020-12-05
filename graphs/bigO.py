#!pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Branching factor.
B = 2.8
# Search depth of d plies. d = 5.
x = np.linspace(1,5,500)
# Minimax Big O.
y_minimax = np.power(B, x)
# Alpha beta Big O.
y_a_b = np.sqrt(y_minimax)
# Plot:
plt.plot(x, y_minimax, label="Minimax")
plt.plot(x, y_a_b, label="Alpha-Beta")
plt.title("Big O Complexity")
plt.xlabel("Plies - Game Tree Depth level")
plt.ylabel("Operations")
plt.legend()
plt.savefig("TimeComplexityComparison.png")
plt.show()