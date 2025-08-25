import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_expenses, save_expense, get_summary
from datetime import date

st.title("💰 Personal Expense Tracker")

# --- Add Expense ---
st.header("Add Expense")
with st.form("expense_form"):
    exp_date = st.date_input("Date", value=date.today())
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Entertainment", "Bills", "Other"])
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    description = st.text_input("Description")
    submitted = st.form_submit_button("Add Expense")
    
    if submitted:
        expense = {
            "Date": exp_date,
            "Category": category,
            "Amount": amount,
            "Description": description
        }
        save_expense(expense)
        st.success("Expense added successfully!")

# --- View Expenses ---
st.header("Your Expenses")
df = load_expenses()
st.dataframe(df.sort_values(by="Date", ascending=False))

# --- Expense Summary ---
st.header("Expense Summary")
summary = get_summary(df)
st.bar_chart(summary)

# --- Optional: Pie chart ---
st.subheader("Spending by Category")
fig = px.pie(df, names='Category', values='Amount', title='Expenses by Category')
st.plotly_chart(fig)

# --- Download Expenses ---
st.header("Export Data")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Expenses as CSV",
    data=csv,
    file_name='expenses.csv',
    mime='text/csv',
)

