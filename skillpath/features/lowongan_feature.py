from models.lowongan import Lowongan

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
                print("\n[+] Detail Lowongan berhasil diperbarui oleh Admin!")
            
            # KONDISI USER: Dikunci aksinya, TIDAK BISA edit teks dari admin, cuma bisa daftar/apply
            elif role == "user":
                print("[ Hak Akses: USER/PELAMAR ]")
                print("-> Anda TIDAK BISA mengubah Posisi, Perusahaan, Gaji, atau Tanggal.")
                print("-> Anda hanya diperbolehkan memperbarui status lamaran Anda di sini.")
                
                pilihan = input("\nApakah Anda ingin mengubah status lowongan ini menjadi 'Melamar'? (y/n): ")
                if pilihan.lower() == 'y':
                    current.data.status = f"Dilamar oleh {nama_user}"
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
                
            print(f"Lowongan dengan ID {id_cari} berhasil dihapus!")
            ketemu = True
            break
        previous = current
        current = current.next
        
    if not ketemu:
        print("[-] ID Lowongan tidak ditemukan.")


# ==================================================
# 4. FITUR SORTING LOWONGAN (BUBBLE SORT - KHUSUS ADMIN)
# ==================================================
def sorting_lowongan(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        print("Data lowongan terlalu sedikit untuk diurutkan.")
        return

    print("\nUrutkan Berdasarkan:")
    print("1. Gaji (Tertinggi ke Terendah)")
    print("2. Tanggal (Terbaru ke Terlama)")
    pilihan = input("Pilih metode urut (1/2): ")

    diurutkan = True
    while diurutkan:
        diurutkan = False
        current = linked_list.head
        
        while current.next is not None:
            kondisi = False
            if pilihan == "1":
                # Sort berdasarkan Gaji (Descending)
                if current.data.gaji < current.next.data.gaji:
                    kondisi = True
            elif pilihan == "2":
                # Sort berdasarkan Tanggal (String Descending)
                if current.data.tanggal < current.next.data.tanggal:
                    kondisi = True
            
            if kondisi:
                # Tukar data antar objek di dalam node
                sementara = current.data
                current.data = current.next.data
                current.next.data = sementara
                diurutkan = True
                
            current = current.next
            
    print("[+] Daftar lowongan berhasil diurutkan! Silakan cek perubahannya di Menu 3.")


# ==================================================
# 5. FITUR PENCARIAN LOWONGAN (LINEAR SEARCH - UMUM)
# ==================================================
def cari_lowongan_by_keyword(linked_list):
    print("\n===== PENCARIAN LOWONGAN =====")
    keyword = input("Masukkan kata kunci posisi atau perusahaan: ").lower()
    
    current = linked_list.head
    ketemu = False
    
    print("\n===== HASIL PENCARIAN =====")
    while current is not None:
        # Linear search: Mencari string kecocokan keyword di data posisi/perusahaan
        if keyword in current.data.posisi.lower() or keyword in current.data.perusahaan.lower():
            current.data.tampilkan()
            print("-------------------")
            ketemu = True
        current = current.next
        
    if not ketemu:
        print("[-] Tidak ada lowongan yang cocok dengan kata kunci tersebut.")