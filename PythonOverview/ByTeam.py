# %%
import ipywidgets as widgets
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt

# %%
# Create a slider
slider = widgets.FloatSlider(
    value=1,         # Initial value
    min=0,           # Minimum value
    max=3,          # Maximum value
    step=0.5,          # Step size
    description='Test Slider:',  # Description of the slider
)

def plot_sine(frequency):
    # Create a sine wave
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(2*np.pi*x*frequency)
    # Plot the sine wave
    plt.plot(x, y)
    plt.show()

# %%
# Linnnk the sliker to the plot
widgets.interact(plot_sine, frequency=slider)
# %%
