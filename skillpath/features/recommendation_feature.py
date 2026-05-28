from structures.graph import Graph

graph = Graph()

graph.tambah_relasi("Python", "Python Developer")
graph.tambah_relasi("Design", "UI UX Designer")


def tampil_rekomendasi(skill):
    graph.rekomendasi(skill)