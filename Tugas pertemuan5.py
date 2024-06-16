from abc import ABC, abstractmethod

class Mobil(ABC):
    @abstractmethod
    def fasilitas(self):
        pass
    
    @abstractmethod
    def kecepatan(self):
        pass
    
    @abstractmethod
    def harga(self):
        pass
    
    @abstractmethod
    def kekuatan(self):
        pass

class BMW(Mobil):
    def fasilitas(self):
        return "BMW dilengkapi dengan fitur canggih seperti AC otomatis."
    
    def kecepatan(self):
        return "kecepatan maximum BMW : 250 km/jam"
    
    def harga(self):
        return "BMW memiliki harga yang cukup tinggi, berkisar antara 500 juta hingga milyaran rupiah."
    
    def kekuatan(self):
        return "BMW dikenal dengan kekuatan mesinnya yang handal dan performa berkualitas."

class Avanza(Mobil):
    def fasilitas(self):
        return "Toyota Avanza cocok untuk keluarga dengan fitur ruang kabin yang luas dan nyaman."
    
    def kecepatan(self):
        return "Avanza memiliki kecepatan maksimum standar, sekitar 160 km/jam."
    
    def harga(self):
        return "Avanza memiliki harga yang terjangkau, berkisar antara 200 juta hingga 300 juta rupiah."
    
    def kekuatan(self):
        return "Avanza dikenal dengan keandalannya dalam perjalanan jarak jauh dan konsumsi bahan bakar yang efisien."

class Ferrari(Mobil):
    def fasilitas(self):
        return "Ferrari merupakan simbol kemewahan dengan fitur-fitur terbaru dan desain yang elegan."
    
    def kecepatan(self):
        return "Ferrari adalah mobil super dengan kecepatan maksimum yang mencapai 350 km/jam."
    
    def harga(self):
        return "Harga Ferrari sangat tinggi, dimulai dari miliaran hingga puluhan miliar rupiah."
    
    def kekuatan(self):
        return "Ferrari dikenal dengan mesin yang sangat bertenaga dan kekuatan akselerasinya yang luar biasa."


# bmw = BMW()
# print("BMW:")
# print(bmw.fasilitas())
# print(bmw.kecepatan())
# print(bmw.harga())
# print(bmw.kekuatan())
# print()

# avanza = Avanza()
# print("Avanza:")
# print(avanza.fasilitas())
# print(avanza.kecepatan())
# print(avanza.harga())
# print(avanza.kekuatan())
# print()

# ferrari = Ferrari()
# print("Ferrari:")
# print(ferrari.fasilitas())
# print(ferrari.kecepatan())
# print(ferrari.harga())
# print(ferrari.kekuatan())

def interface (mobil: Mobil):
    print(f"Fasilitas: {mobil.fasilitas()}")
    print(f"Kecepatan: {mobil.kecepatan()}")
    print(f"Harga: {mobil.harga()}")
    print(f"Kekuatan: {mobil.kekuatan()}")
    
bmw = BMW()

avanza = Avanza()
ferrari= Ferrari()
interface(bmw)
interface(avanza)
interface(ferrari)


