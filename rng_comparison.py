import matplotlib.pyplot as plt
import numpy as np

def generate_bad_rng(n):
    """Generates a sequence using a poor Linear Congruential Generator (LCG)
    to demonstrate 'striping' or patterns."""
    # Parameters for a "bad" generator
    m = 256  # Small modulus
    a = 137
    c = 1
    
    x = 1 # Seed
    results = []
    for _ in range(n):
        x = (a * x + c) % m
        results.append(x / m) # Normalize to [0, 1]
    return np.array(results)

def generate_good_rng(n):
    """Generates a sequence using Python's standard robust generator (Mersenne Twister)"""
    return np.random.rand(n)

# 1. Generate Data
n_points = 500
bad_data = generate_bad_rng(n_points)
good_data = generate_good_rng(n_points)

# 2. Create Lag-1 Pairs (x[i], x[i+1])
# For Bad RNG
bad_x = bad_data[:-1]
bad_y = bad_data[1:]

# For Good RNG
good_x = good_data[:-1]
good_y = good_data[1:]

# 3. Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot Bad RNG
ax1.scatter(bad_x, bad_y, alpha=0.6, s=15, color='red')
ax1.set_title('Bad RNG (Lag-1 Plot)\nNote the visible lines/lattice structure', color='darkred', weight='bold')
ax1.set_xlabel('$U_i$')
ax1.set_ylabel('$U_{i+1}$')
ax1.grid(True, linestyle='--', alpha=0.3)

# Plot Good RNG
ax2.scatter(good_x, good_y, alpha=0.6, s=15, color='green')
ax2.set_title('Good RNG (Lag-1 Plot)\nNote the random "cloud" with no pattern', color='darkgreen', weight='bold')
ax2.set_xlabel('$U_i$')
ax2.set_ylabel('$U_{i+1}$')
ax2.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('rng_comparison.png')