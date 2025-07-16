# QualGent Backend Coding Challenge

## Overview

This project implements a backend job orchestrator and CLI tool (`qgjob`) for managing AppWright end-to-end test jobs. It allows organizations to submit tests, which are grouped by `app_version_id` and assigned to available devices (emulator, physical device, BrowserStack) to optimize test execution.

The system supports job submission, status tracking, and scheduling with efficient batching to minimize app reinstalls.

---

## Tech Stack

- Backend: FastAPI (Python)  
- CLI Tool: Python (`qgjob.py`)  
- Queueing & Storage: Redis  
- CI Integration: GitHub Actions  

---

## Setup Instructions

### Prerequisites

- Python 3.10+ installed  
- Redis server installed and running locally (default port 6379)  
- `pip` package manager  

### Install dependencies

```bash
pip install -r requirements.txt

Start Redis Server
If Redis is installed locally, start it with: redis-server

Run the Backend Server
uvicorn main:app --reload
The backend server will be available at http://127.0.0.1:8000

CLI Tool Usage
Submit a Test Job
python3 qgjob.py submit --org-id=qualgent --app-version-id=xyz123 --test=tests/onboarding.spec.js --target=device

Check Job Status
python qgjob.py status --job-id=<job_id>