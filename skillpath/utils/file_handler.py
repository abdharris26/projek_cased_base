# ==================================================
# FUNGSI SIMPAN LOWONGAN
# ==================================================
# Fungsi ini digunakan untuk menyimpan data lowongan
# ke dalam file teks (lowongan.txt).
def simpan_lowongan(data_lowongan):

    # Membuka file dalam mode write (menulis ulang isi file)
    file = open("database/lowongan.txt", "w")

    current = data_lowongan.head
    # Menelusuri seluruh data lowongan
    while current is not None:
        # Menggabungkan posisi dan perusahaan
        teks = current.data.posisi + ";" + current.data.perusahaan + "\n"
        # Menulis data ke file
        file.write(teks)

        # Pindah ke data berikutnya
        current = current.next

    # Menutup file setelah selesai digunakan
    file.close()