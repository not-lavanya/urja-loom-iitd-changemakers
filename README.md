# Urja Loom

Urja Loom is a sustainable energy-harvesting prototype that converts the repetitive foot-pedal motion of handloom weavers into usable electrical energy for workspace lighting.

The project was developed during the IIT Delhi Changemakers Bootcamp 2.0 as a community-centered design response to unreliable electricity access, dim workspaces, and the cost of generator-based lighting in handloom and tailoring contexts.

![Piezoelectric tile prototype](assets/images/piezoelectric-tile-prototype.png)

## Problem

Many handloom weavers and tailors work in informal or semi-formal settings where electricity supply can be unreliable. When power fails, work hours, productivity, and earnings are affected. Generator-based backup is expensive and carbon-intensive.

Urja Loom asks a practical question:

> Can the repeated foot motion already present in loom work be used to power small lighting needs with minimal disruption to the worker?

## Approach

The prototype uses piezoelectric discs embedded into a tile-like structure placed under the foot-pedal zone of a loom or similar workspace. Mechanical pressure from repeated foot motion is converted into electrical output, conditioned through a circuit, and stored or used for LED lighting.

## System Flow

```text
Foot-pedal pressure
    -> Piezoelectric tile array
    -> Bridge rectifier
    -> Capacitor / smoothing stage
    -> Control / switching stage
    -> Rechargeable battery or lighting load
    -> LED workspace lighting
```

## Prototype Highlights

- Built at IIT Delhi Makerspace during Changemakers Bootcamp 2025.
- Used a tile array with piezoelectric discs to simulate handloom foot-pedal pressure.
- Explored multiple circuit designs for rectification, voltage stabilization, storage, and lighting.
- Tested output behavior with multimeter readings and lighting loads.
- User research with 20+ respondents indicated strong interest in visible, foot-powered clean-energy feedback.

## Key Design Principles

- **Fit the worker, not the lab.** The design should adapt to natural foot-pressure patterns rather than requiring weavers to change their rhythm.
- **Make impact visible.** Survey responses showed that users were more likely to engage when they could see the output, such as lights turning on.
- **Keep cost realistic.** Cost, maintenance, durability, and vandalism risk were common concerns.
- **Design for low disruption.** The system should integrate into existing workspaces with minimal retraining.

## Repository Structure

```text
urja-loom/
  README.md
  docs/
    design-brief.md
    technical-architecture.md
    user-research-summary.md
  src/
    energy_estimator.py
  data/
    sample_assumptions.csv
  assets/
    images/
```

## Quick Energy Estimate

Run the simple estimator:

```bash
python src/energy_estimator.py --steps 1800 --voltage 4.5 --current-ma 8 --efficiency 0.35
```

This is not a production-grade electrical simulation. It is a lightweight planning tool for comparing assumptions and documenting prototype reasoning.

## Status

Prototype / research-stage project. The current repository documents the design logic, early prototype, and future improvement directions.

## Future Work

- Improve voltage stabilization and storage efficiency.
- Test under real loom-pedal pressure patterns for longer durations.
- Add a durable casing suitable for dust, vibration, and workshop conditions.
- Add low-cost visual feedback showing generated energy.
- Compare piezoelectric design against flywheel/dynamo alternatives for specific weaving contexts.

## Acknowledgements

Developed as part of IIT Delhi Changemakers Bootcamp 2.0 with mentorship from Prof. Jay Dhariwal and the bootcamp team.

