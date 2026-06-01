# ==================================================
# CLASS HRD
# ==================================================
class HRD:

    # Constructor untuk menyimpan data HRD
    def __init__(self, nama, perusahaan):
        self.nama = nama
        self.perusahaan = perusahaan

    # Menampilkan data HRD
    def tampilkan(self):
        print("Nama HRD :", self.nama)
        print("Perusahaan :", self.perusahaan)