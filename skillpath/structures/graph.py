# ==================================================
# CLASS GRAPH
# ==================================================
# Struktur data Graph digunakan untuk menyimpan
# relasi antara skill dan pekerjaan yang sesuai.
class Graph:
    # ==================================================
    # CONSTRUCTOR
    # ==================================================
    # Menginisialisasi graph kosong menggunakan dictionary
    def __init__(self):
        self.data = {}

    # ==================================================
    # METHOD TAMBAH RELASI
    # ==================================================
    # Menambahkan hubungan antara skill dan pekerjaan
    def tambah_relasi(self, skill, pekerjaan):
        self.data[skill] = pekerjaan

    # ==================================================
    # METHOD REKOMENDASI
    # ==================================================
    # Menampilkan rekomendasi pekerjaan berdasarkan skill
    def rekomendasi(self, skill):

        # Jika skill ditemukan dalam graph
        if skill in self.data:
            print("Rekomendasi :", self.data[skill])
        # Jika skill tidak ditemukan
        else:
            print("Tidak ada rekomendasi")