class Lowongan:
    def __init__(self, id_lowongan, judul, perusahaan, gaji, tanggal, status="Aktif"):
        self.id_lowongan = id_lowongan
        self.judul = judul
        self.perusahaan = perusahaan
        self.gaji = float(gaji)
        self.tanggal = tanggal
        self.status = status