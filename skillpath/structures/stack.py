class Stack:
    def __init__(self):
        self.data = []

    def push(self, nilai):
        self.data.append(nilai)

    def pop(self):
        if len(self.data) == 0:
            return None

        return self.data.pop()