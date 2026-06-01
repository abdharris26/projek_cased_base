# ==================================================
# CLASS NODE SINGLE LINKED LIST
# ==================================================
# Node digunakan untuk menyimpan data dan pointer
# ke node berikutnya.
class Node:
    # Constructor node
    def __init__(self, data):
        self.data = data
        self.next = None


# ==================================================
# CLASS SINGLE LINKED LIST
# ==================================================
# Struktur data Single Linked List yang digunakan
# untuk menyimpan data lowongan secara berurutan.
class SingleLinkedList:
    # ==================================================
    # CONSTRUCTOR
    # ==================================================
    # Menginisialisasi linked list kosong
    def __init__(self):
        self.head = None

    # ==================================================
    # METHOD TAMBAH
    # ==================================================
    # Menambahkan node baru ke akhir linked list
    def tambah(self, data):
        node_baru = Node(data)

        # Jika linked list masih kosong
        if self.head is None:
            self.head = node_baru
        # Jika linked list sudah memiliki data
        else:
            current_lowongan = self.head

            # Mencari node terakhir
            while current_lowongan.next is not None:
                current_lowongan = current_lowongan.next

            # Menghubungkan node terakhir dengan node baru
            current_lowongan.next = node_baru

    # ==================================================
    # METHOD TAMPILKAN
    # ==================================================
    # Menampilkan seluruh data dalam linked list
    def tampilkan(self):
        current_lowongan = self.head

        # Menelusuri linked list dari awal hingga akhir
        while current_lowongan is not None:

            # Menampilkan data lowongan
            current_lowongan.data.tampilkan()
            print("--------------------")

            # Berpindah ke node berikutnya
            current_lowongan = current_lowongan.next