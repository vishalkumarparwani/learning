import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
data = pd.read_csv("train.csv")
print(data.head())
print(data.shape)
print(data.columns)
num = data.select_dtypes(include=np.number).columns
cat = data.select_dtypes(exclude=np.number).columns
print(num)
print(cat)
print(data.isnull().sum())
for i in num:
    data[i].fillna(data[i].median(), inplace=True)
for i in cat:
    data[i].fillna(data[i].mode()[0], inplace=True)
data = data.loc[:, data.isnull().mean() < 0.5]
plt.hist(data["SalePrice"])
plt.show()
plt.boxplot(data["SalePrice"])
plt.show()
plt.hist(data["GrLivArea"])
plt.show()
plt.boxplot(data["GrLivArea"])
plt.show()
corr = data.corr(numeric_only=True)
print(corr["SalePrice"].sort_values(ascending=False))
plt.scatter(data["GrLivArea"], data["SalePrice"])
plt.show()
data.groupby("OverallQual")["SalePrice"].mean().plot(kind="bar")
plt.show()
import seaborn as sns
sns.heatmap(corr, cmap="coolwarm")
plt.show()
data["HouseAge"] = data["YrSold"] - data["YearBuilt"]
if "Id" in data.columns:
    data.drop("Id", axis=1, inplace=True)
data = pd.get_dummies(data, drop_first=True)
X = data.drop("SalePrice", axis=1)
y = data["SalePrice"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
print("R2:", r2_score(y_test, pred))
