import argparse
import requests

API_BASE = "http://127.0.0.1:8000"

def submit(args):
    payload = {
        "org_id": args.org_id,
        "app_version_id": args.app_version_id,
        "test_path": args.test,
        "priority": args.priority,
        "target": args.target
    }
    try:
        response = requests.post(f"{API_BASE}/submit", json=payload)
        print("Status Code:", response.status_code)
        print("Raw Response:", response.text)

        # Parse response only if it's JSON
        try:
            data = response.json()
            print("JSON Response:", data)
        except Exception as e:
            print("Failed to parse JSON:", e)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

def status(args):
    try:
        response = requests.get(f"{API_BASE}/status/{args.job_id}")
        print("Status Code:", response.status_code)
        print("Raw Response:", response.text)

        try:
            data = response.json()
            print("JSON Response:", data)
        except Exception as e:
            print("Failed to parse JSON:", e)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

parser = argparse.ArgumentParser(prog="qgjob")
subparsers = parser.add_subparsers(dest="command")

# Submit
submit_parser = subparsers.add_parser("submit")
submit_parser.add_argument("--org-id", required=True)
submit_parser.add_argument("--app-version-id", required=True)
submit_parser.add_argument("--test", required=True)
submit_parser.add_argument("--priority", type=int, default=1)
submit_parser.add_argument("--target", required=True)
submit_parser.set_defaults(func=submit)

# Status
status_parser = subparsers.add_parser("status")
status_parser.add_argument("--job-id", required=True)
status_parser.set_defaults(func=status)

args = parser.parse_args()
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()
