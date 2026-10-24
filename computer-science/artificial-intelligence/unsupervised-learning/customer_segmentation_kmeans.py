import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("customers.csv")

if "customer_id" in data.columns:
    data = data.drop("customer_id", axis=1)

k1 = KMeans(n_clusters=3, random_state=0)
data["cluster_no_scaling"] = k1.fit_predict(data)

data_scaled = data.drop("cluster_no_scaling", axis=1).copy()

cols = [c for c in data_scaled.columns if c != "age"]

scaler = StandardScaler()
data_scaled[cols] = scaler.fit_transform(data_scaled[cols])

k2 = KMeans(n_clusters=3, random_state=0)
data["cluster_with_scaling"] = k2.fit_predict(data_scaled)

print(data.head())
print(data["cluster_no_scaling"].value_counts())
print(data["cluster_with_scaling"].value_counts())
