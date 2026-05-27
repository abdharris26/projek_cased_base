from structures.single_linked_list import SingleLinkedList
from structures.double_linked_list import DoubleLinkedList
from structures.circular_linked_list import CircularLinkedList

from features.login_feature import login
from features.lowongan_feature import tambah_lowongan
from features.apply_feature import apply_job
from features.apply_feature import undo_apply
from features.recommendation_feature import tampil_rekomendasi

from models.pelamar import Pelamar

data_lowongan = SingleLinkedList() 

hot_jobs = CircularLinkedList()
hot_jobs.tambah("AI Support")
hot_jobs.tambah("Data Analyst")
hot_jobs.tambah("Cyber Security")

histori_lamaran = DoubleLinkedList()

nama_user = " "
skill_user = set()


jalan = True

while jalan:

    print("====== SKILLPATH ======")
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
    print("11. Keluar")

    pilih = input("Pilih menu : ")

    if pilih == "1":
        login()

    elif pilih == "2":
        tambah_lowongan(data_lowongan)

    elif pilih == "3":
        print("\n===== DATA LOWONGAN =====")
        data_lowongan.tampilkan()

    elif pilih == "4":
        nama = input("Nama : ")
        pekerjaan = input("Pekerjaan : ")

        apply_job(nama, pekerjaan)

        histori_lamaran.tambah(pekerjaan)
        print("Histori lamaran ditambahkan")

    elif pilih == "5":
        undo_apply()

    elif pilih == "6":
        skill = input("Skill : ")

        tampil_rekomendasi(skill)

    elif pilih == "7":
        print("\n===== HOT JOBS =====")
        hot_jobs.tampilkan()

    elif pilih == "8":
        print("\n===== HISTORI LAMARAN =====")
        histori_lamaran.tampil_maju()
    
    elif pilih == "9":
        skill_baru = input("Masukkan skill: ")

        skill_user.add(skill_baru)
        print("Skill berhasil ditambahkan")

    elif pilih == "10":
        profil_user = {
            "Nama": nama_user,
            "Skill": skill_user
        }
        print("\n===== PROFIL USER =====")
        print("Nama: ", profil_user["Nama"])
        print("Skill: ", profil_user["Skill"])

    elif pilih == "11":
        jalan = False
        print("Program selesai")

    else:
        print("Menu tidak tersedia")