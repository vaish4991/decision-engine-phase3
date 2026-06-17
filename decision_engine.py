def decide_action(score, context):

    # Interview completed
    if context.question_number >= context.total_questions:
        return "end_interview"

    # Inconsistent evaluation
    if not context.consistency:
        return "follow_up"

    # Low confidence
    if context.confidence < 0.5:
        return "follow_up"

    # Borderline scores
    if 70 <= score < 75:
        return "follow_up"

    # Strong answer
    if score >= 75:
        return "next_question"

    # Average answer
    if score >= 50:
        return "follow_up"

    # Weak answer
    return "end_interview"