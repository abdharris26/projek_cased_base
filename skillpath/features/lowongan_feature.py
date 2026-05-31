from models.lowongan import Lowongan

def tambah_lowongan(linked_list):
    id_lowongan = input("ID : ")
    posisi = input("posisi : ")
    perusahaan = input("Perusahaan : ")
    gaji = int(input("Gaji : "))
    tanggal = input("Tanggal : ")
    status = "Aktif"

    lowongan = Lowongan(
        id_lowongan,
        posisi,
        perusahaan,
        gaji,
        tanggal,
        status
    )

    linked_list.tambah(lowongan)

    print("Lowongan berhasil ditambah")