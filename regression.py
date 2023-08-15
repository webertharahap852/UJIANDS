import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Membaca data dari file JSON
with open('raw.json', 'r') as json_file:
    raw_data = json.load(json_file)

# Membuat DataFrame dari data JSON
data = pd.DataFrame(raw_data)

# Mengisi nilai yang hilang dengan rata-rata kolom 'employee'
mean_employee = data['employee'].mean()
data['employee'].fillna(mean_employee, inplace=True)

# Memilih fitur dan target
features = ['tenure', 'employee', 'avg_num_visit', 'avg_promotion',
            'avg_sales_call_duration', 'avg_visit_duration']
target = 'revenue'

X = data[features]
y = data[target]

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Membuat model Regresi Linier
model = LinearRegression()

# Melatih model pada data latih
model.fit(X_train, y_train)

# Membuat prediksi pada data uji
y_pred = model.predict(X_test)

# Evaluasi model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
