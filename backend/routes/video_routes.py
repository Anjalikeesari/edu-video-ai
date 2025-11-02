import os
from flask import Blueprint, request, jsonify, current_app
from services.video_processing import save_upload, transcribe_audio
from services.summarizer import summarize_transcript
from models.video_model import VideoModel

video_bp = Blueprint('video', __name__)

@video_bp.route('/upload', methods=['POST'])
def upload_video():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    filepath = save_upload(file, folder=current_app.config.get('UPLOAD_FOLDER'))
    transcript = transcribe_audio(filepath)  # returns text
    summary = summarize_transcript(transcript)

    # Create video record (in-memory stub or DB)
    vid = VideoModel.create(filepath=filepath, transcript=transcript, summary=summary)
    return jsonify({"video_id": vid.id, "summary": summary})

@video_bp.route('/summary/<video_id>', methods=['GET'])
def get_summary(video_id):
    vid = VideoModel.get(video_id)
    if not vid:
        return jsonify({"error": "not found"}), 404
    return jsonify({"video_id": vid.id, "summary": vid.summary})
