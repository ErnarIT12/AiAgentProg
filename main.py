from pydantic import BaseModel, validator, field_validator
from fastapi import FastAPI
from routers.agentRouters import router as agentRouters
app = FastAPI()
app.include_router(agentRouters)
@app.get("/")
async def root():
    return {"message": "FastAPI is up and running"}











