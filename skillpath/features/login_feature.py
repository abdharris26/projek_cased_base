from structures.hash_table import HashTable

def login(akun):
    username = input("Username : ")
    password = input("Password : ")

    hasil = akun.login(username, password)

    if hasil:
        print("Login Berhasil")
        return username
    else:
        print("Login Gagal")
        return None