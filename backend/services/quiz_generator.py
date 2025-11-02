import random

def generate_mcq(question_text, choices, answer_index):
    return {
        "type": "mcq",
        "question": question_text,
        "choices": choices,
        "answer": answer_index
    }

def simple_extract_keypoints(summary):
    # Very naive: treat sentences as keypoints
    sents = [s.strip() for s in summary.split('.') if s.strip()]
    return sents[:5]

def generate_quiz_for_summary(summary, num_questions=5):
    keypoints = simple_extract_keypoints(summary)
    questions = []
    for i, kp in enumerate(keypoints[:num_questions]):
        correct = kp
        # fabricate distractors by truncating/altering correct
        distractors = []
        words = correct.split()
        if len(words) > 3:
            distractors.append(" ".join(words[1:]))
            distractors.append(" ".join(words[:-1]))
        else:
            distractors.append(correct + " (not)")
            distractors.append("Opposite of " + correct)
        choices = [correct] + distractors
        random.shuffle(choices)
        answer_index = choices.index(correct)
        questions.append(generate_mcq(f"What is the key idea: '{kp[:80]}...'? ", choices, answer_index))
    return questions
