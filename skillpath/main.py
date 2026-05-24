from structures.single_linked_list import SingleLinkedList
from features.login_feature import login
from features.lowongan_feature import tambah_lowongan
from features.apply_feature import apply_job
from features.apply_feature import undo_apply
from features.recommendation_feature import tampil_rekomendasi

data_lowongan = SingleLinkedList() 

jalan = True

while jalan:

    print("====== SKILLPATH ======")
    print("1. Login")
    print("2. Tambah Lowongan")
    print("3. Tampilkan Lowongan")
    print("4. Apply Job")
    print("5. Undo Apply")
    print("6. Rekomendasi") 
    print("7. Keluar")

    pilih = input("Pilih menu : ")

    if pilih == "1":
        login()

    elif pilih == "2":
        tambah_lowongan(data_lowongan)

    elif pilih == "3":
        data_lowongan.tampilkan()

    elif pilih == "4":
        nama = input("Nama : ")
        pekerjaan = input("Pekerjaan : ")

        apply_job(nama, pekerjaan)

    elif pilih == "5":
        undo_apply()

    elif pilih == "6":
        skill = input("Skill : ")

        tampil_rekomendasi(skill)

    elif pilih == "7":
        jalan = False

    else:
        print("Menu tidak tersedia")