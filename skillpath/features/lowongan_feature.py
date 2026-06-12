from models.lowongan import Lowongan
from utils.file_handler import simpan_lowongan
# ==================================================
# 1. FITUR TAMBAH LOWONGAN (KHUSUS ADMIN)
# ==================================================
def tambah_lowongan(linked_list):
    id_lowongan = input("ID : ")
    posisi = input("posisi : ")
    perusahaan = input("Perusahaan : ")
    gaji = int(input("Gaji : "))
    tanggal = input("Tanggal : ")
    status = "Aktif"

    data_lowongan = Lowongan(
        id_lowongan,
        posisi,
        perusahaan,
        gaji,
        tanggal,
        status
    )

    linked_list.tambah(data_lowongan)
    simpan_lowongan(linked_list)
    print("Lowongan berhasil ditambah")


# ==================================================
# 2. FITUR EDIT LOWONGAN 
# ==================================================
def edit_lowongan(linked_list, role, nama_user):
    print("\n===== EDIT DATA LOWONGAN =====")
    id_cari = input("Masukkan ID Lowongan yang ingin dicari/diedit: ")
    
    current = linked_list.head
    ketemu = False
    
    while current is not None:
        if current.data.id_lowongan == id_cari:
            ketemu = True
            print("\n--- Data Lowongan Ditemukan ---")
            current.data.tampilkan()
            print("-------------------------------")
            
            # KONDISI ADMIN: Bisa edit semua detail teks lowongan
            if role == "admin":
                print("[ Hak Akses: ADMIN ] -> Anda berhak mengubah detail informasi lowongan.")
                current.data.posisi = input("Masukkan Posisi Baru: ")
                current.data.perusahaan = input("Masukkan Perusahaan Baru: ")
                current.data.gaji = int(input("Masukkan Gaji Baru: "))
                current.data.tanggal = input("Masukkan Tanggal Baru: ")
                current.data.status = input("Masukkan Status Baru (Aktif/Tutup): ")
                simpan_lowongan(linked_list)
                print("\n[+] Detail Lowongan berhasil diperbarui oleh Admin!")
            
            # KONDISI USER: Dikunci aksinya, TIDAK BISA edit teks dari admin, cuma bisa daftar/apply
            elif role == "user":
                print("[ Hak Akses: USER/PELAMAR ]")
                print("-> Anda TIDAK BISA mengubah Posisi, Perusahaan, Gaji, atau Tanggal.")
                print("-> Anda hanya diperbolehkan memperbarui status lamaran Anda di sini.")
                
                pilihan = input("\nApakah Anda ingin mengubah status lowongan ini menjadi 'Melamar'? (y/n): ")
                if pilihan.lower() == 'y':
                    current.data.status = f"Dilamar oleh {nama_user}"
                    simpan_lowongan(linked_list)
                    print(f"\n[+] Status lowongan sukses diubah menjadi: Dilamar oleh {nama_user}")
                else:
                    print("\n[-] Perubahan status dibatalkan.")
            
            break
        current = current.next
        
    if not ketemu:
        print("[-] ID Lowongan tidak ditemukan.")


# ==================================================
# 3. FITUR HAPUS LOWONGAN (KHUSUS ADMIN)
# ==================================================
def hapus_lowongan(linked_list):
    print("\n===== HAPUS DATA LOWONGAN =====")
    id_cari = input("Masukkan ID Lowongan yang ingin dihapus: ")
    
    current = linked_list.head
    previous = None
    ketemu = False
    
    while current is not None:
        if current.data.id_lowongan == id_cari:
            if previous is None:
                # Jika yang dihapus ternyata node pertama (head)
                linked_list.head = current.next
            else:
                # Jika yang dihapus ada di tengah atau di ujung akhir
                previous.next = current.next
            simpan_lowongan(linked_list)   
            print(f"Lowongan dengan ID {id_cari} berhasil dihapus!")
            ketemu = True
            break
        previous = current
        current = current.next
        
    if not ketemu:
        print("[-] ID Lowongan tidak ditemukan.")