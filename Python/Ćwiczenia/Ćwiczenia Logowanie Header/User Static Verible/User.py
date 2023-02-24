
class User:
    lastUserId = 0

    def __init__(self, name):
        User.lastUserId += 1
        self.id = User.lastUserId
        self.name = name
