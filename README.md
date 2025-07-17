# QualGent Backend

This is a backend service for managing AppWright test submissions. It supports test job queuing, grouping, scheduling, and GitHub Actions integration.

---

## 🚀 Features

- Queue and group submitted test jobs
- Schedule tests based on grouping criteria (e.g. tags, repo)
- Run and track test jobs
- RESTful API with endpoints to submit and check job status
- GitHub Actions integration for automated submissions

---

## 🧰 Setup Instructions

### 🐳 With Docker

```bash
# Clone the repo
git clone https://github.com/your-username/qgjob-backend.git
cd qgjob-backend

# Build and run the container
docker build -t qgjob-backend .
docker run -p 8000:8000 qgjob-backend

🏗 Architecture Diagram

                        ┌───────────────────────┐
                        │      GitHub Action    │
                        └────────────┬──────────┘
                                     │
                                     ▼
                        ┌──────────────────────────┐
                        │      /submit-job API     │
                        └────────────┬─────────────┘
                                     │
          ┌──────────────────────────┼──────────────────────────┐
          ▼                          ▼                          ▼
┌────────────────┐       ┌──────────────────────┐     ┌────────────────────┐
│  Job Queue     │──────▶│  Grouping Strategy   │────▶│  Scheduler/Runner  │
└────────────────┘       └──────────────────────┘     └────────────────────┘
                                                            │
                                                            ▼
                                                  ┌────────────────────┐
                                                  │  Result Collector  │
                                                  └─────────┬──────────┘
                                                            │
                                                            ▼
                                                ┌──────────────────────┐
                                                │  /status/{job_id}    │
                                                └──────────────────────┘
🧠 Grouping & Scheduling Logic

Jobs submitted via /submit-job are:

Queued immediately.

Grouped based on shared attributes like:

Repo name

Test tag

Priority (future feature)

Scheduled in batches using a JobRunner, which:

Picks jobs from the same group

Executes them sequentially or concurrently

Collects output & updates job status

Grouping logic is configurable and modular. Add your own strategies in grouping.py.

✅ End-to-End Test Submission
Start the server:
uvicorn main:app --reload

Submit a test job:
python3 qgjob.py submit --org-id qualgent --app-version-id xyz123 --test tests/onboarding.spec.js

Check the job status:
python3 qgjob.py status --job-id abc123  # Replace abc123 with the actual job ID given to you


