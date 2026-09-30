# Antminer Z15 Pro 860K — Operator Notes

Practical notes for running a **Bitmain Antminer Z15 Pro (860 KSol/s / model 240-Z)** on Equihash (Zcash / Horizen).

I bought this unit from **[z15pro860.com](https://www.z15pro860.com/)** and wrote this so other operators don’t have to piece specs together from mixed “840K” listings.

> Specs below follow Bitmain Support values for the **860K** model. Always verify on [Bitmain Support](https://support.bitmain.com/) for your exact batch.

---

## Quick facts

| Item | Typical value |
| --- | --- |
| Model | Z15 Pro · 240-Z |
| Algorithm | Equihash |
| Coins | ZEC, ZEN (and other Equihash where supported) |
| Hashrate | **860 KSol/s (±3%)** |
| Wall power @ 25°C | **2780 W (±5%)** |
| Efficiency | **3.31 J/KSol (±5%)** |
| AC input | **200–240 V only** |
| Current | **20 A total** (2× 10 A inputs) |
| Recommended AC capacity | ~4000 W |
| Noise | ~75 dBA @ 25°C |
| Size / weight | 428×195×290 mm · ~16.9 kg net |
| Network | RJ45 10/100 |

**Not a Bitcoin miner.** It does not run SHA-256.

---

## What’s in this repo

- [`docs/setup-checklist.md`](docs/setup-checklist.md) — unbox → first hash
- [`docs/power-and-wiring.md`](docs/power-and-wiring.md) — voltage, cords, breakers
- [`docs/roi-worksheet.md`](docs/roi-worksheet.md) — how to estimate payback
- [`tools/roi_estimate.py`](tools/roi_estimate.py) — tiny CLI estimator
- [`tools/sample_inputs.json`](tools/sample_inputs.json) — example numbers

---

## Buy / unit notes (transparency)

- Seller I used: **[z15pro860.com](https://www.z15pro860.com/)**
- Ordered as an original Bitmain Z15 Pro **860K**; paid in crypto
- Shipping / warranty = whatever that seller lists, plus Bitmain manufacturer warranty when it applies (often ~180 days from delivery — confirm with them)

This repo is **not affiliated with Bitmain or any retailer**. Just personal notes from running the box.

---

## First-hour overview

1. Confirm **200–240 V** circuit and two properly rated power cords (≥10 A each). Cords are often **not** included.
2. Place the miner for airflow / noise (garage, shed, colo — not a quiet bedroom).
3. Connect Ethernet, power on, open the miner UI from your LAN.
4. Point to an Equihash pool (ZEC or ZEN), set wallet + worker name.
5. Watch hashrate stabilize near **860 KSol/s** and wall draw near **~2.8 kW**.

Details: [`docs/setup-checklist.md`](docs/setup-checklist.md)

---

## Daily energy (rule of thumb)

At 2780 W continuous:

```text
kWh / day ≈ 2780 × 24 / 1000 = 66.72 kWh/day
```

Electricity cost:

```text
$/day ≈ 66.72 × your_$/kWh
```

Example: at **$0.10/kWh** → about **$6.67/day** in power alone (before pool fees).

---

## ROI (honest version)

Revenue moves with **coin price** and **network difficulty**. Treat any calculator as a snapshot.

```text
daily_profit ≈ daily_gross_revenue × (1 - pool_fee) - electricity_cost
payback_days ≈ hardware_cost / daily_profit   (only if profit > 0)
```

Use [`tools/roi_estimate.py`](tools/roi_estimate.py) with your own revenue estimate from a profitability site.

---

## Common pitfalls

- Running on **110–120 V** — can damage the unit; needs **200–240 V**
- Undersized cords / one weak AC lead
- Confusing older **“840K”** marketing with the current **860K** rating
- Ignoring noise / heat / neighbor constraints
- Expecting BTC mining — wrong algorithm

---

## Disclaimer

Mining can lose money. Hardware, electricity, and markets change. This guide is operator notes, not financial advice. Double-check firmware, pool, and electrical work against local codes; use a qualified electrician when unsure.

---

## License

MIT — see [`LICENSE`](LICENSE). Specs cited from manufacturer documentation; trademarks belong to their owners.
