# projek_cased_base
# SKILLPATH
## Portal Pencarian Kerja & Pelatihan

SkillPath adalah program berbasis Python yang dibuat untuk membantu proses pencarian kerja, pengelolaan lowongan, dan sistem rekrutmen sederhana menggunakan konsep Algoritma Pemrograman dan Struktur Data.

Program ini dibuat sebagai proyek akhir praktikum dengan menerapkan berbagai materi seperti:
- OOP
- Sorting
- Searching
- Rekursif
- Linked List
- Stack
- Queue
- Tree
- Graph
- Hash Table
- File Handling

---

# TUJUAN PROGRAM

Program ini bertujuan untuk:
1. Mengelola data lowongan pekerjaan
2. Membantu user mencari pekerjaan
3. Mengelola proses lamaran kerja
4. Memberikan rekomendasi pekerjaan berdasarkan skill
5. Menerapkan struktur data dalam studi kasus nyata

---

# FITUR PROGRAM

## FITUR ADMIN (HRD)

| No |          Fitur          |                     Penjelasan                     | Struktur Data / Algoritma |
|----|-------------------------|----------------------------------------------------|---------------------------|
| 1  | Login Admin             | Admin login menggunakan username dan password      | Hash Table, Dictionary    |
| 2  | Tambah Lowongan         | Admin menambahkan data lowongan pekerjaan          | OOP, Single Linked List   |
| 3  | Edit dan Hapus Lowongan | Admin mengubah atau menghapus data lowongan        | Linked List               |
| 4  | Sorting Lowongan        | Mengurutkan lowongan berdasarkan gaji atau tanggal | Sorting (Bubble Sort)     |
| 5  | Proses Antrean Pelamar  | Pelamar diproses sesuai urutan masuk               | Queue (FIFO)              |
| 6  | Statistik Lowongan      | Menampilkan jumlah peminat lowongan                | List, Dictionary          |

---

## FITUR USER (PELAMAR)

| No |       Fitur       |               Penjelasan                | Struktur Data / Algoritma |
|----|-------------------|-----------------------------------------|---------------------------|
| 1  | Login User        | User login ke sistem                    | Hash Table                |
| 2  | Profil Digital    | User menyimpan nama, skill, dan riwayat | Dictionary, Set, List     |
| 3  | Apply Job         | User melamar pekerjaan                  | Queue                     |
| 4  | Undo Apply        | Membatalkan lamaran terakhir            | Stack (LIFO)              |
| 5  | Rekomendasi Karir | Menampilkan pekerjaan sesuai skill      | Graph                     |
| 6  | Histori Lamaran   | Menampilkan riwayat lamaran user        | Double Linked List        |

---

# FITUR TAMBAHAN

| No |        Fitur        |                  Penjelasan                  |      Struktur Data        |
|----|---------------------|----------------------------------------------|---------------------------|
| 1  | Hot Jobs            | Menampilkan lowongan premium secara berputar | Circular Linked List      |
| 2  | Struktur Departemen | Menampilkan struktur organisasi perusahaan   | Tree                      |
| 3  | Pencarian Lowongan  | Mencari lowongan berdasarkan kata kunci      | Searching (Linear Search) |
| 4  | Penyimpanan Data    | Menyimpan data ke file txt/csv               | File Handling             |
| 5  | Rekursif Departemen | Menampilkan departemen secara bertingkat     | Rekursif                  |

---

# STRUKTUR FOLDER

```text
SkillPath/
│
├── main.py
│
├── models/
│   ├── lowongan.py
│   ├── pelamar.py
│   └── hrd.py
│
├── structures/
│   ├── single_linked_list.py
│   ├── double_linked_list.py
│   ├── circular_linked_list.py
│   ├── stack.py
│   ├── queue.py
│   ├── tree.py
│   ├── graph.py
│   └── hash_table.py
│
├── utils/
│   ├── sorting.py
│   ├── searching.py
│   ├── file_handler.py
│   └── recursive.py
│
├── features/
│   ├── login_feature.py
│   ├── lowongan_feature.py
│   ├── apply_feature.py
│   ├── recommendation_feature.py
│   └── statistics_feature.py
│
└── database/
    ├── lowongan.txt
    └── pelamar.txt