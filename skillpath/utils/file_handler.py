# ==================================================
# FUNGSI SIMPAN LOWONGAN
# ==================================================
# Fungsi ini digunakan untuk menyimpan data lowongan
# ke dalam file teks (lowongan.txt).
def simpan_lowongan(data):

    # Membuka file dalam mode write (menulis ulang isi file)
    file = open("database/lowongan.txt", "w")

    # Inisialisasi indeks untuk traversal data
    i = 0

    # Menelusuri seluruh data lowongan
    while i < len(data):

        # Menggabungkan posisi dan perusahaan
        # menjadi satu baris teks
        teks = data[i].posisi + ";" + data[i].perusahaan + "\n"

        # Menulis data ke file
        file.write(teks)

        # Pindah ke data berikutnya
        i = i + 1

    # Menutup file setelah selesai digunakan
    file.close()