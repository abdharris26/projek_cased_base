# ==================================================
# FITUR STATISTIK LOWONGAN
# ==================================================
def statistik_lowongan(data):
    # Menampilkan jumlah total lowongan
    # berdasarkan banyaknya data yang tersimpan
    count = 0
    current = data.head

    while current is not None:
        count += 1
        current = current.next

    print("Total lowongan :", count)