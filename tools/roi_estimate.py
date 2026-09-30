#!/usr/bin/env python3
"""Estimate daily profit / payback for an Antminer Z15 Pro 860K-class unit."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Bitmain typical wall power for Z15 Pro 860K @ 25°C
DEFAULT_WATTS = 2780.0


def kwh_per_day(watts: float) -> float:
    return watts * 24.0 / 1000.0


def estimate(
    cost: float,
    shipping: float,
    kwh_price: float,
    revenue: float,
    pool_fee: float,
    watts: float = DEFAULT_WATTS,
) -> dict:
    kwh = kwh_per_day(watts)
    elec = kwh * kwh_price
    net_rev = revenue * (1.0 - pool_fee)
    profit = net_rev - elec
    all_in = cost + shipping
    payback = (all_in / profit) if profit > 0 else None
    return {
        "watts": watts,
        "kwh_per_day": round(kwh, 2),
        "electricity_per_day": round(elec, 2),
        "net_revenue_per_day": round(net_rev, 2),
        "profit_per_day": round(profit, 2),
        "all_in_cost": round(all_in, 2),
        "payback_days": round(payback, 1) if payback is not None else None,
        "payback_months": round(payback / 30.0, 1) if payback is not None else None,
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--cost", type=float, help="Hardware USD cost")
    p.add_argument("--shipping", type=float, default=0.0, help="Shipping USD")
    p.add_argument("--kwh", type=float, help="Electricity price USD/kWh")
    p.add_argument("--revenue", type=float, help="Gross USD revenue per day before fees")
    p.add_argument("--pool-fee", type=float, default=0.01, help="Pool fee fraction (0.01 = 1%)")
    p.add_argument("--watts", type=float, default=DEFAULT_WATTS, help="Wall watts (default 2780)")
    p.add_argument("--from-json", type=Path, help="Load inputs from JSON file")
    args = p.parse_args()

    if args.from_json:
        data = json.loads(args.from_json.read_text(encoding="utf-8"))
        result = estimate(
            cost=float(data["cost"]),
            shipping=float(data.get("shipping", 0)),
            kwh_price=float(data["kwh"]),
            revenue=float(data["revenue"]),
            pool_fee=float(data.get("pool_fee", 0.01)),
            watts=float(data.get("watts", DEFAULT_WATTS)),
        )
    else:
        missing = [n for n, v in (("cost", args.cost), ("kwh", args.kwh), ("revenue", args.revenue)) if v is None]
        if missing:
            p.error(f"missing required args: {', '.join(missing)} (or use --from-json)")
        result = estimate(
            cost=args.cost,
            shipping=args.shipping,
            kwh_price=args.kwh,
            revenue=args.revenue,
            pool_fee=args.pool_fee,
            watts=args.watts,
        )

    print("Z15 Pro 860K-style estimate")
    print("---------------------------")
    for key, value in result.items():
        print(f"{key:24} {value}")
    if result["profit_per_day"] <= 0:
        print("\nProfit is zero/negative at these inputs — not profitable to run.")
    print("\nNot financial advice. Revenue estimates change with price & difficulty.")
    print("Hardware reference: https://www.z15pro860.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
