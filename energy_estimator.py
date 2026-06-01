"""Simple planning estimator for Urja Loom.

This is not a circuit simulator. It is a lightweight calculator for comparing
prototype assumptions while documenting the design process.
"""

from __future__ import annotations

import argparse


def estimate_energy_wh(
    steps: int,
    voltage: float,
    current_ma: float,
    pulse_seconds: float,
    efficiency: float,
) -> float:
    current_a = current_ma / 1000
    joules = steps * voltage * current_a * pulse_seconds * efficiency
    return joules / 3600


def led_runtime_minutes(energy_wh: float, led_watts: float) -> float:
    if led_watts <= 0:
        raise ValueError("LED wattage must be positive.")
    return (energy_wh / led_watts) * 60


def main() -> None:
    parser = argparse.ArgumentParser(description="Estimate Urja Loom energy output.")
    parser.add_argument("--steps", type=int, default=1800, help="Number of foot presses.")
    parser.add_argument("--voltage", type=float, default=4.5, help="Voltage per press.")
    parser.add_argument("--current-ma", type=float, default=8.0, help="Current per press in mA.")
    parser.add_argument(
        "--pulse-seconds",
        type=float,
        default=0.08,
        help="Effective pulse duration per press.",
    )
    parser.add_argument(
        "--efficiency",
        type=float,
        default=0.35,
        help="Combined conversion/storage efficiency from 0 to 1.",
    )
    parser.add_argument("--led-watts", type=float, default=1.0, help="LED load wattage.")
    args = parser.parse_args()

    if not 0 <= args.efficiency <= 1:
        raise ValueError("Efficiency must be between 0 and 1.")

    energy = estimate_energy_wh(
        steps=args.steps,
        voltage=args.voltage,
        current_ma=args.current_ma,
        pulse_seconds=args.pulse_seconds,
        efficiency=args.efficiency,
    )
    runtime = led_runtime_minutes(energy, args.led_watts)

    print(f"Estimated stored energy: {energy:.4f} Wh")
    print(f"Estimated runtime for {args.led_watts:g} W LED: {runtime:.2f} minutes")


if __name__ == "__main__":
    main()

