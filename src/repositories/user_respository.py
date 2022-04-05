class UserRepo:
    def __init__(self, db, user_model):
        self._db = db
        self._user_model = user_model

    def create(self, user):
        exists = self.find_by_username(user.username)

        if exists:
            return None

        self._db.session.add(user)
        self._db.session.commit()

        return user

    def find(self, username):
        return self._db.session.query(self._user_model).filter_by(username=username).first()

    def get_all(self):
        return self._db.session.query(self._user_model).all()