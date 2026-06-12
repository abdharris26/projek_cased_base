# ==================================================
# IMPORT STRUCTURES
# ==================================================
# FUNGSI APPLY LOWONGAN
# ==================================================
def apply_job(antrian, undo, nama, pekerjaan):
    # Membuat data lamaran dalam bentuk string
    data = nama + " melamar " + pekerjaan

    # Menambahkan data ke dalam antrian lamaran
    antrian.enqueue(data)
    # Menyimpan data ke stack agar bisa di-undo
    undo.push(data)

    # Menampilkan pesan berhasil
    print("Lamaran berhasil dikirim")

# ==================================================
# FUNGSI UNDO APPLY
# ==================================================
def undo_apply(undo):
    # Mengambil data terakhir dari stack
    data = undo.pop()

    # Jika masih ada data di stack
    if data is not None:
        print("Undo :", data)
    # Jika stack kosong
    else:
        print("Tidak ada data")