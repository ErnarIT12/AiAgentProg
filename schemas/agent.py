from pydantic import BaseModel, field_validator, Field
class GoalRequest(BaseModel):
    goal: str
    level: str
class AgentResponse(BaseModel):
    answer: str

