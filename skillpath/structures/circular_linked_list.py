# ==================================================
# CLASS NODE CIRCULAR LINKED LIST
# ==================================================
# Node digunakan untuk menyimpan data dan pointer
# ke node berikutnya.
class NodeCLL:

    # Constructor node
    def __init__(self, data):
        self.data = data
        self.next = None


# ==================================================
# CLASS CIRCULAR LINKED LIST
# ==================================================
# Struktur data Circular Linked List, di mana node
# terakhir akan menunjuk kembali ke node pertama.
class CircularLinkedList:

    # ==================================================
    # CONSTRUCTOR
    # ==================================================
    # Menginisialisasi linked list kosong
    def __init__(self):
        self.head = None

    # ==================================================
    # METHOD TAMBAH
    # ==================================================
    # Menambahkan node baru ke akhir Circular Linked List
    def tambah(self, data):
        node_baru = NodeCLL(data)

        # Jika linked list masih kosong
        if self.head is None:
            self.head = node_baru
            node_baru.next = self.head
        # Jika linked list sudah memiliki node
        else:
            current_hotjob = self.head

            # Mencari node terakhir
            while current_hotjob.next != self.head:
                current_hotjob = current_hotjob.next

            # Menghubungkan node terakhir dengan node baru
            current_hotjob.next = node_baru

            # Node baru menunjuk kembali ke head
            node_baru.next = self.head

    # ==================================================
    # METHOD TAMPILKAN
    # ==================================================
    # Menampilkan seluruh data dalam Circular Linked List
    def tampilkan(self):

        # Jika linked list kosong
        if self.head is None:
            print("Data kosong")
        # Jika linked list memiliki data
        else:
            current_hotjob = self.head

            while True:
                print(current_hotjob.data)
                current_hotjob = current_hotjob.next

                # Berhenti jika sudah kembali ke head
                if current_hotjob == self.head:
                    break