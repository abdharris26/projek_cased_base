def cari_lowongan(data, posisi):
    i = 0

    while i < len(data):
        if data[i].posisi == posisi:
            return data[i]

        i = i + 1

    return None