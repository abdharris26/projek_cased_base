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
