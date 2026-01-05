from idlelib.rpc import response_queue
import uuid
from fastapi import FastAPI, APIRouter, HTTPException
from schemas.agent import ChatRequest, AgentResponse, ChatRequest
from services.agent_service import get_agent

router = APIRouter(prefix = "/agent", tags = ["agents"])

@router.post("/goal", response_model=AgentResponse)
async def create_goal(data: ChatRequest):
    session_id = data.session_id or str(uuid.uuid4())
    agent = get_agent(session_id = session_id)
    response = agent.run(data.message)
    return AgentResponse(answer=response.content, session_id=session_id)









