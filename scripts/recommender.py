
import pandas as pd

def recommend_funds(risk_appetite, df_score, df_fund, top_n=3):
    risk_map = {
        "Low"       : ["Low"],
        "Moderate"  : ["Moderate","Low"],
        "High"      : ["High","Moderately High","Moderate"],
        "Very High" : ["Very High","High","Moderately High"],
    }
    allowed  = risk_map.get(risk_appetite, ["Moderate"])
    filtered = df_score[df_score["amfi_code"].isin(
        df_fund[df_fund["risk_category"].isin(allowed)]["amfi_code"]
    )].copy()
    filtered = filtered.merge(
        df_fund[["amfi_code","risk_category","fund_manager","sub_category"]],
        on="amfi_code", how="left")
    cols = ["scheme_name","fund_house","sub_category",
            "sharpe_ratio","cagr_3y_pct","composite_score",
            "risk_category","fund_manager"]
    if "expense_ratio_pct" in filtered.columns:
        cols.append("expense_ratio_pct")
    return filtered.nlargest(top_n, "sharpe_ratio")[cols]

if __name__ == "__main__":
    PROC     = "bluestock/data/processed"
    df_score = pd.read_csv(f"{PROC}/fund_scorecard.csv")
    df_fund  = pd.read_csv(f"{PROC}/01_fund_master_clean.csv")
    risk     = input("Enter risk appetite (Low/Moderate/High/Very High): ")
    print(recommend_funds(risk, df_score, df_fund).to_string(index=False))
