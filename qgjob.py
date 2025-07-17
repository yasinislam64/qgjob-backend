import requests
import argparse
import time

BASE_URL = "http://localhost:8000"

def submit(org_id, app_version_id, test, priority=0, target="device"):
    payload = {
        "org_id": org_id,
        "app_version_id": app_version_id,
        "test_path": test,
        "priority": priority,
        "target": target,
    }
    response = requests.post(f"{BASE_URL}/submit", json=payload)
    if response.ok:
        print("Job submitted:", response.json())
    else:
        print("Error submitting job:", response.text)

def status(job_id):
    response = requests.get(f"{BASE_URL}/status/{job_id}")
    if response.ok:
        print("Job status:", response.json())
    else:
        print("Error fetching status:", response.text)

def main():
    parser = argparse.ArgumentParser(prog="qgjob")
    subparsers = parser.add_subparsers(dest="command")

    submit_parser = subparsers.add_parser("submit")
    submit_parser.add_argument("--org-id", required=True)
    submit_parser.add_argument("--app-version-id", required=True)
    submit_parser.add_argument("--test", required=True)
    submit_parser.add_argument("--priority", type=int, default=0)
    submit_parser.add_argument("--target", default="device")

    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("--job-id", required=True)

    args = parser.parse_args()

    if args.command == "submit":
        submit(args.org_id, args.app_version_id, args.test, args.priority, args.target)
    elif args.command == "status":
        status(args.job_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
