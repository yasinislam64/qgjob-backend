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


