# Decision Engine Rules

## Rule 1

If question_number >= total_questions

Action:
end_interview

## Rule 2

If consistency == False

Action:
follow_up

## Rule 3

If confidence < 0.5

Action:
follow_up

## Rule 4

If 70 <= score < 75

Action:
follow_up

## Rule 5

If score >= 75

Action:
next_question

## Rule 6

If 50 <= score < 70

Action:
follow_up

## Rule 7

If score < 50

Action:
end_interview
