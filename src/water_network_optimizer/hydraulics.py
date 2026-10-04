import math
STANDARD_DIAMETERS_MM = [25.0, 32.0, 40.0, 50.0, 65.0, 80.0, 100.0, 125.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0]
def flow_velocity(flow_m3s, diameter_m):
    return flow_m3s / ((math.pi / 4.0) * (diameter_m ** 2))
def head_loss_hazen_williams(flow_m3s, diameter_m, length_m, roughness_c=130.0):
    if flow_m3s == 0: return 0.0
    return 10.67 * length_m * (flow_m3s ** 1.852) / ((roughness_c ** 1.852) * (diameter_m ** 4.8704))
def select_optimal_diameter(flow_lps, length_m, roughness_c=130.0, min_v=0.6, max_v=2.5, min_velocity_mps=None, max_velocity_mps=None):
    if min_velocity_mps is not None: min_v = min_velocity_mps
    if max_velocity_mps is not None: max_v = max_velocity_mps
    flow_m3s = flow_lps / 1000.0
    for d_mm in STANDARD_DIAMETERS_MM:
        v = flow_velocity(flow_m3s, d_mm / 1000.0)
        if v <= max_v:
            hf = head_loss_hazen_williams(flow_m3s, d_mm / 1000.0, length_m, roughness_c)
            return d_mm, v, hf
    return STANDARD_DIAMETERS_MM[-1], flow_velocity(flow_m3s, STANDARD_DIAMETERS_MM[-1]/1000.0), 0.0
