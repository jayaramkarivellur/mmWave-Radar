import numpy as np
import matplotlib.pyplot as plt

def plot_te_mode(m, n, a=1.0, b=0.5, resolution=100):
    """
    Plot the magnitude of the TE_mn mode field pattern in a rectangular waveguide.
    
    Parameters:
        m, n       : Mode indices (integers)
        a, b       : Waveguide dimensions (in meters)
        resolution : Grid resolution for plotting
    """
    x = np.linspace(0, a, resolution)
    y = np.linspace(0, b, resolution)
    X, Y = np.meshgrid(x, y)

    Hz = np.cos(m * np.pi * X / a) * np.cos(n * np.pi * Y / b)
    field_magnitude = np.abs(Hz)

    plt.figure(figsize=(6, 4))
    plt.contourf(X, Y, field_magnitude, 50, cmap='viridis')
    plt.colorbar(label='|Hz|')
    plt.title(f'TE{m}{n} Mode in Rectangular Waveguide')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.grid(True, linestyle=':')
    plt.tight_layout()
    plt.show()

# Example usage: plot TE10, TE11, and TE20
plot_te_mode(1, 0)  # Dominant mode
plot_te_mode(1, 1)  # Higher-order mode
plot_te_mode(2, 0)  # Higher-order mode
