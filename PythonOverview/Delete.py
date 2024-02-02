# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Generating synthetic data
np.random.seed(0)
x = np.linspace(-1, 1, 100)
y = 2 * x + np.random.normal(0, 0.1, 100)  # Linear relation with noise

# Plotting the data
plt.scatter(x, y)
plt.xlabel('x')
plt.show()

# %%# Splitting the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# %%
# Building a neural network
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compiling the model
model.compile(optimizer=Adam(learning_rate=0.01), loss='mean_squared_error')

# Training the model (potentially overfitting)
history = model.fit(x_train, y_train, epochs=500, verbose=0)

# Evaluating the model on training data
train_loss = model.evaluate(x_train, y_train, verbose=0)

print(f"Training loss: {train_loss}")

# Evaluating the model on test data
test_loss = model.evaluate(x_train, y_train, verbose=0)

print(f"Test loss: {test_loss}")
# %%
