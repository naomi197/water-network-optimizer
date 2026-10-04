import os

files = {
    "pyproject.toml": """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "water-network-optimizer"
version = "0.1.0"
description = "Hydraulic pipe sizing and head loss optimization engine"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "MIT"}
authors = [{name = "Alireza Fazeli"}]

[project.scripts]
water-optimizer = "water_network_optimizer.cli:main"
""",

    "README.md": """# Water Network Optimizer 💧

Hydraulic pipe sizing and head loss optimization engine for municipal water supply networks.

## Features
- **Hazen-Williams Calculation**: Automated head loss and friction gradient computation.
- **Velocity Window Enforcement**: Sizing against industry criteria (0.6 - 2.5 m/s) to prevent sedimentation and surge.
- **Standard Metric Sizing**: Commercial diameters from 25mm to 800mm.
- **Automated CLI & CSV Reports**: Production-ready command line interface.

## Quickstart
```bash
python -m water_network_optimizer examples/sample_network.json
