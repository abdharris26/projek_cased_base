# ==================================================
# CLASS HASH TABLE
# ==================================================
# Struktur data Hash Table digunakan untuk menyimpan
# data akun pengguna berupa username dan password.
class HashTable:
    # ==================================================
    # CONSTRUCTOR
    # ==================================================
    # Menginisialisasi hash table kosong menggunakan dictionary
    def __init__(self):
        self.data = {}

    # ==================================================
    # METHOD TAMBAH USER
    # ==================================================
    # Menambahkan username dan password ke hash table
    def tambah_user(self, username, password):
        self.data[username] = password

    # ==================================================
    # METHOD LOGIN
    # ==================================================
    # Memvalidasi username dan password pengguna
    def login(self, username, password):
        # Memeriksa apakah username tersedia
        if username in self.data:
            # Memeriksa kecocokan password
            if self.data[username] == password:
                return True
        # Login gagal jika username tidak ditemukan
        # atau password tidak sesuai
        return False