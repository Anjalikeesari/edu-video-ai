def adjust_difficulty(previous_performance):
    """
    previous_performance: dict {correct: int, total: int}
    returns difficulty label.
    """
    if previous_performance["total"] == 0:
        return "medium"
    pct = previous_performance["correct"] / previous_performance["total"]
    if pct >= 0.85:
        return "hard"
    if pct >= 0.6:
        return "medium"
    return "easy"
