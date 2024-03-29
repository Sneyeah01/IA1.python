# -*- coding: utf-8 -*-
"""LVADSUSR120_snehaO_FA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SbWEy_Ta_DC5_u3O2ixf1iVikgUszdEL
"""

#Q1
import pandas as pd
df = pd.read_excel('/content/Walmart_Dataset Python_Final_Assessment.xlsx')
print(df.info())
print(df.describe())

#Q2
print(df.isnull().sum())
#there are no missing values in the data
df.drop_duplicates(inplace=True)

#Q3
print("Mean: Sales \n", df['Sales'].mean())
print("Median: Sales \n", df['Sales'].median())
print("Mode: Sales \n", df['Sales'].mode())
print("Range: Sales \n", df['Sales'].max() - df['Sales'].min())
print("Variance: Sales \n", df['Sales'].var())
print("Standard Deviation: Sales \n", df['Sales'].std())
print("Mean: Quantity \n", df['Quantity'].mean())
print("Median: Quantity \n", df['Quantity'].median())
print("Mode: Quantity \n", df['Quantity'].mode())
print("Range: Quantity \n", df['Quantity'].max() - df['Quantity'].min())
print("Variance: Quantity \n", df['Quantity'].var())
print("Standard Deviation: Quantity \n", df['Quantity'].std())
print("Mean: Profit \n", df['Profit'].mean())
print("Median: Profit \n", df['Profit'].median())
print("Mode: Profit \n", df['Profit'].mode())
print("Range: Profit \n", df['Profit'].max() - df['Profit'].min())
print("Variance: Profit \n", df['Profit'].var())
print("Standard Profit: Profit \n", df['Profit'].std())

#Q4
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Order Year'] = pd.to_datetime(df['Order Date']).dt.year


salesData = df.groupby('Order Year')['Sales'].sum()
salesData.plot(label='Sales')
profitData = df.groupby('Order Year')['Profit'].sum()
profitData.plot(label='Profit')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Category', y='Sales', data=df)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Quantity', y='Profit', data=df)
plt.title('Profit vs Quantity')
plt.xlabel('Quantity')
plt.ylabel('Profit')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Profit', data=df)
plt.title('Profit Distribution')
plt.xlabel('Profit')
plt.tight_layout()
plt.show()

#Q5
df = pd.read_excel('/content/Walmart_Dataset Python_Final_Assessment.xlsx')
correlation= df.corr()
print(correlation)

#6
numeric_cols = ['Sales', 'Quantity', 'Profit']
df_zscores = df[numeric_cols].apply(lambda x: np.abs((x - x.mean()) / x.std()))

outliers = df_zscores > 3

outliers_data = df[outliers.any(axis=1)]

print(" The Outliers are:")
print(outliers_data)

plt.figure(figsize=(15, 6))
sns.boxplot(data=df[numeric_cols])
plt.title('Boxplot of Sales, Quantity, and Profit')
plt.xlabel('Features')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""### There is a growth or increase in both sales and profit in the month of march alone and there is a low/dip in sales in the month of june and october. overall,sales and the profit increases the same throughout the year"""

#Q7 - Trend Analysis

df['Order Month'] = pd.to_datetime(df['Order Date']).dt.month
salesData = df.groupby('Order Year')['Sales'].sum()
salesData.plot(label='Sales')
profitData = df.groupby('Order Year')['Profit'].sum()
profitData.plot(label='Profit')
plt.grid(True)
plt.legend()
plt.show()

salesData = df.groupby('Order Month')['Sales'].sum()
salesData.plot(label='Sales')
profitData = df.groupby('Order Month')['Profit'].sum()
profitData.plot(label='Profit')
plt.grid(True)
plt.legend()
plt.show()

# ii)
total_sales = df.groupby(['Order Year', 'Category'])['Sales'].sum().reset_index()
total_sales['Growth'] = total_sales.groupby('Category')['Sales'].pct_change() * 100
most_growth_category = total_sales.groupby('Category')['Growth'].mean().idxmax()
print("Category with the Most Growth in Sales:", most_growth_category)

#Q7 Customer Analysis

summary = df.groupby('EmailID').agg({'Order ID': 'nunique', 'Sales': 'sum'}).reset_index()
summary.columns = ['EmailID', 'Quantity', 'TotalSales']

top_customers_by_orders = summary.nlargest(5, 'Quantity')
top_customers_by_sales = summary.nlargest(5, 'TotalSales')

print("Top 5 Customers of Orders Placed:")
print(top_customers_by_orders.set_index('EmailID'))
print("Top 5 Customers of Total Sales:")
print(top_customers_by_sales.set_index('EmailID'))

"""Insights : Here it is clear that the Customers who spend more usually spend them on less number of products and also the customers who tend to buy more usually spend less on the product."""

#Q7- Customer Analysis
#ii)
df['OrderDate'] = pd.to_datetime(df['Order Date'])
df.sort_values(by=['EmailID', 'Order Date'], inplace=True)
df['TimeBetweenOrders'] = df.groupby('EmailID')['Order Date'].diff()
averagetime_btw_orders = df.groupby('EmailID')['TimeBetweenOrders'].mean()

print("The Average Time Between Orders for Each Customer is:")
print(averagetime_btw_orders)
print(averagetime_btw_orders.mean())

"""#Comprehensive Analysis:"""

#average Time between order and delivery
df['TimeBetweenOrderAndDelivery'] = df['Ship Date'] - df['Order Date']
average_time_between_order_and_delivery = df.groupby('Category')['TimeBetweenOrderAndDelivery'].mean()
print(average_time_between_order_and_delivery)

df['TimeBetweenOrderAndDelivery'] = df['Ship Date'] - df['Order Date']
average_time_between_order_and_delivery = df.groupby('EmailID')['TimeBetweenOrderAndDelivery'].mean()
print(average_time_between_order_and_delivery.mean())

"""#### i) From the datas,  the average time taken for the shipment of an order is 8 days and 20 hours.It stands highest for Tables delivery . Bigger trucks with more space can be used to improve the overall suppy chain betterment.

#### ii) The geographic distribution of sales is DEFINED  by factors such as Age and income and the cultural preferences, economic conditions and also local requirements. overall it can be improved by marketing which enables businesses to tailor products, pricing, promotions, and advertising strategies to specific regions, demographics, and consumer behaviors which indeed improves sales performance and customer engagement.
"""

order_amounts = df.groupby('EmailID')['Sales'].sum().reset_index()

top10 = int(len(order_amounts) * 0.1)
high_value_customers = order_amounts.nlargest(top10, 'Sales')
print(high_value_customers)

order_amounts = df.groupby('EmailID')['Quantity'].sum().reset_index()

top10p= int(len(order_amounts) * 0.1)
high_value_customers = order_amounts.nlargest(top10, 'Quantity')
print(high_value_customers)

for index, customer in high_value_customers.iterrows():
  pass

"""### iii) Finally the we can indentify the High value customers by their purchasing quantity, purchase frequency and their purchase amount . These customers can be given additional promotions and offers to retain and improve the customer loyalty and business improvement and recommendations"""

