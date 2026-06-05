
import pandas as pd
import numpy as np
import sqlite3
import os
from sqlalchemy import create_engine

RAW_DIR       = 'data/raw'
PROCESSED_DIR = 'data/processed'
DB_PATH       = 'data/db/bluestock_mf.db'

os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs('data/db', exist_ok=True)

engine = create_engine(f'sqlite:///{DB_PATH}')

def clean_and_load():
    print('DAY 2 - ETL PIPELINE')

    # Fund Master
    df = pd.read_csv(f'{RAW_DIR}/01_fund_master.csv')
    df['launch_date'] = pd.to_datetime(df['launch_date'], errors='coerce')
    df.to_csv(f'{PROCESSED_DIR}/01_fund_master_clean.csv', index=False)
    df.to_sql('dim_fund', engine, if_exists='replace', index=False)
    print(f'dim_fund : {len(df)} rows')

    # NAV History
    df = pd.read_csv(f'{RAW_DIR}/02_nav_history.csv')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['nav']  = pd.to_numeric(df['nav'], errors='coerce')
    df.dropna(subset=['date','nav'], inplace=True)
    df = df[df['nav'] > 0]
    df['daily_return_pct'] = df.groupby('amfi_code')['nav'].pct_change() * 100
    df.to_csv(f'{PROCESSED_DIR}/02_nav_history_clean.csv', index=False)
    df.to_sql('fact_nav', engine, if_exists='replace', index=False)
    print(f'fact_nav : {len(df)} rows')

    # Transactions
    df = pd.read_csv(f'{RAW_DIR}/08_investor_transactions.csv')
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
    df['amount_inr']       = pd.to_numeric(df['amount_inr'], errors='coerce')
    df = df[df['amount_inr'] > 0]
    df.to_csv(f'{PROCESSED_DIR}/08_transactions_clean.csv', index=False)
    df.to_sql('fact_transactions', engine, if_exists='replace', index=False)
    print(f'fact_transactions : {len(df)} rows')

    print('ETL complete!')
    print(f'Database : {DB_PATH}')

if __name__ == '__main__':
    clean_and_load()
