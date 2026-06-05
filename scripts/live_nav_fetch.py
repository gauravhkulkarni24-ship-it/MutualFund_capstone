
import requests
import pandas as pd
import os

RAW_DIR = 'data/raw'
os.makedirs(RAW_DIR, exist_ok=True)

SCHEMES = {
    125497: 'HDFC_Top100_Direct',
    119551: 'SBI_Bluechip',
    120503: 'ICICI_Bluechip',
    118632: 'Nippon_LargeCap',
    119092: 'Axis_Bluechip',
    120841: 'Kotak_Bluechip',
}

def fetch_all():
    print('LIVE NAV FETCH - mfapi.in')
    all_dfs = []
    for code, name in SCHEMES.items():
        print(f'Fetching {name} ({code})...', end=' ')
        try:
            r    = requests.get(f'https://api.mfapi.in/mf/{code}', timeout=15)
            data = r.json()
            df   = pd.DataFrame(data['data'])
            df['amfi_code']   = code
            df['scheme_name'] = data['meta']['scheme_name']
            df['fund_house']  = data['meta']['fund_house']
            df.to_csv(f'{RAW_DIR}/nav_live_{code}.csv', index=False)
            all_dfs.append(df)
            print(f'Done - {len(df)} records')
        except Exception as e:
            print(f'Error: {e}')
    if all_dfs:
        combined = pd.concat(all_dfs, ignore_index=True)
        combined.to_csv(f'{RAW_DIR}/nav_live_combined.csv', index=False)
        print(f'Combined saved - {len(combined)} total rows')

if __name__ == '__main__':
    fetch_all()
