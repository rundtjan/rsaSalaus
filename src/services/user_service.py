from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    def __init__(self, user_repo, user_model):
        self._user_repo = user_repo
        self._user_model = user_model

    def check_login(self, username, pword):
        user = self._user_repo.find(username)

        if not user or not check_password_hash(user.pword, pword):
            return None

        return user

    def create(self, username, pword):
        user = self._user_repo.create(
            self._user_model(
                username,
                generate_password_hash(pword, method='sha256'))
        )

        return user

    def username_is_free(self, username):
        if self._user_repo.find(username):
            return False
        return True