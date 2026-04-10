Day 13 Reviewer Guide — Regional Demand Forecasting + Inventory Optimization

What this project does
This project builds an end-to-end planning workflow that connects regional demand forecasting to inventory policy and strategic fulfillment decision-making.

Recommended review order
1. reports/executive/day13_executive_memo.txt
2. reports/executive/day13_board_memo.txt
3. reports/presentation/day13_slide_builder.csv
4. outputs/benchmarks/overall_accuracy.csv
5. models/ml/model_comparison_all.csv
6. models/inventory/inventory_policy_table.csv
7. outputs/benchmarks/day11_5_executive_scorecard_v2.csv
8. reports/technical/day13_reproducibility_notes.txt

What to look for
- Forecast accuracy improved materially versus baseline methods
- Forecast outputs were translated into usable safety stock and reorder point policies
- Fulfillment strategy was evaluated as a trade-off, not as a single-metric winner
- Governance, assumptions, and limitations were documented explicitly

Headline results
- Baseline MA7 WMAPE: 19.25%
- XGBoost WMAPE: 11.06%
- Improvement vs baseline: 42.5%
- Safety stock value: $157,292.60
- Annual storage cost: $21,370.33
- Replenishment needed: $780,850.78
- Recommended strategy: Carbon-first

Important caution
Estimated carbon is a synthetic comparative proxy for strategy evaluation and should not be treated as a formal ESG disclosure metric.