import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

df = pd.DataFrame({
    "study_hours": [2, 4, 6, 8, 10],
    "attendance": [60, 70, 75, 85, 95],
    "previous_grade": [55, 60, 65, 80, 90],
    "participation": ["Low", "Medium", "Medium", "High", "High"],
    "internet_usage": ["High", "Low", "Low", "Low", "High"],
    "final_score": [50, 60, 70, 85, 95]
})

df["study_hours"] = df["study_hours"].fillna(df["study_hours"].mean())
df["attendance"] = df["attendance"].fillna(df["attendance"].mean())

le1 = LabelEncoder()
le2 = LabelEncoder()

df["participation"] = le1.fit_transform(df["participation"])
df["internet_usage"] = le2.fit_transform(df["internet_usage"])

X = df.drop("final_score", axis=1)
y = df["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

if len(y_test) > 1:
    r2 = r2_score(y_test, y_pred)
else:
    r2 = "Not defined (need more test samples)"

print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)

importance = pd.Series(model.coef_, index=X.columns)
print("\nFeature Importance:\n", importance.sort_values(ascending=False))

new_student = pd.DataFrame([{
    "study_hours": 7,
    "attendance": 80,
    "previous_grade": 75,
    "participation": le1.transform(["High"])[0],
    "internet_usage": le2.transform(["Low"])[0]
}])

prediction = model.predict(new_student)

print("\nPredicted Final Score:", prediction[0])
