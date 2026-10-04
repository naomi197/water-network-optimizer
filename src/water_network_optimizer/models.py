from dataclasses import dataclass
from typing import List

@dataclass
class PipeSegment:
    id: str
    from_node: str
    to_node: str
    length_m: float
    design_flow_lps: float
    roughness_c: float = 130.0

@dataclass
class SizingResult:
    pipe_id: str
    flow_lps: float
    diameter_mm: float
    velocity_mps: float
    head_loss_m: float
    unit_head_loss_m_per_km: float
    status: str

@dataclass
class NetworkReport:
    total_length_m: float
    total_head_loss_m: float
    results: List[SizingResult]
