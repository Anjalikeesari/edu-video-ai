import uuid
class UserModel:
    _store = {}
    def __init__(self, username):
        self.id = uuid.uuid4().hex
        self.username = username
        self.progress = {}

    @classmethod
    def create(cls, username):
        u = cls(username)
        cls._store[u.id] = u
        return u

    @classmethod
    def get(cls, uid):
        return cls._store.get(uid)
