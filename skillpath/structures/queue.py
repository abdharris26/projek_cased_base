# ==================================================
# CLASS QUEUE
# ==================================================
# Struktur data Queue (Antrian) menggunakan konsep
# FIFO (First In First Out), yaitu data yang masuk
# pertama akan keluar pertama.
class Queue:

    # ==================================================
    # CONSTRUCTOR
    # ==================================================
    # Menginisialisasi queue kosong
    def __init__(self):
        self.data = []

    # ==================================================
    # METHOD ENQUEUE
    # ==================================================
    # Menambahkan data ke bagian belakang antrian
    def enqueue(self, data):
        self.data.append(data)

    # ==================================================
    # METHOD DEQUEUE
    # ==================================================
    # Mengambil dan menghapus data paling depan
    # dari antrian
    def dequeue(self):
        # Jika queue kosong
        if len(self.data) == 0:
            return None

        # Mengambil data pertama
        data = self.data[0]
        # Menghapus data pertama dari queue
        del self.data[0]

        # Mengembalikan data yang diambil
        return data