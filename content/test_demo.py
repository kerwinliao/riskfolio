# test_demo.py

import pandas as pd

from riskfolio_beta.core import AttributionEngine

# 1️⃣ Load synthetic trade-level data
print("📥 Loading synthetic transaction data...")
df = pd.read_csv(filepath)
print(df.head())

# 2️⃣ Compute Risk-Weighted Assets (RWA)
print("\n📊 Computing RWA...")
df = AttributionEngine.compute_rwa(df)
print(df[["trade_id", "EAD", "risk_weight", "RWA"]].head())

# 3️⃣ Allocate Tangible Common Equity (TCE)
print("\n🏦 Allocating TCE (capital buffer)...")
df = AttributionEngine.allocate_tce(df, capital_ratio=0.12, equity_floor=5e8)
print(df[["trade_id", "RWA", "TCE_alloc"]].head())

# 4️⃣ Compute capital charge and Net Income
print("\n💸 Calculating capital charge & Net Income...")
df = AttributionEngine.compute_capital_charge(df, cost_of_capital=0.12)
print(df[["trade_id", "PnL", "capital_charge", "Net_Income"]].head())

# 5️⃣ Generate attribution tables
print("\n📊 Attribution by desk:")
by_desk = AttributionEngine.attribution_table(df, dims=("desk",))
print(by_desk)

print("\n📊 Attribution by product:")
by_product = attribution_table(df, dims=("product",))
print(by_product)

# 6️⃣ Compute G-SIB score (toy model)
print("\n🏦 Computing G-SIB score...")
gsib_scores = AttributionEngine.compute_gsib_toy(df)
for k, v in gsib_scores.items():
    print(f"{k:30s}: {v:.2f}")

# 7️⃣ Run a scenario: what if HY_Bond grows 15% and Repo shrinks 5%?
print("\n🔄 Running weight scenario...")
df_alt = AttributionEngine.apply_weight_scenario(df, {"HY_Bond": 1.15, "Repo": 0.95}, level="product")
by_product_alt = attribution_table(df_alt, dims=("product",))

print("\n📊 Attribution under new scenario:")
print(by_product_alt)

print("\n✅ Demo completed successfully!")