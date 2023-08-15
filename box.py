import pandas as pd
import matplotlib.pyplot as plt

# Data dalam bentuk DataFrame
data = {
    'tenant_id': [12336009752852, 359290056708112, 13327005405727, 12336009545942, 359254061684940, 359206051922227, 12336005164391],
    'tenure': [2, 4, 3, 1, 4, 1, 3],
    'employee': [3.0, None, 2.0, 1.0, 2.0, 1.0, 1.0],
    'ownership': ['rent', 'rent', 'own', 'own', 'rent', 'own', 'own'],
    'avg_num_visit': [0.221944, 6.929247, 9.100100, 9.216673, 5.019374, 12.772986, 0.151258],
    'avg_promotion': [0.637752, 0.403893, 0.135532, 0.421228, 0.267538, 0.108748, 1.678097],
    'avg_sales_call_duration': [1.150045, 0.325592, 1.484479, 3.053756, 2.611484, 2.059884, 1.618929],
    'avg_visit_duration': [4.404288, 1.695479, 13.987075, 8.267001, 20.065617, 4.261116, 3.403725],
    'revenue': [3.513797, -35.693060, 110.252596, 37.385833, 175.201750, 89.670519, 70.353925]
}

df = pd.DataFrame(data)

# Menentukan variabel-variabel yang akan digambarkan
variables_to_plot = ['tenure', 'avg_num_visit', 'revenue']

# Membuat box plot
plt.figure(figsize=(10, 6))
df[variables_to_plot].boxplot()
plt.ylabel('Nilai')
plt.title('Box Plot Distribusi Variabel-Variabel')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
