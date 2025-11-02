from services.summarizer import summarize_transcript
def test_summarizer_basic():
    t = "This is a test. It has multiple sentences. Final sentence."
    s = summarize_transcript(t)
    assert "test" in s.lower()
