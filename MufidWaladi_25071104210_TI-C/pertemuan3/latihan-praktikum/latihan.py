class Vehicle():
    def __init__(self, jenis, merek, tahun_rilis):
        self.jenis = jenis
        self.merek = merek
        self.tahun_rilis = tahun_rilis

    def sound(self):
        return "suara" 
   
class Honda(Vehicle):
    def __init__(self, jenis, merek, tahun_rilis):
        super().__init__(jenis, merek, tahun_rilis)
        self.__jenis = jenis

    def sound(self):
        return super().sound("tit")
    
    def get_jenis(self):
        return self.__jenis
    
    def set_jenis(self,jenis_lain):
        self.__jenis = jenis_lain
        print("Nilai sudah di ubah")

class Mobil(Vehicle):
    def __init__(self, jenis, merek, tahun_rilis):
        super().__init__(jenis, merek, tahun_rilis)
        self.__merek = merek
    
    def sound(self):
        return super().sound("Tit tit")


y = Honda("Moge", "Yamaha", 2020)
print(y.jenis)
y.set_jenis("Ninja")