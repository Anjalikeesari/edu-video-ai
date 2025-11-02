from services.quiz_generator import generate_quiz_for_summary
def test_quiz_gen():
    summary = "Point one. Point two. Point three."
    quiz = generate_quiz_for_summary(summary)
    assert isinstance(quiz, list)
    assert len(quiz) >= 1
