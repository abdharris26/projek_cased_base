# ==================================================
# FUNGSI BUBBLE SORT GAJI
# ==================================================
# Fungsi ini digunakan untuk mengurutkan data
# lowongan berdasarkan gaji dari terbesar ke terkecil
# menggunakan algoritma Bubble Sort.
def bubble_sort_gaji(data):
    # Menyimpan jumlah data yang akan diurutkan
    panjang = len(data)

    # Perulangan utama Bubble Sort
    i = 0

    while i < panjang:

        # Indeks untuk membandingkan elemen yang berdekatan
        j = 0

        while j < panjang - 1:

            # Jika gaji saat ini lebih kecil dari gaji berikutnya
            # maka posisi kedua data ditukar
            if data[j].gaji < data[j + 1].gaji:

                sementara = data[j]
                data[j] = data[j + 1]
                data[j + 1] = sementara

            # Pindah ke pasangan data berikutnya
            j = j + 1

        # Melanjutkan ke putaran berikutnya
        i = i + 1