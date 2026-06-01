# Technical Architecture

## Hardware Concept

Urja Loom uses a piezoelectric tile array beneath a repeated foot-pressure zone. Each press generates a small voltage pulse. The circuit rectifies, smooths, and stores the generated energy before powering a lighting load.

## Components Explored

- Piezoelectric discs / sensors
- Bridge rectifier
- Capacitor
- Relay or switching stage
- Rechargeable battery
- Inverter or boost stage, depending on load
- LED lighting load
- MDF or tile base for pressure distribution

## Prototype Flow

```text
Piezoelectric discs
    -> rectification
    -> smoothing / temporary storage
    -> voltage boosting or switching
    -> storage / output
    -> LED lighting
```

## Observed Technical Challenges

- Voltage output depends heavily on pressure and contact consistency.
- Piezoelectric pulses need conditioning before they are useful.
- Conversion losses are significant, especially when moving between DC and AC stages.
- A design optimized in the lab may underperform under real user pressure patterns.
- Durability and casing matter as much as raw electrical output.

## Engineering Direction

Future versions should prioritize:

- lower-power LED lighting instead of high-watt bulbs
- direct DC lighting to reduce conversion losses
- better pressure distribution across the tile
- modular casing for replacement and maintenance
- visible output indicators for user trust

