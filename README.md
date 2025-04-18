# 🧠 Sistem Pakar Diagnosis Penyakit  
Sistem pakar berbasis Python menggunakan library `experta`, yang mengimplementasikan metode **Forward Chaining** dan **Backward Chaining** untuk mendiagnosis beberapa jenis penyakit, termasuk **penyakit tambahan dari modul**.

## 📌 Deskripsi  
Repository ini berisi implementasi sistem pakar interaktif yang dapat digunakan untuk:
- Mendeteksi gejala penyakit berdasarkan input pengguna.
- Menarik kesimpulan diagnosis melalui metode inferensi (Forward & Backward Chaining).
- Mendeteksi penyakit umum seperti flu, infeksi tenggorokan, serta 4 penyakit tambahan sesuai modul.

## 🧪 Metode yang Digunakan
- **Forward Chaining**: Sistem mulai dari fakta/gejala yang diberikan dan bergerak maju ke kesimpulan.
- **Backward Chaining**: Sistem mulai dari hipotesis dan memverifikasi dengan mencari gejala yang mendukung hipotesis tersebut.

## 📁 Struktur File
| File                         | Deskripsi                                                                 |
|-----------------------------|---------------------------------------------------------------------------|
| `sistem_pakar.py`           | Berisi implementasi sistem pakar menggunakan `experta`.                  |
| `screenshot/`               | Berisi dokumentasi visual (hasil run program, input pengguna, dll).      |
| `README.md`                 | Dokumentasi dari proyek ini.                                             |


## 💡 Penyakit yang Ditangani
Penyakit yang ditambahkan berdasarkan modul dan bisa dideteksi oleh sistem:
--COVID-19
--Alergi
--TBC (Tubrkulosis)
--DBD (Demam Berdarah Dengue)

## 🛠️ Instalasi & Penggunaan

### 1. Install Library yang Dibutuhkan
```bash
pip install experta
```

### 2. Jalankan Program
```bash
python sistem_pakar.py
```

### 3. Contoh Pertanyaan
Kamu akan diberi serangkaian pertanyaan seperti:
- Apakah kamu demam? (yes/no)
- Apakah kamu kehilangan penciuman? (yes/no)
- … dan lain-lain

Hasil diagnosis akan ditampilkan di akhir berdasarkan aturan yang cocok.

## 📖 Catatan Tambahan
- Sistem ini bersifat **deterministik** dan hanya bekerja sesuai fakta/gejala yang dimasukkan.
- Cocok sebagai **simulasi diagnosis awal**, bukan pengganti pemeriksaan medis profesional.

