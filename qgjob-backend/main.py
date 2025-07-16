from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import redis

# Connect to Redis (default localhost:6379)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

app = FastAPI()

# Job payload schema
class Job(BaseModel):
    org_id: str
    app_version_id: str
    test_path: str
    priority: int = 1
    target: str  # emulator, device, browserstack

# Submit a new job
@app.post("/submit")
def submit_job(job: Job):
    job_id = str(uuid.uuid4())  # Generate unique job ID
    job_data = job.dict()
    job_data['status'] = "queued"
    # Store job data as JSON string in Redis hash
    r.hset(f"job:{job_id}", mapping=job_data)
    # Add job_id to a queue list (optional)
    r.lpush(f"queue:{job.org_id}", job_id)
    return {"job_id": job_id, "message": "Job submitted successfully"}

# Get status of a job
@app.get("/status/{job_id}")
def get_status(job_id: str):
    job = r.hgetall(f"job:{job_id}")
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"job_id": job_id, "status": job.get("status", "unknown")}

# Simple root route
@app.get("/")
def root():
    return {"message": "AppWright Job Orchestrator is running."}

