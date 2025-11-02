from models.user_model import UserModel
def test_user_create():
    u = UserModel.create("alice")
    assert u.username == "alice"
    assert UserModel.get(u.id) is not None
