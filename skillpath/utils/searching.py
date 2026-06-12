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