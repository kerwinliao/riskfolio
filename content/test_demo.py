# test_demo.py

import pandas as pd

from riskfolio_beta.core import AttributionEngine, Portfolio

# 1️⃣ Load synthetic trade-level data
print("📥 Loading synthetic transaction data...")
df = pd.read_csv(r'C:\Users\kerwi\Documents\GitHub\riskfolio\content\fif_trades_test.csv')
print(df.head())
data = Portfolio.from_df(df)

# 2️⃣ Compute Risk-Weighted Assets (RWA)
print("\n📊 Computing RWA...")
data = AttributionEngine.compute_rwa(data)
print(data[["trade_id", "EAD", "risk_weight", "RWA"]].head())

# 3️⃣ Allocate Tangible Common Equity (TCE)
print("\n🏦 Allocating TCE (capital buffer)...")
data = AttributionEngine.allocate_tce(data, capital_ratio=0.12, equity_floor=5e8)
print(data[["trade_id", "RWA", "TCE_alloc"]].head())

# 4️⃣ Compute capital charge and Net Income
print("\n💸 Calculating capital charge & Net Income...")
data = AttributionEngine.compute_capital_charge(data, cost_of_capital=0.12)
print(data[["trade_id", "PnL", "capital_charge", "Net_Income"]].head())

# 5️⃣ Generate attribution tables
print("\n📊 Attribution by desk:")
by_desk = AttributionEngine.attribution_table(data, dims=("desk",))
print(by_desk)

print("\n📊 Attribution by product:")
by_product = AttributionEngine.attribution_table(data, dims=("product",))
print(by_product)

# 6️⃣ Compute G-SIB score (toy model)
print("\n🏦 Computing G-SIB score...")
gsib_scores = AttributionEngine.compute_gsib_toy(data)
for k, v in gsib_scores.items():
    print(f"{k:30s}: {v:.2f}")

# 7️⃣ Run a scenario: what if HY_Bond grows 15% and Repo shrinks 5%?
print("\n🔄 Running weight scenario...")
data_alt = AttributionEngine.apply_weight_scenario(data, {"HY_Bond": 1.15, "Repo": 0.95}, level="product")
by_product_alt = attribution_table(data_alt, dims=("product",))

print("\n📊 Attribution under new scenario:")
print(by_product_alt)

print("\n✅ Demo completed successfully!")