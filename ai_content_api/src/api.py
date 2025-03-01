import os
from dotenv import load_dotenv
from fastapi import FastAPI
from crew import crew

# Load environment variables
load_dotenv()

app = FastAPI(title="AI Content API", version="1.0")

@app.post("/run")
def run_crew():
    """Run AI workflow"""
    result = crew.kickoff()
    return {"output": result}
