# ==================================================
# IMPORT STRUCTURES
# ==================================================
# HashTable digunakan untuk menyimpan data akun
from structures.hash_table import HashTable

# ==================================================
# FUNGSI LOGIN
# ==================================================
def login(akun):
    # Meminta input username dari pengguna
    username = input("Username : ")
    # Meminta input password dari pengguna
    password = input("Password : ")

    # Memeriksa kecocokan username dan password
    hasil = akun.login(username, password)

    # Jika data login valid
    if hasil:
        print("Login Berhasil")
        # Mengembalikan username pengguna yang berhasil login
        return username
    # Jika data login tidak valid
    else:
        print("Login Gagal")
        # Mengembalikan nilai None sebagai tanda gagal login
        return None