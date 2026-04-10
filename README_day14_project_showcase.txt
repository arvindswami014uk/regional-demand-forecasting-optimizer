# Regional Demand Forecasting and Inventory Placement Optimizer

Amazon-inspired supply chain analytics capstone combining forecasting, inventory placement, and operations decision support.

## Project Overview
This project simulates how a network planning team can forecast demand at the SKU-region level and convert those forecasts into inventory placement decisions across a fulfillment network.

It is designed around a practical operations question: how do you improve service levels and delivery reliability without blindly increasing inventory or transfer cost?

## Business Problem
Poor regional demand prediction creates stockouts, emergency transfers, inventory imbalance, and missed delivery promises. Leaders need a disciplined decision system that connects forecasting quality to inventory policy and placement strategy.

## What This Project Does
- Forecasts regional demand at SKU-region level
- Benchmarks baseline and advanced forecasting approaches
- Converts forecast behavior into safety stock and reorder policy logic
- Evaluates service, cost, and sustainability trade-offs
- Recommends a final constrained network strategy for decision-makers

## Methodology
### 1. Forecasting
- Prepared processed demand history at SKU-region level
- Benchmarked baseline moving average against Prophet and XGBoost
- Selected the best model using weighted error comparison

### 2. Inventory Policy
- Calculated safety stock and reorder points
- Flagged urgency and days-of-supply risk
- Built policy-oriented placement logic rather than black-box optimization only

### 3. Strategy Evaluation
- Compared service, cost, and carbon proxy scenarios
- Distinguished unconstrained scenario insight from constrained final recommendation
- Preserved governance note that carbon is a synthetic comparative proxy

## Key Results
- Best forecasting model: **XGBoost**
- XGBoost WMAPE: **11.06%**
- Prophet WMAPE: **11.16%**
- MA7 baseline WMAPE: **19.25%**
- Improvement vs baseline: **42.5%**
- Top feature: **roll_14_mean (0.4682)**
- Weakest forecast segment: **West region**
- Weakest category: **Beauty**

## Inventory Results
- Safety stock value: **\$157,292.60**
- Annual storage cost: **\$21,370.33**
- Replenishment needed: **\$780,850.78**
- High urgency combinations: **41**
- Average days of supply: **6.3**
- Critical combinations: **0**
- Total combinations evaluated: **125**

## Final Recommendation
- **Forecasting recommendation:** Use XGBoost as the production-oriented forecasting approach.
- **Inventory recommendation:** Use policy-based safety stock and reorder point logic as the operating control layer.
- **Strategy insight:** Carbon-first was the strongest unconstrained sustainability scenario in the synthetic network proxy.
- **Final constrained recommendation:** Balanced is the recommended strategy under practical decision rules and feasibility constraints.

## Why Carbon-first and Balanced Are Both True
- Carbon-first performed best in unconstrained comparative scenario analysis.
- Balanced became the final recommendation after capacity, feasibility, and operating realism constraints were applied.
- This is not a contradiction. It reflects the difference between theoretical frontier performance and deployable operating policy.

## Governance and Limitations
- Carbon metric is a **synthetic comparative proxy** for planning and scenario discussion.
- It should **not** be used for formal ESG disclosure.
- Planner overrides and KPI monitoring remain necessary.
- Project source grounding is based on preserved source and processed tables currently available in the repo, not on missing raw-package folders.

## Recommended Reviewer Path
1. Read the executive summary and submission notes
2. Review benchmark outputs and key charts
3. Inspect inventory policy tables and strategy outputs
4. Use the artifact map to connect technical files to business meaning

## Key Visuals
- Forecast model comparison dashboard
- Feature importance chart
- Inventory dashboard and safety stock heatmap
- Strategy scorecard and constrained executive dashboard

## Folder Guide
- `B_Dataset/` → preserved source and processed project tables
- `data/processed/` → modeling-ready processed datasets
- `models/` → forecasts, inventory logic, optimization outputs
- `outputs/benchmarks/` → evaluation tables and strategy scorecards
- `outputs/charts/` → business visuals for review and presentation
- `reports/` → executive, presentation, and technical delivery assets

## Skills Demonstrated
- Demand forecasting
- Time-series feature engineering
- Inventory policy design
- Supply chain strategy analysis
- Executive storytelling
- Portfolio-grade documentation

## Why This Matters
The project shows how analytics becomes operational decision support: not just a better forecast, but a better network decision under trade-offs, constraints, and governance realities.