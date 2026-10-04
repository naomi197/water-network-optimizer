from typing import List
from .models import PipeSegment, SizingResult, NetworkReport
from .hydraulics import select_optimal_diameter

def optimize_network(
    segments: List[PipeSegment],
    min_velocity_mps: float = 0.6,
    max_velocity_mps: float = 2.5
) -> NetworkReport:
    results: List[SizingResult] = []
    total_length = 0.0
    total_head_loss = 0.0

    for seg in segments:
        d_mm, v, hf = select_optimal_diameter(
            flow_lps=seg.design_flow_lps,
            length_m=seg.length_m,
            roughness_c=seg.roughness_c,
            min_velocity_mps=min_velocity_mps,
            max_velocity_mps=max_velocity_mps,
        )

        status = "OK"
        if v < min_velocity_mps:
            status = "Low Velocity (Sedimentation Risk)"
        elif v > max_velocity_mps:
            status = "High Velocity (Erosion / Surge Risk)"

        unit_hl = (hf / (seg.length_m / 1000.0)) if seg.length_m > 0 else 0.0

        results.append(SizingResult(
            pipe_id=seg.id,
            flow_lps=seg.design_flow_lps,
            diameter_mm=d_mm,
            velocity_mps=round(v, 3),
            head_loss_m=round(hf, 3),
            unit_head_loss_m_per_km=round(unit_hl, 3),
            status=status,
        ))
        total_length += seg.length_m
        total_head_loss += hf

    return NetworkReport(
        total_length_m=round(total_length, 2),
        total_head_loss_m=round(total_head_loss, 3),
        results=results,
    )
