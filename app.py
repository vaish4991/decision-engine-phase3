from fastapi import FastAPI
from models import DecisionRequest
from decision_engine import decide_action

app = FastAPI(
    title="Decision Engine API",
    version="1.0"
)


@app.post("/decision")
def decision(request: DecisionRequest):

    action = decide_action(
        request.score,
        request.context
    )

    return {
        "score": request.score,
        "action": action
    }