import os
from pathlib import Path
import uuid
import subprocess
from dotenv import load_dotenv
load_dotenv()
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

def save_upload(file_obj, folder=UPLOAD_FOLDER):
    ext = os.path.splitext(file_obj.filename)[1] or ".mp4"
    fname = f"{uuid.uuid4().hex}{ext}"
    path = os.path.join(folder, fname)
    file_obj.save(path)
    return path

def extract_audio(video_path, out_audio_path=None):
    if out_audio_path is None:
        out_audio_path = f"{os.path.splitext(video_path)[0]}.wav"
    # use ffmpeg to extract audio; ensure ffmpeg exists on system
    cmd = ["ffmpeg", "-y", "-i", video_path, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", out_audio_path]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out_audio_path

def transcribe_audio(video_path):
    """
    Simple wrapper: extract audio then call a transcription model (Whisper placeholder).
    Replace with actual API/model call.
    """
    audio_path = extract_audio(video_path)
    # placeholder simple stub: return filename as "transcript"
    # Replace with whisper or cloud STT call
    fake_transcript = f"Transcript of {os.path.basename(video_path)} — (placeholder)."
    return fake_transcript
