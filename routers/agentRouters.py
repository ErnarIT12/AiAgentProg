from fastapi import FastAPI, APIRouter, HTTPException
from schemas.agent import GoalRequest, AgentResponse
router = APIRouter(prefix = "/agent", tags = ["agents"])

@router.post("/goal", response_model = GoalRequest)
async def creat_goal(data: GoalRequest):
    pass


