import numpy as np
import pandas as pd

print("Data Science environment is ready!")
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")

# Простой пример
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85.5, 92.0, 88.5]
})

print("\nSample DataFrame:")
print(data)