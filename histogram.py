import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file JSON
data = pd.read_json('raw.json')

# Membuat DataFrame dari data
df = pd.DataFrame(data)

# Menentukan variabel yang akan diplot dalam histogram
variables_to_plot = ['avg_num_visit', 'avg_promotion']

# Membuat subplot dengan ukuran 1 baris dan 2 kolom
plt.figure(figsize=(12, 6))

# Loop untuk membuat histogram untuk setiap variabel
for i, variable in enumerate(variables_to_plot, 1):
    plt.subplot(1, 2, i)
    plt.hist(df[variable], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel(variable)
    plt.ylabel('Frekuensi')
    plt.title(f'Histogram {variable}')

plt.tight_layout()
plt.show()
