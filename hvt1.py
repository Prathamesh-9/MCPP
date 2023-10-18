import pandas as pd

customers = pd.read_csv(r'C:\Users\Administrator\Desktop\MC GIT\MCPP\customers.csv')
orders = pd.read_csv(r'C:\Users\Administrator\Desktop\MC GIT\MCPP\orders.csv')
transactions = pd.read_csv(r'C:\Users\Administrator\Desktop\MC GIT\MCPP\transactions.csv')

merged_data = pd.merge(orders, transactions, on='order_id')
merged_data = pd.merge(merged_data, customers, on='customer_id')

hvt = merged_data[merged_data['sales']>150]
hvt_by_oc = hvt.groupby(by=['order_id','customer_name'])
print(hvt_by_oc[['order_id','customer_name']].head())

