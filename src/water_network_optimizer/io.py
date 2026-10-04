import json
import csv
from typing import List
from .models import PipeSegment, NetworkReport

def load_network_from_json(file_path: str) -> List[PipeSegment]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    segments = []
    for item in data.get("pipes", []):
        segments.append(PipeSegment(
            id=item["id"],
            from_node=item.get("from_node", "N/A"),
            to_node=item.get("to_node", "N/A"),
            length_m=float(item["length_m"]),
            design_flow_lps=float(item["design_flow_lps"]),
            roughness_c=float(item.get("roughness_c", 130.0)),
        ))
    return segments

def export_results_to_csv(report: NetworkReport, file_path: str) -> None:
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Pipe ID", "Design Flow (L/s)", "Optimal Diameter (mm)", "Velocity (m/s)", "Head Loss (m)", "Unit Loss (m/km)", "Status"])
        for res in report.results:
            writer.writerow([
                res.pipe_id,
                res.flow_lps,
                res.diameter_mm,
                res.velocity_mps,
                res.head_loss_m,
                res.unit_head_loss_m_per_km,
                res.status,
            ])
