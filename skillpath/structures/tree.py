class TreeNode:

    def __init__(self, data):

        self.data = data
        self.children = []


    # Tambah child
    def tambah_child(self, child_node):

        self.children.append(child_node)


    # Tampilkan tree
    def tampilkan(self, level=0):

        # Spasi sesuai level
        print("   " * level + "- " + self.data)

        # Traversal child
        i = 0

        while i < len(self.children):

            self.children[i].tampilkan(level + 1)

            i = i + 1