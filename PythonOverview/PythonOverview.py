# %%
import numpy as np
import matplotlib.pyplot as plt

x = 1

# %% Make a synthetic pandas dataset
import pandas as pd
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
print(df)

# %%
# Simple plot of a sine wave between 0 and pi
x = np.linspace(0, 4*np.pi, 100)
y = np.cos(x)
plt.plot(x, y)
plt.show()

y = x
print(y)
# %%
