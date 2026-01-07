# serve_agent.py
# from crew_workflow import run_crew_workflow  # Import your function
from fastapi import FastAPI
from pydantic import BaseModel

import app_crew2 as ac

app = FastAPI()


# Define the input data structure
class CrewInput(BaseModel):
    topic: str


@app.post("/run_crew")
def run_crew_endpoint(input_data: CrewInput):
    """
    Endpoint to trigger the CrewAI workflow.
    """
    try:
        result = ac.run_crew2(input_data.topic)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
