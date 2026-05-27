def bubble_sort_gaji(data):
    panjang = len(data)

    i = 0
    while i < panjang:
        j = 0

        while j < panjang - 1:
            if data[j].gaji < data[j + 1].gaji:
                sementara = data[j]
                data[j] = data[j + 1]
                data[j + 1] = sementara

            j = j + 1

        i = i + 1