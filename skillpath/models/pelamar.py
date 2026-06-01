# ==================================================
# CLASS PELAMAR
# ==================================================
# Class ini digunakan untuk menyimpan data pelamar
# beserta skill dan riwayat lamarannya.
class Pelamar:
    # CONSTRUCTOR
    # Menginisialisasi data pelamar
    def __init__(self, nama, skill):
        self.nama = nama
        self.skill = skill
        self.riwayat = []

    # METHOD TAMBAH RIWAYAT
    # Menambahkan data lowongan yang pernah dilamar
    # ke dalam riwayat pelamar
    def tambah_riwayat(self, lowongan):
        self.riwayat.append(lowongan)

    # METHOD TAMPILKAN
    # Menampilkan informasi pelamar
    def tampilkan(self):
        print("Nama :", self.nama)
        print("Skill :", self.skill)