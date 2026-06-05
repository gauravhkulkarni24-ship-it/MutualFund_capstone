-- Bluestock Fintech MF Analytics Star Schema
-- Day 2

CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code           INTEGER PRIMARY KEY,
    fund_house          TEXT,
    scheme_name         TEXT,
    category            TEXT,
    sub_category        TEXT,
    plan                TEXT,
    launch_date         TEXT,
    benchmark           TEXT,
    expense_ratio_pct   REAL,
    exit_load_pct       REAL,
    fund_manager        TEXT,
    risk_category       TEXT
);

CREATE TABLE IF NOT EXISTS dim_investor (
    investor_id         TEXT PRIMARY KEY,
    state               TEXT,
    city                TEXT,
    city_tier           TEXT,
    age_group           TEXT,
    gender              TEXT,
    annual_income_lakh  REAL
);

CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id              INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code           INTEGER,
    date                TEXT,
    nav                 REAL,
    daily_return_pct    REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    txn_id              INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id         TEXT,
    amfi_code           INTEGER,
    transaction_date    TEXT,
    transaction_type    TEXT,
    amount_inr          INTEGER,
    payment_mode        TEXT,
    kyc_status          TEXT,
    FOREIGN KEY (investor_id) REFERENCES dim_investor(investor_id),
    FOREIGN KEY (amfi_code)   REFERENCES dim_fund(amfi_code)
);

CREATE TABLE IF NOT EXISTS fact_performance (
    perf_id             INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code           INTEGER,
    return_1yr_pct      REAL,
    return_3yr_pct      REAL,
    return_5yr_pct      REAL,
    sharpe_ratio        REAL,
    sortino_ratio       REAL,
    beta                REAL,
    alpha               REAL,
    max_drawdown_pct    REAL,
    std_dev_ann_pct     REAL,
    aum_crore           INTEGER,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE IF NOT EXISTS fact_aum (
    aum_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date            TEXT,
    fund_house      TEXT,
    aum_lakh_crore  REAL,
    aum_crore       INTEGER,
    num_schemes     INTEGER
);

CREATE TABLE IF NOT EXISTS fact_sip (
    sip_id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    month                     TEXT,
    sip_inflow_crore          INTEGER,
    active_sip_accounts_crore REAL,
    new_sip_accounts_lakh     REAL,
    sip_aum_lakh_crore        REAL,
    yoy_growth_pct            REAL
);

-- INDEXES
CREATE INDEX IF NOT EXISTS idx_nav_code  ON fact_nav(amfi_code);
CREATE INDEX IF NOT EXISTS idx_nav_date  ON fact_nav(date);
CREATE INDEX IF NOT EXISTS idx_txn_code  ON fact_transactions(amfi_code);
CREATE INDEX IF NOT EXISTS idx_txn_date  ON fact_transactions(transaction_date);
