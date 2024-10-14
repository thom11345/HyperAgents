import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# model_results = pd.read_csv('analysis/agent_models.csv')
model_results = pd.read_csv('analysis/heuristic_models.csv')
df = pd.DataFrame(model_results)

# Create the bar chart
plt.barh(model_results['Model'], model_results['Regret'])

plt.xlabel('Average Regret')
plt.ylabel('Model')
plt.grid(axis='x')
plt.tight_layout()

plt.show()