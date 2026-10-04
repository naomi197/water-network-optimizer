\# Water Network Optimizer



\[!\[Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)

\[!\[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

\[!\[Domain](https://img.shields.io/badge/Domain-Hydraulic%20%26%20Civil%20Engineering-green.svg)](#)



A high-performance Python engineering toolkit designed to size pipe diameters, calculate head loss via the \*\*Hazen-Williams equation\*\*, and optimize municipal and commercial pressurized water distribution systems.



\---



\## Key Features



\- \*\*Hazen-Williams Hydraulic Engine:\*\* Computes friction head loss and flow velocity across pipe networks.

\- \*\*Automated Pipe Sizing:\*\* Iteratively sizes standard pipe diameters to satisfy velocity thresholds (0.6 m/s ≤ V ≤ 2.5 m/s).

\- \*\*Head Loss Optimization:\*\* Minimizes hydraulic energy loss while adhering to velocity limits and pressure constraints.

\- \*\*Export \& Reporting:\*\* Exports sizing schedules and hydraulic metrics directly to CSV and visualization plots.

\- \*\*CLI \& Scriptable API:\*\* Ready for both command-line automation and programmatic integration into larger infrastructure pipelines.



\---



\## Mathematical Formulation



Frictional head loss is evaluated using the empirical Hazen-Williams formula (SI units):



$$h\_f = 10.67 \\cdot \\frac{L \\cdot Q^{1.852}}{C^{1.852} \\cdot D^{4.87}}$$



Where:

\- $h\_f$: Head loss due to friction (m)

\- $L$: Pipe length (m)

\- $Q$: Volumetric flow rate ($m^3/s$)

\- $C$: Hazen-Williams roughness coefficient

\- $D$: Pipe internal diameter (m)



\---



\## Installation

```bash

git clone https://github.com/naomi197/water-network-optimizer.git

cd water-network-optimizer

python -m venv .venv

\# Windows

.venv\\Scripts\\activate

\# Linux/macOS

source .venv/bin/activate



pip install -e .



