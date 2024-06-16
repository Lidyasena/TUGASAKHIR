class Manusia:
    def __init__(self, nama, umur, pekerjaan):
        self.nama = nama
        self.umur = umur
        self.pekerjaan = pekerjaan
        
    def tampilkan(self):
        print("Rincian:", self.nama, self.umur, self.pekerjaan)
    
    def tampilkan_umur(self):
        print("manusia:", self.nama, "adalah", self.umur, "thn")
        
    def tampilkan_pekerjaan(self):
        print("manusia:", self.nama, "adalah", self.pekerjaan)
        
    def peranan(self):
        print(self.nama, "tugas utama saya adalah menjaga keamanan negara.")
        
class Tentara(Manusia):
    def peranan(self):
        print(self.nama, "tugas utama saya adalah menjaga keamanan negara.")

class Dokter(Manusia):
    def peranan(self):
        print(self.nama, "tugas utama saya adalah menyelamatkan nyawa dan menjaga kesehatan masyarakat.")

class Petani(Manusia):
    def peranan(self):
        print(self.nama, "tugas utama saya adalah menanam dan menghasilkan makanan bagi masyarakat.")
        
        
# memanggil fungsi dari parent class Manusia
tentara = Tentara("Budi", 30, "Tentara")
tentara.peranan()
dokter = Dokter("Ani", 28, "Dokter")
dokter.peranan()
petani = Petani("Joko", 45, "Petani")
petani.peranan()
