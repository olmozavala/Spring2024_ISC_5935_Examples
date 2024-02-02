# %%
import numpy as np

# A big loop for random matrix multiplication
def big_loop(msize = 100):
    for i in range(1):
        a = np.random.rand(msize, msize)
        b = np.random.rand(msize, msize)
        c = np.dot(a, b)

    print(f"Done: {c[0:10,0:10]}")


# %%
big_loop(10000)
