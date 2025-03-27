from fastapi import FastAPI
from pydantic import BaseModel
import uuid


app = FastAPI()

jobs = {}



class JobRequest(BaseModel):    #BaseModel authenticates makes sure the passed in is legit simply inherits 
    command: str




@app.post("/submit") # A client will send a post from anywhere maybe like this curl   ** -X POST "http://localhost:8000/submit" \H "Content-Type: application/json" \d '{"command": "python script.py"}'
def submit_job(job: JobRequest):   # Saying the job arg should be type JobRequest  and we call is a job instance
    job_id = str(uuid.uuid4()) # generate a unique job ID
    
    
    jobs[job_id] = {"command": job.command, 
                    "status": "queued",
                   }  #2ith the new key store its status and queue and the command 
    

    
    return {"job_id": job_id, 
            "message": "Job submitted"
            }

    #dict within a dict 
    #/submit gets automatically converted in JobRequest object that we instaniate using job?
    
    
@app.get("/status/{job_id}")


def check_status(job_id: str):
    job = jobs.get(job_id)
    if job:
        
        return{"job_id":job_id, 
               "status": job["status"],
               "Test": "Working on it"
                }
    return {"error": "Job not found"}



@app.get("/jobs")
def get_all_jobs():
    return jobs





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    
    
# uvicorn job_api:app --host 127.0.0.1 --port 8000 --reload
# http://127.0.0.1:8000/docs


    


    