# Power & wiring — Z15 Pro 860K

Electrical mistakes are the #1 way to kill an ASIC. Read this before first power-on.

## Voltage

- Required: **200–240 V AC**, 50/60 Hz  
- **Do not** run on typical North American 120 V wall outlets without a proper 240 V circuit

## Current & cords

Bitmain documents about **20 A** total across **two** AC inputs (**10 A each**).

- Use **two** cords, each rated **≥ 10 A**
- Power cords are frequently **not included** with the unit
- Avoid cheap thin extension cords; keep cable runs short when possible

## Breaker / capacity

Continuous wall draw is typically **~2780 W (±5%)** at 25°C.

Rough continuous current at 230 V:

```text
I ≈ 2780 W / 230 V ≈ 12.1 A
```

Still follow Bitmain’s higher **adapted AC capacity (~4000 W)** guidance and local electrical code. When in doubt, hire an electrician.

## Heat & placement

- Plan exhaust so hot air does not recirculate into the intake
- Noise is high (~**75 dBA**); plan location accordingly
- Keep ambient in the manufacturer operating window (commonly **0–40°C**, humidity limits apply — see Bitmain Support)

## PDU tips

- Use a PDU that shows per-outlet or total watts if you want real wall power readings
- Don’t daisy-chain consumer power strips

## Safety

- Dry location only  
- No liquid cooling mods unless you fully accept voiding warranty / fire risk  
- Bonding / grounding must meet local code  

This is not professional electrical advice.
