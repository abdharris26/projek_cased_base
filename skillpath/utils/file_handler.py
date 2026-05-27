def simpan_lowongan(data):
    file = open("database/lowongan.txt", "w")

    i = 0

    while i < len(data):
        teks = data[i].posisi + "," + data[i].perusahaan + "\n"
        file.write(teks)

        i = i + 1

    file.close()