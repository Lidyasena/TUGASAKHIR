class Bunga :
    def __init__(self, nama) :
        self.nama = nama
        
    def warna(self) :
        pass
class Mawar(Bunga) :
    def warna(self) :
        return('Merah')
    
class Melati(Bunga) :
    def warna(self):
        return('Putih')
    
class Matahari(Bunga) :
    def warna(self) :
        return('Kuning')

mawar = Mawar ("Mawar")
melati = Melati("melati")
matahari = Matahari("matahari")

print(f' {mawar.nama} berwarna {mawar.warna()}')
print(f' {melati.nama} berwarna {melati.warna()}')
print(f' {matahari.nama} berwarna{matahari.warna()}')