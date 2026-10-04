import os

os.makedirs("src/water_network_optimizer", exist_ok=True)
os.makedirs("examples", exist_ok=True)

with open("pyproject.toml", "w", encoding="utf-8") as f:
    f.write('[build-system]\nrequires = ["setuptools>=61.0"]\nbuild-backend = "setuptools.build_meta"\n\n[project]\nname = "water-network-optimizer"\nversion = "0.1.0"\ndescription = "Hydraulic pipe sizing tool"\nreadme = "README.md"\nrequires-python = ">=3.9"\n')

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Water Network Optimizer 💧\n\nHydraulic pipe sizing and head loss optimization engine.\n\n## Usage\n
```bash\npython -m water_network_optimizer examples/sample_network.json\n
```\n")

with open(".gitignore", "w", encoding="utf-8") as f:
    f.write("__pycache__/\n*.pyc\nmake.py\n")

with open("examples/sample_network.json", "w", encoding="utf-8") as f:
    f.write('{"project_name": "District Zone 4", "pipes": [{"id": "P-101", "length_m": 450.0, "design_flow_lps": 45.0, "roughness_c": 130}, {"id": "P-102", "length_m": 320.0, "design_flow_lps": 30.0, "roughness_c": 130}]}')

with open("src/water_network_optimizer/__init__.py", "w", encoding="utf-8") as f:
    f.write('__version__ = "0.1.0"\n')

hydraulics_code = """import math

STANDARD_DIAMETERS_MM = [25.0, 32.0, 40.0, 50.0, 65.0, 80.0, 100.0, 125.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0]

def flow_velocity(flow_m3s, diameter_m):
    return flow_m3s / ((math.pi / 4.0) * (diameter_m ** 2))

def head_loss_hazen_williams(flow_m3s, diameter_m, length_m, roughness_c=130.0):
    if flow_m3s == 0:
        return 0.0
    return 10.67 * length_m * (flow_m3s ** 1.852) / ((roughness_c ** 1.852) * (diameter_m ** 4.8704))

def select_optimal_diameter(flow_lps, length_m, roughness_c=130.0, min_v=0.6, max_v=2.5):
    flow_m3s = flow_lps / 1000.0
    for d_mm in STANDARD_DIAMETERS_MM:
        d_m = d_mm / 1000.0
        v = flow_velocity(flow_m3s, d_m)
        if v <= max_v:
            hf = head_loss_hazen_williams(flow_m3s, d_m, length_m, roughness_c)
            return d_mm, v, hf
    d_mm = STANDARD_DIAMETERS_MM[-1]
    return d_mm, flow_velocity(flow_m3s, d_mm / 1000.0), 0.0
"""

with open("src/water_network_optimizer/hydraulics.py", "w", encoding="utf-8") as f:
    f.write(hydraulics_code)

cli_code = """import json, sys
from .hydraulics import select_optimal_diameter

def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else 'examples/sample_network.json'
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("=" * 60)
    print(f"Project: {data.get('project_name')}")
    print("=" * 60)
    for p in data['pipes']:
        d, v, hf = select_optimal_diameter(p['design_flow_lps'], p['length_m'], p.get('roughness_c', 130))
        print(f"Pipe {p['id']}: Diam={d}mm, Vel={v:.2f}m/s, HeadLoss={hf:.2f}m")
    print("=" * 60)

if __name__ == '__main__':
    main()
"""

with open("src/water_network_optimizer/cli.py", "w", encoding="utf-8") as f:
    f.write(cli_code)

with open("src/water_network_optimizer/__main__.py", "w", encoding="utf-8") as f:
    f.write("from .cli import main\nif __name__ == '__main__':\n    main()\n")

print("OK! ALL FILES CREATED.")
