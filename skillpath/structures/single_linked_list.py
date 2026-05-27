class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
        else:
            current_lowongan = self.head

            while current_lowongan.next is not None:
                current_lowongan = current_lowongan.next

            current_lowongan.next = node_baru

    def tampilkan(self):
        current_lowongan = self.head

        while current_lowongan is not None:
            current_lowongan.data.tampilkan()
            print("-------------------")
            current_lowongan = current_lowongan.next