# ==================================================
# FUNGSI CARI LOWONGAN
# ==================================================
# Fungsi ini digunakan untuk mencari lowongan
# berdasarkan posisi pekerjaan menggunakan
# metode Linear Search.
def cari_lowongan(data, posisi):

    # Inisialisasi indeks untuk traversal data
    i = 0

    # Menelusuri seluruh data lowongan
    while i < len(data):

        # Jika posisi yang dicari ditemukan
        if data[i].posisi == posisi:
            return data[i]

        # Pindah ke data berikutnya
        i = i + 1

    # Jika data tidak ditemukan
    return None