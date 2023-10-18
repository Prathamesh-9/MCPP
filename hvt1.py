import pandas as pd

customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')
transactions = pd.read_csv('transactions.csv')

merged_data = pd.merge(orders, transactions, on='order_id')
merged_data = pd.merge(merged_data, customers, on='customer_id')

hvt = merged_data[merged_data['sales']>250]

from datetime import datetime as dt
hvt['order_month'] = pd.to_datetime(hvt['order_purchase_date'].str.strip()).dt.month
hvt['order_year'] = pd.to_datetime(hvt['order_purchase_date'].str.strip()).dt.year

hvt_new = hvt.groupby(by=['order_month','order_year'])['order_id'].size()

print(hvt_new)
