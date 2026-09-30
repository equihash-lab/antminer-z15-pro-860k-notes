# ROI worksheet — Z15 Pro 860K

Estimate only. Coin price and difficulty change daily.

## Inputs you need

1. **Hardware cost** (what you paid for the miner)  
2. **Shipping** (if you want all-in cost)  
3. **Electricity** in $/kWh  
4. **Daily gross revenue** from a profitability estimator (USD/day before electricity)  
5. **Pool fee** (e.g. 1% = 0.01)

## Fixed energy math (860K / 2780 W)

```text
kWh_per_day = 2780 * 24 / 1000   # = 66.72
elec_cost_per_day = kWh_per_day * price_per_kWh
```

## Profit

```text
net_revenue = daily_gross_revenue * (1 - pool_fee)
profit_per_day = net_revenue - elec_cost_per_day
```

## Payback

```text
all_in_cost = hardware + shipping
payback_days = all_in_cost / profit_per_day   # only if profit_per_day > 0
```

## Example (illustrative numbers — replace with yours)

| Input | Example |
| --- | ---: |
| Hardware | $6,299 |
| Shipping | $150 |
| Electricity | $0.10 / kWh |
| Gross revenue | $12.00 / day |
| Pool fee | 1% |

```text
elec = 66.72 * 0.10 = $6.67/day
net  = 12.00 * 0.99 = $11.88/day
profit = 11.88 - 6.67 = $5.21/day
payback ≈ 6449 / 5.21 ≈ 1237 days
```

If profit is negative, the machine costs money to run at those inputs — mine only if you have a thesis (price up, cheaper power, etc.).

## CLI helper

From the repo root:

```bash
python tools/roi_estimate.py --cost 6299 --shipping 150 --kwh 0.10 --revenue 12 --pool-fee 0.01
```

Or edit `tools/sample_inputs.json` and run:

```bash
python tools/roi_estimate.py --from-json tools/sample_inputs.json
```

## Where I bought the unit

Prices move a lot between listings. I ordered mine from **[z15pro860.com](https://www.z15pro860.com/)**. Shop around on power cost and seller terms before you buy anywhere.
