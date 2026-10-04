from water_network_optimizer.models import PipeSegment
from water_network_optimizer.optimizer import optimize_network

def test_optimize_network():
    pipes = [
        PipeSegment(id="P1", from_node="A", to_node="B", length_m=500.0, design_flow_lps=35.0),
        PipeSegment(id="P2", from_node="B", to_node="C", length_m=300.0, design_flow_lps=15.0),
    ]
    report = optimize_network(pipes)
    assert len(report.results) == 2
    assert report.total_length_m == 800.0
    for res in report.results:
        assert res.status == "OK"
