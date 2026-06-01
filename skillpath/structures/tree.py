# ==================================================
# CLASS TREE NODE
# ==================================================
# Struktur data Tree digunakan untuk menyimpan data
# secara hierarki (parent dan child).
class TreeNode:
    # ==================================================
    # CONSTRUCTOR
    # ==================================================
    # Menginisialisasi node tree dengan data
    # dan daftar child yang masih kosong
    def __init__(self, data):
        self.data = data
        self.children = []

    # ==================================================
    # METHOD TAMBAH CHILD
    # ==================================================
    # Menambahkan node anak (child) ke node saat ini
    def tambah_child(self, child_node):
        self.children.append(child_node)

    # ==================================================
    # METHOD TAMPILKAN
    # ==================================================
    # Menampilkan struktur tree secara hierarki
    def tampilkan(self, level=0):

        # Memberikan indentasi sesuai level node
        print("  " * level + "- " + self.data)

        # Menelusuri seluruh child secara rekursif
        i = 0

        while i < len(self.children):

            # Menampilkan child pada level berikutnya
            self.children[i].tampilkan(level + 1)

            i = i + 1