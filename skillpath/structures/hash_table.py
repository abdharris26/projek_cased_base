class HashTable:
    def __init__(self):
        self.data = {}

    def tambah_user(self, username, password):
        self.data[username] = password

    def login(self, username, password):
        if username in self.data:
            if self.data[username] == password:
                return True

        return False