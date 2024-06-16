from abc import ABC, abstractmethod

class Perpustakaan(ABC):
    @abstractmethod
    def Harga(self):
        pass

class Buku(Perpustakaan):
    def __init__(self, penulis, genre):
        self.penulis = penulis
        self.genre = genre

    def databuku(self):
        print("Buku ini ber genre:", self.genre, "dan nama penulisnya:", self.penulis)

    def Harga(self):
        return 50000

class Majalah(Perpustakaan):
    def __init__(self, penerbit, tgl_terbit):
        self.penerbit = penerbit
        self.tgl_terbit = tgl_terbit

    def datamajalah(self):
        print("Majalah ini diterbitkan oleh:", self.penerbit, "dan diterbitkan pada:", self.tgl_terbit)

    def Harga(self):
        return 25000

# Membuat objek Buku dan memanggil metode
buku = Buku("Lidya Sena", "Fiksi Ilmiah")
buku.databuku()
print("Harga Buku:", buku.Harga())

# Membuat objek Majalah dan memanggil metode
majalah = Majalah("Penerbit Sena", "2024-05-15")
majalah.datamajalah()
print("Harga Majalah:", majalah.Harga())
