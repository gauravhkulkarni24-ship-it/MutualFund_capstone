
import pandas as pd
import numpy as np
import os
import json
from datetime import datetime

RAW_DIR = 'data/raw'
CSV_FILES = {
    'fund_master'          : f'{RAW_DIR}/01_fund_master.csv',
    'nav_history'          : f'{RAW_DIR}/02_nav_history.csv',
    'aum_by_fund_house'    : f'{RAW_DIR}/03_aum_by_fund_house.csv',
    'monthly_sip_inflows'  : f'{RAW_DIR}/04_monthly_sip_inflows.csv',
    'category_inflows'     : f'{RAW_DIR}/05_category_inflows.csv',
    'industry_folio_count' : f'{RAW_DIR}/06_industry_folio_count.csv',
    'scheme_performance'   : f'{RAW_DIR}/07_scheme_performance.csv',
    'investor_transactions': f'{RAW_DIR}/08_investor_transactions.csv',
    'portfolio_holdings'   : f'{RAW_DIR}/09_portfolio_holdings.csv',
    'benchmark_indices'    : f'{RAW_DIR}/10_benchmark_indices.csv',
}

def load_and_inspect(csv_map):
    datasets  = {}
    anomalies = []
    print('=' * 60)
    print('DAY 1 - LOADING ALL 10 DATASETS')
    print('=' * 60)
    for name, path in csv_map.items():
        if not os.path.exists(path):
            print(f'MISSING: {path}')
            continue
        df = pd.read_csv(path)
        datasets[name] = df
        print(f'\n{name.upper()}')
        print(f'  Shape   : {df.shape}')
        print(f'  Columns : {df.columns.tolist()}')
        print(f'  Head    :\n{df.head(3)}')
        nulls = df.isnull().sum()
        if nulls.any():
            anomalies.append(f'{name}: nulls in {nulls[nulls>0].index.tolist()}')
    return datasets, anomalies

def explore_fund_master(df):
    print('\nFUND MASTER EXPLORATION')
    print(f'Total Schemes : {len(df)}')
    print(f'Fund Houses   : {df["fund_house"].nunique()}')
    print(df['fund_house'].value_counts().to_string())
    print(df['category'].value_counts().to_string())
    print(df['risk_category'].value_counts().to_string())

def validate_amfi_codes(fund_master, nav_history):
    master_codes = set(fund_master['amfi_code'].astype(str))
    nav_codes    = set(nav_history['amfi_code'].astype(str))
    matched      = master_codes & nav_codes
    coverage     = len(matched) / len(master_codes) * 100
    print(f'\nAMFI CODE VALIDATION')
    print(f'Master codes : {len(master_codes)}')
    print(f'NAV codes    : {len(nav_codes)}')
    print(f'Matched      : {len(matched)}')
    print(f'Coverage     : {coverage:.1f}%')
    print(f'Verdict      : PASS' if coverage == 100 else f'Verdict : WARN')

if __name__ == '__main__':
    datasets, anomalies = load_and_inspect(CSV_FILES)
    if 'fund_master' in datasets:
        explore_fund_master(datasets['fund_master'])
    if 'fund_master' in datasets and 'nav_history' in datasets:
        validate_amfi_codes(datasets['fund_master'], datasets['nav_history'])
    print('\nAnomalies:', anomalies)
    print('\nDay 1 complete!')
