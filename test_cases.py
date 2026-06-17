from decision_engine import decide_action


class Context:
    def __init__(self, q, t, c, s):
        self.question_number = q
        self.total_questions = t
        self.confidence = c
        self.consistency = s


tests = [
    ("High Score", 85, Context(2, 10, 0.8, True)),
    ("Medium Score", 65, Context(2, 10, 0.8, True)),
    ("Low Score", 35, Context(2, 10, 0.8, True)),
    ("Low Confidence", 85, Context(2, 10, 0.3, True)),
    ("Inconsistent Evaluation", 85, Context(2, 10, 0.8, False)),
    ("Interview Complete", 85, Context(10, 10, 0.8, True))
]


for name, score, ctx in tests:
    result = decide_action(score, ctx)
    print(f"{name}: {result}")