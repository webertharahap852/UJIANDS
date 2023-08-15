import pandas as pd
import matplotlib.pyplot as plt
import json

# Membaca data dari file JSON
with open('raw.json', 'r') as f:
    data = json.load(f)

# Membuat DataFrame dari data JSON
df = pd.DataFrame(data)

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['avg_num_visit'], df['avg_promotion'],
            c=df['tenure'], cmap='viridis')
plt.xlabel('Average Number of Visits')
plt.ylabel('Average Promotion')
plt.title('Scatter Plot of Average Number of Visits vs. Average Promotion')
plt.colorbar(label='Tenure')
plt.grid(True)
plt.show()
