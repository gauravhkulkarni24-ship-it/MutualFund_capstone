-- Bluestock Fintech - 10 Analytical SQL Queries

-- Q1: Top 5 funds by AUM
SELECT scheme_name, fund_house, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC LIMIT 5;

-- Q2: Average NAV per month per fund
SELECT amfi_code,
       strftime('%Y-%m', date) AS month,
       ROUND(AVG(nav), 4)      AS avg_nav
FROM fact_nav
GROUP BY amfi_code, month
ORDER BY amfi_code, month;

-- Q3: SIP inflow YoY growth
SELECT month, sip_inflow_crore, yoy_growth_pct
FROM fact_sip
ORDER BY month;

-- Q4: Total transaction amount by state
SELECT state,
       COUNT(*)        AS num_transactions,
       SUM(amount_inr) AS total_amount
FROM fact_transactions ft
JOIN dim_investor di ON ft.investor_id = di.investor_id
GROUP BY state
ORDER BY total_amount DESC;

-- Q5: Funds with expense ratio less than 1 percent
SELECT amfi_code, scheme_name, fund_house, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct;

-- Q6: Top 5 funds by Sharpe Ratio
SELECT scheme_name, fund_house, sharpe_ratio, sortino_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC LIMIT 5;

-- Q7: Monthly transaction count by type
SELECT strftime('%Y-%m', transaction_date) AS month,
       transaction_type,
       COUNT(*)                             AS count,
       SUM(amount_inr)                     AS total_amount
FROM fact_transactions
GROUP BY month, transaction_type
ORDER BY month;

-- Q8: Benchmark index total return
SELECT index_name,
       MIN(close_value) AS start_value,
       MAX(close_value) AS peak_value,
       ROUND((MAX(close_value) - MIN(close_value))
             / MIN(close_value) * 100, 2) AS total_return_pct
FROM fact_benchmark
GROUP BY index_name;

-- Q9: Sector allocation across all funds
SELECT sector,
       ROUND(SUM(weight_pct), 2)     AS total_weight,
       ROUND(AVG(weight_pct), 2)     AS avg_weight,
       COUNT(DISTINCT amfi_code)     AS num_funds
FROM fact_holdings
GROUP BY sector
ORDER BY total_weight DESC;

-- Q10: SIP amount by age group
SELECT age_group,
       COUNT(*)                  AS num_transactions,
       ROUND(AVG(amount_inr), 2) AS avg_sip_amount,
       SUM(amount_inr)           AS total_invested
FROM fact_transactions ft
JOIN dim_investor di ON ft.investor_id = di.investor_id
WHERE ft.transaction_type = 'Sip'
GROUP BY age_group
ORDER BY avg_sip_amount DESC;
