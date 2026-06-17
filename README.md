# Decision Engine (Next Step Selector)

## Overview

This project implements a Decision Engine for an AI Interview System.

The engine determines whether the system should:

* Ask the next question
* Ask a follow-up question
* End the interview

based on candidate evaluation results.

---

## Technologies

* Python
* FastAPI
* Pydantic
* Uvicorn

---

## Input

```json
{
  "score": 85,
  "context": {
    "question_number": 2,
    "total_questions": 10,
    "confidence": 0.8,
    "consistency": true
  }
}
```

## Output

```json
{
  "score": 85,
  "action": "next_question"
}
```

---

## Actions

* next_question
* follow_up
* end_interview

---

## Run

```bash
source venv/bin/activate
uvicorn app:app --reload
```

---

## API Endpoint

POST /decision

---

## Features

* Borderline score handling
* Confidence-based decisions
* Consistency validation
* Deterministic rule-based engine
* Simulation testing
