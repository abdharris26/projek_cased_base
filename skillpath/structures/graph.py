class Graph:
    def __init__(self):
        self.data = {}

    def tambah_relasi(self, skill, pekerjaan):
        self.data[skill] = pekerjaan

    def rekomendasi(self, skill):
        if skill in self.data:
            print("Rekomendasi :", self.data[skill])
        else:
            print("Tidak ada rekomendasi")