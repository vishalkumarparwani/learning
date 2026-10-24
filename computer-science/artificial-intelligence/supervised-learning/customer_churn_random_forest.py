import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

df = pd.DataFrame({
    "monthly_charges": [20, 80, 50, 100, 30, 90, 60, 70, 40, 85],
    "contract": ["Month-to-month", "Two year", "One year", "Month-to-month", "One year",
                 "Two year", "Month-to-month", "One year", "Month-to-month", "Two year"],
    "tenure": [1, 24, 12, 3, 10, 36, 5, 18, 2, 30],
    "internet_service": ["DSL", "Fiber", "DSL", "Fiber", "DSL",
                         "Fiber", "DSL", "Fiber", "DSL", "Fiber"],
    "support_calls": [5, 1, 2, 6, 3, 1, 4, 2, 5, 1],
    "churn": [1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
})

le_contract = LabelEncoder()
le_internet = LabelEncoder()

df["contract"] = le_contract.fit_transform(df["contract"])
df["internet_service"] = le_internet.fit_transform(df["internet_service"])

X = df.drop("churn", axis=1)
y = df["churn"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=1))
print("Recall:", recall_score(y_test, y_pred, zero_division=1))
print("F1 Score:", f1_score(y_test, y_pred, zero_division=1))

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nFeature Importance:\n", importance)

new_customer = pd.DataFrame([{
    "monthly_charges": 85,
    "contract": le_contract.transform(["Month-to-month"])[0],
    "tenure": 2,
    "internet_service": le_internet.transform(["Fiber"])[0],
    "support_calls": 5
}])

new_customer_scaled = scaler.transform(new_customer)

print("\nChurn Prediction (1 = Yes, 0 = No):",
      model.predict(new_customer_scaled)[0])
