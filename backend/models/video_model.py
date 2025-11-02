import uuid

class VideoModel:
    _store = {}

    def __init__(self, filepath, transcript, summary):
        self.id = uuid.uuid4().hex
        self.filepath = filepath
        self.transcript = transcript
        self.summary = summary

    @classmethod
    def create(cls, filepath, transcript, summary):
        v = cls(filepath, transcript, summary)
        cls._store[v.id] = v
        return v

    @classmethod
    def get(cls, vid):
        return cls._store.get(vid)
