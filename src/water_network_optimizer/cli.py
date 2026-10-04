import argparse
import sys
from .io import load_network_from_json, export_results_to_csv
from .optimizer import optimize_network

def main():
    parser = argparse.ArgumentParser(description="Water Network Hydraulic Optimizer")
    parser.add_argument("input", help="Path to input network JSON file")
    parser.add_argument("--csv", default="outputs/sizing_results.csv", help="Path to output CSV report")
    parser.add_argument("--plot", default="outputs/head_loss.png", help="Path to head loss PNG chart")
    parser.add_argument("--min-v", type=float, default=0.6, help="Min allowable velocity (m/s)")
    parser.add_argument("--max-v", type=float, default=2.5, help="Max allowable velocity (m/s)")
    args = parser.parse_args()

    pipes = load_network_from_json(args.input)
    report = optimize_network(pipes, min_velocity_mps=args.min_v, max_velocity_mps=args.max_v)

    export_results_to_csv(report, args.csv)
    print(f"Analysis complete. Total Network Length: {report.total_length_m} m | Total Head Loss: {report.total_head_loss_m} m")
    print(f"Results exported to {args.csv}")

if __name__ == "__main__":
    main()
