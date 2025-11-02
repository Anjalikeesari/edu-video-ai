from services.summarizer import chunk_text
def test_chunk_text():
    text = "word " * 2000
    chunks = chunk_text(text, size=500)
    assert len(chunks) == 4
