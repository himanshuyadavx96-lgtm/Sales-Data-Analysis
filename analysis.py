import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

product_sales = df.groupby("Product")["Sales"].sum()
print(product_sales)

product_sales.plot(kind="bar")
plt.title("Product Wise Sales")
plt.show()
