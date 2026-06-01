# ==================================================
# IMPORT STRUCTURES
# ==================================================
# Graph digunakan untuk menyimpan relasi skill
# dan memberikan rekomendasi pekerjaan
from structures.graph import Graph

# ==================================================
# FITUR REKOMENDASI PEKERJAAN
# ==================================================
def tampil_rekomendasi(graph, skill):
    # Menampilkan rekomendasi pekerjaan
    # berdasarkan skill yang dimasukkan pengguna
    graph.rekomendasi(skill)