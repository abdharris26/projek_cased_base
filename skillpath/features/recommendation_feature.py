# ==================================================
# IMPORT STRUCTURES
# ==================================================
# Graph digunakan untuk menyimpan relasi skill
# dan memberikan rekomendasi pekerjaan
# ==================================================
# FITUR REKOMENDASI PEKERJAAN
# ==================================================
def tampil_rekomendasi(graph, skill):
    # Menampilkan rekomendasi pekerjaan
    # berdasarkan skill yang dimasukkan pengguna
    graph.rekomendasi(skill)