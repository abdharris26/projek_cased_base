from structures.hash_table import HashTable

akun = HashTable()

akun.tambah_user("admin", "123")
akun.tambah_user("user", "123")


def login():
    username = input("Username : ")
    password = input("Password : ")

    hasil = akun.login(username, password)

    if hasil:
        print("Login Berhasil")
        return username
    else:
        print("Login Gagal")
        return None