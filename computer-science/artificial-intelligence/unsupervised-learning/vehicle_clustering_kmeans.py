import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df, columns=["vehicle_type"])

k1 = KMeans(n_clusters=3, random_state=0)
df["cluster_no_scaling"] = k1.fit_predict(df_encoded)

scaler = StandardScaler()
df_scaled = df_encoded.copy()
df_scaled = pd.DataFrame(scaler.fit_transform(df_scaled), columns=df_scaled.columns)

k2 = KMeans(n_clusters=3, random_state=0)
df["cluster_with_scaling"] = k2.fit_predict(df_scaled)

print(df)
