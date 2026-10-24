import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

X = df[["GPA", "study_hours", "attendance_rate"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []
for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state=0)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

plt.plot(range(2,7), wcss, marker='o')
plt.xlabel("K")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

k_opt = 3

kmeans = KMeans(n_clusters=k_opt, random_state=0)
df["cluster"] = kmeans.fit_predict(X_scaled)

plt.scatter(df["study_hours"], df["GPA"], c=df["cluster"])
plt.xlabel("Study Hours")
plt.ylabel("GPA")
plt.title("Student Clusters")
plt.show()

print(df[["student_id", "cluster"]])
