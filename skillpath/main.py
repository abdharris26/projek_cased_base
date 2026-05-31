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
from features.lowongan_feature import tambah_lowongan
from features.apply_feature import apply_job
from features.apply_feature import undo_apply
from features.recommendation_feature import tampil_rekomendasi

#==================================================
#IMPORT MODELS
#==================================================
from models.lowongan import Lowongan
from models.pelamar import Pelamar
from models.hrd import HRD

#==================================================
#SINGLE LINKED LIST (DATA LOWONGAN)
#==================================================
data_lowongan = SingleLinkedList() 

#==================================================
#DOUBLE LINKED LIST (HISTORI LAMARAN)
#==================================================
histori_lamaran = DoubleLinkedList()

#==================================================
#CIRCULAR LINKED LIST (HOT JOBS)
#==================================================
hot_jobs = CircularLinkedList()

hot_jobs.tambah("AI Support")
hot_jobs.tambah("Data Analyst")
hot_jobs.tambah("Cyber Security")

#==================================================
#STACK (UNDO APPLY)
#==================================================
undo = Stack()

#==================================================
#QUEUE (ANTRIAN PELAMAR)
#==================================================
antrian = Queue()

#==================================================
#HASH TABLE (LOGIN USER)
#==================================================
akun = HashTable()

akun.tambah_user("admin", "123")
akun.tambah_user("user", "123")

#==================================================
#GRAPH (REKOMENDASI)
#==================================================
graph = Graph()

graph.tambah_relasi("Python", "Python Developer")
graph.tambah_relasi("Design", "UI UX Designer")

#==================================================
#TREE (STRUKTUR PERUSAHAAN)
#==================================================
perusahaan = TreeNode("CEO")

hrd = TreeNode("HRD")
finance = TreeNode("Finance")
it = TreeNode("IT Division")

backend = TreeNode("Backend Developer")
frontend = TreeNode("Frontend Developer")
cyber = TreeNode("Cyber Security")

#MENGHUBUNGKAN TREE
perusahaan.tambah_child(hrd)
perusahaan.tambah_child(finance)
perusahaan.tambah_child(it)

it.tambah_child(backend)
it.tambah_child(frontend)
it.tambah_child(cyber)

#==================================================
#DATA USER
#==================================================
nama_user = " "
#SET
skill_user = set()

#==================================================
#PROGRAM UTAMA
#==================================================
jalan = True

while jalan:

    print("\n====== SKILLPATH ======")
    print("1. Login")
    print("2. Tambah Lowongan")
    print("3. Tampilkan Lowongan")
    print("4. Apply Job")
    print("5. Undo Apply")
    print("6. Rekomendasi") 
    print("7. Hot Jobs")
    print("8. Histori Lamaran")
    print("9. Tambah Skill")
    print("10. Tampilkan Profil")
    print("11. Struktur Perusahaan")
    print("12. Proses Antrian Pelamar")
    print("13. Keluar")

    pilih = input("Pilih menu : ")

    #==================================================
    #HASH TABLE (LOGIN)
    #==================================================
    if pilih == "1":
        hasil_login = login(akun)
        if hasil_login is not None:
            nama_user = hasil_login

    #==================================================
    #SINGLE LINKED LIST (TAMBAH LOWONGAN)
    #==================================================
    elif pilih == "2":
        tambah_lowongan(data_lowongan)

    #==================================================
    #TAMPILKAN LOWONGAN
    #==================================================
    elif pilih == "3":
        print("\n===== DATA LOWONGAN =====")
        data_lowongan.tampilkan()

    #==================================================
    #STACK, QUEUE, DOUBLE LINKED LIST (APPLY JOB)
    #==================================================
    elif pilih == "4":
        nama = input("Nama : ")
        pekerjaan = input("Pekerjaan : ")

        apply_job(antrian, undo, nama, pekerjaan)

        histori_lamaran.tambah(pekerjaan)
        print("Histori lamaran ditambahkan")

    #==================================================
    #STACK (UNDO APPLY)
    #==================================================
    elif pilih == "5":
        undo_apply(undo)

    #==================================================
    #GRAPH (REKOMENDASI)
    #==================================================
    elif pilih == "6":
        skill = input("Skill : ")
        print("\n===== REKOMENDASI =====")

        tampil_rekomendasi(graph, skill)

    #==================================================
    #CIRCULAR LINKED LIST (HOT JOBS)
    #==================================================
    elif pilih == "7":
        print("\n===== HOT JOBS =====")
        hot_jobs.tampilkan()

    #==================================================
    #HASH TABLE (HISTORI LAMARAN)
    #==================================================
    elif pilih == "8":
        print("\n===== HISTORI LAMARAN =====")
        histori_lamaran.tampil_maju()
    
    #==================================================
    #SET (TAMBAH SKILL)
    #================================================== 
    elif pilih == "9":
        skill_baru = input("Masukkan skill: ")

        skill_user.add(skill_baru)
        print("Skill berhasil ditambahkan")

    #==================================================
    #DICTIONARY (TAMPILKAN PORFIL)
    #==================================================
    elif pilih == "10":
        profil_user = {
            "Nama": nama_user,
            "Skill": skill_user
        }
        print("\n===== PROFIL USER =====")
        print("Nama: ", profil_user["Nama"])
        print("Skill: ", profil_user["Skill"])

    #==================================================
    #TREE (STRUKTUR PERUSAHAAN)
    #==================================================
    elif pilih == "11":
        print("\n===== STRUKTUR PERUSAHAAN =====")
        perusahaan.tampilkan()

    #==================================================
    #QUEUE (PROSES ANTRIAN)
    #==================================================
    elif pilih == "12":
        print("\n===== PROSES ANTRIAN =====")
        proses = antrian.dequeue()
        if proses is not None:
            print("Pelamar diproses: ", proses)
        else:
            print("Antrian kosong")

    #==================================================
    #KELUAR
    #==================================================
    elif pilih == "13":
        jalan = False
        print("Program selesai")

    else:
        print("Menu tidak tersedia")