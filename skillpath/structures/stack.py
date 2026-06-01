# ==================================================
# CLASS STACK
# ==================================================
# Struktur data Stack menggunakan konsep
# LIFO (Last In First Out), yaitu data yang terakhir
# masuk akan keluar terlebih dahulu.
class Stack:
    # ==================================================
    # CONSTRUCTOR
    # ==================================================
    # Menginisialisasi stack kosong
    def __init__(self):
        self.data = []

    # ==================================================
    # METHOD PUSH
    # ==================================================
    # Menambahkan data ke bagian atas stack
    def push(self, nilai):
        self.data.append(nilai)

    # ==================================================
    # METHOD POP
    # ==================================================
    # Mengambil dan menghapus data paling atas
    # dari stack
    def pop(self):
        # Jika stack kosong
        if len(self.data) == 0:
            return None

        # Menghapus dan mengembalikan data teratas
        return self.data.pop()