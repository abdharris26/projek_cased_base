class NodeCLL:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = NodeCLL(data)

        if self.head is None:
            self.head = node_baru
            node_baru.next = self.head
        else:
            current_hotjob = self.head

            while current_hotjob.next != self.head:
                current_hotjob = current_hotjob.next

            current_hotjob.next = node_baru
            node_baru.next = self.head

    def tampilkan(self):
        if self.head is None:
            print("Data kosong")
        else:
            current_hotjob = self.head

            while True:
                print(current_hotjob.data)
                current_hotjob = current_hotjob.next
                if current_hotjob == self.head:
                    break