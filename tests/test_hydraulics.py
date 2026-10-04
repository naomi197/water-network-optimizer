import pytest
from water_network_optimizer.hydraulics import (
    flow_velocity,
    head_loss_hazen_williams,
    select_optimal_diameter,
)

def test_flow_velocity():
    flow = 0.05
    d = 0.2
    v = flow_velocity(flow, d)
    assert 1.5 < v < 1.6

def test_head_loss_zero_flow():
    assert head_loss_hazen_williams(0.0, 0.2, 500.0) == 0.0

def test_optimal_diameter_selection():
    d_mm, v, hf = select_optimal_diameter(flow_lps=40.0, length_m=500.0)
    assert d_mm in [150.0, 200.0]
    assert 0.6 <= v <= 2.5
    assert hf > 0
