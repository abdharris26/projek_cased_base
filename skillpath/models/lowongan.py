class Lowongan:
    def __init__(self, id_lowongan, posisi, perusahaan, gaji, tanggal, status):
        self.id_lowongan = id_lowongan
        self.posisi = posisi
        self.perusahaan = perusahaan
        self.gaji = gaji
        self.tanggal = tanggal
        self.status = status

    def tampilkan(self):
        print("ID :", self.id_lowongan)
        print("Posisi :", self.posisi)
        print("Perusahaan :", self.perusahaan)
        print("Gaji :", self.gaji)
        print("Tanggal :", self.tanggal)
        print("Status :", self.status)