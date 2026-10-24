import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_selection import SelectKBest, chi2

df = pd.DataFrame({
    "income": [2000, 5000, 3000, 8000, 12000, 4000, 7000, 9000],
    "employment": ["Unemployed", "Employed", "Self", "Employed", "Self", "Employed", "Self", "Employed"],
    "credit_score": [300, 600, 450, 750, 800, 500, 700, 720],
    "loan_amount": [10000, 20000, 15000, 25000, 30000, 12000, 22000, 27000],
    "marital_status": ["Single", "Married", "Single", "Married", "Married", "Single", "Married", "Married"],
    "approved": [0, 1, 0, 1, 1, 0, 1, 1]
})

df["income"] = df["income"].fillna(df["income"].mean())
df["credit_score"] = df["credit_score"].fillna(df["credit_score"].mean())
df["loan_amount"] = df["loan_amount"].fillna(df["loan_amount"].mean())

le_emp = LabelEncoder()
le_mar = LabelEncoder()

df["employment"] = le_emp.fit_transform(df["employment"])
df["marital_status"] = le_mar.fit_transform(df["marital_status"])

X = df.drop("approved", axis=1)
y = df["approved"]

selector = SelectKBest(score_func=chi2, k=3)
X_new = selector.fit_transform(X, y)

X_train, X_test, y_train, y_test = train_test_split(
    X_new, y, test_size=0.25, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

new_applicant = pd.DataFrame([{
    "income": 6000,
    "employment": le_emp.transform(["Employed"])[0],
    "credit_score": 680,
    "loan_amount": 18000,
    "marital_status": le_mar.transform(["Married"])[0]
}])

new_applicant = selector.transform(new_applicant)

prediction = model.predict(new_applicant)

print("Loan Approved (1 = Yes, 0 = No):", prediction[0])
