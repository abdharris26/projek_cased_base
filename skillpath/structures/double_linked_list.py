class NodeDLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = NodeDLL(data)

        if self.head is None:
            self.head = node_baru
        else:
            current_riwayat = self.head

            while current_riwayat.next is not None:
                current_riwayat = current_riwayat.next

            current_riwayat.next = node_baru
            node_baru.prev = current_riwayat

    def tampil_maju(self):
        if self.head is None:
            print("Data kosong")
        else:
            current_riwayat = self.head

            while current_riwayat is not None:
                print(current_riwayat.data)
                current_riwayat = current_riwayat.next

    def tampil_mundur(self):
        if self.head is None:
            print("Data kosong")
        else:
            current_riwayat = self.head

            while current_riwayat.next is not None:
                current_riwayat = current_riwayat.next

            while current_riwayat is not None:
                print(current_riwayat.data)
                current_riwayat = current_riwayat.prev