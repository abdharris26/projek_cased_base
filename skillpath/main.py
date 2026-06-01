#==================================================
#IMPORT STRUCTURES
#==================================================
from structures.single_linked_list import SingleLinkedList
from structures.double_linked_list import DoubleLinkedList
from structures.circular_linked_list import CircularLinkedList

from structures.stack import Stack
from structures.queue import Queue
from structures.hash_table import HashTable
from structures.graph import Graph
from structures.tree import TreeNode

#==================================================
#IMPORT FEATURES
#==================================================
from features.login_feature import login
from features.apply_feature import apply_job, undo_apply
from features.recommendation_feature import tampil_rekomendasi

# IMPORT FITUR LOWONGAN LENGKAP
from features.lowongan_feature import (
    tambah_lowongan, 
    edit_lowongan, 
    hapus_lowongan, 
    sorting_lowongan, 
    cari_lowongan_by_keyword
)

#==================================================
#IMPORT MODELS
#==================================================
from models.lowongan import Lowongan
from models.pelamar import Pelamar
from models.hrd import HRD

#==================================================
#ININISIALISASI DATA STRUCTURES
#==================================================
data_lowongan = SingleLinkedList() 
histori_lamaran = DoubleLinkedList()
undo = Stack()
antrian = Queue()

# CIRCULAR LINKED LIST (HOT JOBS)
hot_jobs = CircularLinkedList()
hot_jobs.tambah("AI Support")
hot_jobs.tambah("Data Analyst")
hot_jobs.tambah("Cyber Security")

# HASH TABLE (LOGIN USER)
# Menyimpan username dan password pengguna.
# Admin memiliki akses penuh sedangkan user hanya
# dapat mengakses fitur pelamar.
akun = HashTable()
akun.tambah_user("admin", "123")
akun.tambah_user("user", "123")

# GRAPH (REKOMENDASI)
# Menyimpan relasi antara skill dan pekerjaan
# yang direkomendasikan.
graph = Graph()
graph.tambah_relasi("Python", "Python Developer")
graph.tambah_relasi("Design", "UI UX Designer")

# TREE (STRUKTUR PERUSAHAAN)
perusahaan = TreeNode("CEO")
hrd = TreeNode("HRD")
finance = TreeNode("Finance")
it = TreeNode("IT Division")
backend = TreeNode("Backend Developer")
frontend = TreeNode("Frontend Developer")
cyber = TreeNode("Cyber Security")

perusahaan.tambah_child(hrd)
perusahaan.tambah_child(finance)
perusahaan.tambah_child(it)
it.tambah_child(backend)
it.tambah_child(frontend)
it.tambah_child(cyber)

#==================================================
#DATA USER LOGGED IN
#==================================================
role_user = None  # Menyimpan role: 'admin', 'user', atau None jika belum login
nama_user = " "
skill_user = set()

#==================================================
#PROGRAM UTAMA
#==================================================
jalan = True

while jalan:
    print("\n====== SKILLPATH ======")
    if role_user is not None:
        print(f"--- [STATUS: LOGGED IN AS {role_user.upper()} ({nama_user})] ---")
    else:
        print("--- [STATUS: BELUM LOGIN] ---")
        
    print("1. Login")
    print("2. Tambah Lowongan (Admin)")
    print("3. Tampilkan Semua Lowongan")
    print("4. Edit Lowongan")
    print("5. Hapus Lowongan (Admin)")
    print("6. Sorting Lowongan (Admin)")
    print("7. Cari Lowongan")
    print("8. Hot Jobs")
    print("9. Rekomendasi")
    print("10. Tambah Skill")
    print("11. Apply Job")
    print("12. Undo Apply")
    print("13. Histori Lamaran")
    print("14. Tampilkan Profil")
    print("15. Struktur Perusahaan")
    print("16. Proses Antrian Pelamar")
    print("17. Keluar / Logout")

    pilih = input("\nPilih menu : ")

    # ==================================================
    # VALIDASI HAK AKSES (ROLE-BASED ACCESS CONTROL)
    # ==================================================
    
    # 1. Jika belum login, hanya boleh akses menu 1, 3, 7, 8, 15, dan 17
    if role_user is None and pilih not in ["1", "3", "7", "8", "15", "17"]:
        print("\n[!] Akses ditolak! Anda harus login (Menu 1) terlebih dahulu.")
        continue
        
    # 2. Jika login sebagai USER, dilarang mengakses menu khusus ADMIN (2, 5, 6, 16)
    elif role_user == "user" and pilih in ["2", "5", "6", "16"]:
        print(f"\n[!] Akses ditolak! Akun '{nama_user}' tidak memiliki hak akses Admin untuk menu ini.")
        continue
        
    # 3. Jika login sebagai ADMIN, dilarang mengakses menu khusus USER (9, 10, 11, 12, 13, 14)
    elif role_user == "admin" and pilih in ["9", "10", "11", "12", "13", "14"]:
        print(f"\n[!] Akses ditolak! Menu ini hanya khusus untuk akun User/Pelamar.")
        continue

    # ==================================================
    # EKSEKUSI MENU
    # ==================================================
    if pilih == "1":
        hasil_login = login(akun)
        if hasil_login is not None:
            nama_user = hasil_login
            role_user = "admin" if hasil_login == "admin" else "user"

    elif pilih == "2":
        tambah_lowongan(data_lowongan)

    elif pilih == "3":
        print("\n===== DATA LOWONGAN =====")
        data_lowongan.tampilkan()

    elif pilih == "4":
        # Menyesuaikan parameter agar fungsi edit di lowongan_feature tahu siapa yang sedang mengedit
        edit_lowongan(data_lowongan, role_user, nama_user)

    elif pilih == "5":
        hapus_lowongan(data_lowongan)

    elif pilih == "6":
        sorting_lowongan(data_lowongan)

    elif pilih == "7":
        cari_lowongan_by_keyword(data_lowongan)

    elif pilih == "8":
        print("\n===== HOT JOBS =====")
        hot_jobs.tampilkan()

    elif pilih == "9":
        skill = input("Skill : ")
        print("\n===== REKOMENDASI =====")
        tampil_rekomendasi(graph, skill)
    
    elif pilih == "10":
        skill_baru = input("Masukkan skill: ")
        skill_user.add(skill_baru)
        print("Skill berhasil ditambahkan")

    elif pilih == "11":
        nama = input("Nama : ")
        pekerjaan = input("Pekerjaan : ")
        apply_job(antrian, undo, nama, pekerjaan)
        histori_lamaran.tambah(pekerjaan)
        print("Histori lamaran ditambahkan")

    elif pilih == "12":
        undo_apply(undo)

    elif pilih == "13":
        print("\n===== HISTORI LAMARAN =====")
        histori_lamaran.tampil_maju()

    elif pilih == "14":
        profil_user = {
            "Nama": nama_user,
            "Skill": skill_user
        }
        print("\n===== PROFIL USER =====")
        print("Nama: ", profil_user["Nama"])
        print("Skill: ", profil_user["Skill"])

    elif pilih == "15":
        print("\n===== STRUKTUR PERUSAHAAN =====")
        perusahaan.tampilkan()

    elif pilih == "16":
        print("\n===== PROSES ANTRIAN =====")
        proses = antrian.dequeue()
        if proses is not None:
            print("Pelamar diproses: ", proses)
        else:
            print("Antrian kosong")

    elif pilih == "17":
        if role_user is not None:
            print(f"\nAkun {nama_user} berhasil logout kembali ke menu utama.")
            role_user = None
            nama_user = " "
        else:
            jalan = False
            print("Program selesai")
            
    else:
        print("Menu tidak tersedia")