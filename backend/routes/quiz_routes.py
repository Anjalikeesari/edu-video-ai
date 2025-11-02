from flask import Blueprint, request, jsonify
from services.quiz_generator import generate_quiz_for_summary
from models.quiz_model import QuizModel

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/generate', methods=['POST'])
def generate_quiz():
    data = request.json or {}
    summary = data.get('summary')
    if not summary:
        return jsonify({"error": "summary required"}), 400

    quiz = generate_quiz_for_summary(summary)
    quiz_record = QuizModel.create(questions=quiz)
    return jsonify({"quiz_id": quiz_record.id, "questions": quiz})

@quiz_bp.route('/<quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    q = QuizModel.get(quiz_id)
    if not q:
        return {"error": "not found"}, 404
    return {"quiz_id": q.id, "questions": q.questions}
