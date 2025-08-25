import pandas as pd
import os

DATA_FILE = "data/expenses.csv"

def load_expenses():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE, parse_dates=['Date'])
    else:
        return pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

def save_expense(expense):
    df = load_expenses()
    df = pd.concat([df, pd.DataFrame([expense])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

def get_summary(df):
    summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    return summary
