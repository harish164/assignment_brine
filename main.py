# main.py

import csv
from collections import defaultdict
from datetime import datetime
from operator import itemgetter

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def compute_monthly_revenue(orders):
    monthly_revenue = defaultdict(float)
    for order in orders:
        order_date = datetime.strptime(order['order_date'], '%Y-%m-%d')
        month_year = order_date.strftime('%Y-%m')
        monthly_revenue[month_year] += float(order['product_price']) * int(order['quantity'])
    return monthly_revenue

def compute_product_revenue(orders):
    product_revenue = defaultdict(float)
    for order in orders:
        product_revenue[order['product_name']] += float(order['product_price']) * int(order['quantity'])
    return product_revenue

def compute_customer_revenue(orders):
    customer_revenue = defaultdict(float)
    for order in orders:
        customer_revenue[order['customer_id']] += float(order['product_price']) * int(order['quantity'])
    return customer_revenue

def top_n_customers_by_revenue(customer_revenue, n=10):
    sorted_customers = sorted(customer_revenue.items(), key=itemgetter(1), reverse=True)
    return sorted_customers[:n]

if __name__ == "__main__":
    orders_data = read_csv('orders.csv')

    monthly_revenue = compute_monthly_revenue(orders_data)
    print("Monthly Revenue:", monthly_revenue)

    product_revenue = compute_product_revenue(orders_data)
    print("Product Revenue:", product_revenue)

    customer_revenue = compute_customer_revenue(orders_data)
    print("Customer Revenue:", customer_revenue)

    top_customers = top_n_customers_by_revenue(customer_revenue)
    print("Top 10 Customers by Revenue:", top_customers)
