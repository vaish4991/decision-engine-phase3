from pydantic import BaseModel


class Context(BaseModel):
    question_number: int
    total_questions: int
    confidence: float
    consistency: bool


class DecisionRequest(BaseModel):
    score: float
    context: Context