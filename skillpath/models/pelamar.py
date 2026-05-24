class Pelamar:
    def __init__(self, nama, skill):
        self.nama = nama
        self.skill = skill
        self.riwayat = []

    def tambah_riwayat(self, lowongan):
        self.riwayat.append(lowongan)

    def tampilkan(self):
        print("Nama :", self.nama)
        print("Skill :", self.skill)