from structures.queue import Queue
from structures.stack import Stack

def apply_job(antrian, undo, nama, pekerjaan):
    data = nama + " melamar " + pekerjaan

    antrian.enqueue(data)
    undo.push(data)

    print("Lamaran berhasil dikirim")


def undo_apply(undo):
    data = undo.pop()

    if data is not None:
        print("Undo :", data)
    else:
        print("Tidak ada data")