# Setup checklist — Z15 Pro 860K

Use this after the miner arrives.

## Before you power on

- [ ] Confirm outlet / PDU is **200–240 V AC**
- [ ] Two power cords rated **≥ 10 A** each (often sold separately)
- [ ] Circuit / breaker sized for ~**2.8 kW** continuous (+ headroom; Bitmain cites ~4000 W adapted capacity)
- [ ] Ethernet cable to your router / switch
- [ ] Space for exhaust air and ~**75 dBA** noise
- [ ] Pool account + ZEC or ZEN wallet ready

## Unbox

- [ ] Inspect for shipping damage; photo the unit + serial if you need warranty
- [ ] Note model sticker (**Z15 Pro / 240-Z** expected for 860K class)
- [ ] Keep packaging until first stable run

## Network & first boot

- [ ] Connect Ethernet
- [ ] Plug **both** AC inputs
- [ ] Power on; wait for UI / network
- [ ] Find IP via router DHCP list or Bitmain scanner tooling
- [ ] Login to miner web UI (default credentials — change after first login; check Bitmain docs for your firmware)

## Pool

- [ ] Algorithm: **Equihash**
- [ ] Pool URL + port from your pool’s Z15 / Equihash guide
- [ ] Wallet address (correct coin network)
- [ ] Worker name (e.g. `rig1`)
- [ ] Save & reboot mining process if required

## Verify

- [ ] Hashrate settles near **860 KSol/s (±3%)**
- [ ] Fans ramp under load; no thermal alarms
- [ ] Pool shows the worker as connected
- [ ] Optional: clamp meter / PDU reading near **~2780 W** at room ~25°C

## After 24 hours

- [ ] Confirm accepted shares / no persistent hardware errors
- [ ] Record serial, purchase order ID, and seller contact
- [ ] If you bought from [z15pro860.com](https://www.z15pro860.com/), keep the order email for tracking / warranty

## If something fails

1. Recheck voltage and both AC leads  
2. Try another Ethernet cable / port  
3. Confirm pool stratum and wallet  
4. Contact the seller with order ID + photos (for purchase support) and Bitmain channels for manufacturer warranty process when applicable
