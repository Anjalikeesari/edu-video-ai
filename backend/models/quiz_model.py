import uuid
class QuizModel:
    _store = {}
    def __init__(self, questions):
        self.id = uuid.uuid4().hex
        self.questions = questions

    @classmethod
    def create(cls, questions):
        q = cls(questions)
        cls._store[q.id] = q
        return q

    @classmethod
    def get(cls, qid):
        return cls._store.get(qid)
