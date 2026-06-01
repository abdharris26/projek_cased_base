# ==================================================
# CLASS NODE DOUBLE LINKED LIST
# ==================================================
# Node digunakan untuk menyimpan data serta pointer
# ke node berikutnya (next) dan sebelumnya (prev).
class NodeDLL:
    # Constructor node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# ==================================================
# CLASS DOUBLE LINKED LIST
# ==================================================
# Struktur data Double Linked List yang memungkinkan
# traversal maju dan mundur.
class DoubleLinkedList:
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
        node_baru = NodeDLL(data)

        # Jika linked list masih kosong
        if self.head is None:
            self.head = node_baru
        # Jika linked list sudah memiliki data
        else:
            current_riwayat = self.head

            # Mencari node terakhir
            while current_riwayat.next is not None:
                current_riwayat = current_riwayat.next

            # Menghubungkan node terakhir dengan node baru
            current_riwayat.next = node_baru
            node_baru.prev = current_riwayat

    # ==================================================
    # METHOD TAMPIL MAJU
    # ==================================================
    # Menampilkan data dari awal ke akhir
    def tampil_maju(self):

        # Jika linked list kosong
        if self.head is None:
            print("Data kosong")
        # Jika linked list memiliki data
        else:
            current_riwayat = self.head

            while current_riwayat is not None:
                print(current_riwayat.data)
                current_riwayat = current_riwayat.next

    # ==================================================
    # METHOD TAMPIL MUNDUR
    # ==================================================
    # Menampilkan data dari akhir ke awal
    def tampil_mundur(self):

        # Jika linked list kosong
        if self.head is None:
            print("Data kosong")
        # Jika linked list memiliki data
        else:
            current_riwayat = self.head

            # Mencari node terakhir
            while current_riwayat.next is not None:
                current_riwayat = current_riwayat.next

            # Menampilkan data dari belakang ke depan
            while current_riwayat is not None:
                print(current_riwayat.data)
                current_riwayat = current_riwayat.prev