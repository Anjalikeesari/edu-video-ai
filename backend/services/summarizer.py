from ai_models.summarization_prompt import PROMPT_TEMPLATE

def chunk_text(text, size=800):
    words = text.split()
    chunks = []
    for i in range(0, len(words), size):
        chunks.append(" ".join(words[i:i+size]))
    return chunks

def summarize_transcript(transcript):
    """
    Minimal LLM prompt-based summarization stub.
    Replace with OpenAI/HF model calls.
    """
    # naive summary: pick first 3 sentences or shorten
    sentences = transcript.split('.')
    summary = '.'.join([s.strip() for s in sentences[:3] if s.strip()])
    if not summary:
        summary = transcript[:800] + ("..." if len(transcript) > 800 else "")
    return summary
