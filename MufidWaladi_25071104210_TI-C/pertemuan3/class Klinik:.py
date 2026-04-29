class Klinik:
    def __init__(self, nama_klinik):
        self.nama_klinik = nama_klinik
        self.daftar_pasien = []

    def tambah_pasien(self, nama, penyakit):
        pasien = {"nama": nama, "penyakit": penyakit}
        self.daftar_pasien.append(pasien)

    def hitung_statistik_penyakit(self):
        # Dictionary untuk menyimpan jumlah: { 'Flu': 2, 'Maag': 2, ... }
        statistik = {}
        for pasien in self.daftar_pasien:
            p = pasien['penyakit']
            statistik[p] = statistik.get(p, 0) + 1
        return statistik

    def tampilkan_laporan(self):
        print("=" * 45)
        print(f"{self.nama_klinik.upper():^45}")
        print("=" * 45)

        # 1. Menghitung dan Menampilkan Statistik Penyakit
        print("\nJUMLAH PENDERITA PER PENYAKIT:")
        statistik = self.hitung_statistik_penyakit()
        
        # Mencari penyakit terbanyak untuk output seperti di gambar
        max_jumlah = max(statistik.values()) if statistik else 0
        penyakit_terbanyak = [k for k, v in statistik.items() if v == max_jumlah]

        for penyakit, jumlah in statistik.items():
            print(f"- {penyakit:<10} : {jumlah} pasien")
        
        print("-" * 25)
        # Menampilkan kesimpulan seperti di foto asli
        info_terbanyak = ", ".join(penyakit_terbanyak)
        print(f"Penyakit terbanyak: {info_terbanyak} ({max_jumlah} pasien)")

        # 2. Data Pasien Lengkap
        print("\nRINCIAN DATA PASIEN:")
        for i, pasien in enumerate(self.daftar_pasien, 1):
            print(f"{i}. {pasien['nama']:<10} | Keluhan: {pasien['penyakit']}")
        
        print("-" * 25)
        print(f"Total pasien terdaftar: {len(self.daftar_pasien)}")
        
        print("\n" + "-" * 45)
        print("Menuju generasi (c)emas")
        print("=" * 45)

# --- EKSEKUSI PROGRAM ---

# Buat objek
klinik_ku = Klinik("Klinik Sehat Ceria Margonda")

# Tambah data sesuai screenshot
klinik_ku.tambah_pasien("Andi", "Maag")
klinik_ku.tambah_pasien("Budi", "Flu")
klinik_ku.tambah_pasien("Citra", "Demam")
klinik_ku.tambah_pasien("Doni", "Flu")
klinik_ku.tambah_pasien("Eka", "Maag")

# Tampilkan Hasil
klinik_ku.tampilkan_laporan()