# 📖 API Alkitab Terjemahan Baru (Flask)

Proyek ini menyediakan API Alkitab Terjemahan Baru (PL & PB) dalam format JSON yang dapat diakses melalui HTTP endpoint. Dibangun dengan Python Flask, siap untuk dijalankan secara lokal atau di-deploy.

---

## 🚀 Fitur

- Data lengkap Perjanjian Lama (PL) & Perjanjian Baru (PB)
- Akses per pasal, ayat tunggal, atau rentang ayat
- Format JSON mudah digunakan
- Respon cepat (data dimuat di memori saat startup)

---

## 📂 Struktur Data

Folder `lib/` berisi file JSON untuk setiap kitab:

```text
lib/
├── pl/  # Perjanjian Lama
│   ├── kejadian.json
│   ├── keluaran.json
│   └── ...
└── pb/  # Perjanjian Baru
     ├── matius.json
     ├── markus.json
     └── ...
```

---

## 💻 Menjalankan di Lokal

1. **Clone repository**

   ```bash
   git clone https://github.com/username/bible-api.git
   cd bible-api
   ```

2. **Buat virtual environment & install dependencies**

   ```bash
   python -m venv venv
   # Aktifkan environment:
   # Linux/MacOS:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Jalankan API**

   ```bash
   flask run
   ```

API akan berjalan di [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📡 Contoh Endpoint

- **Ambil pasal**
  ```http
  GET /api/pl/kejadian/1
  ```
- **Ambil satu ayat**
  ```http
  GET /api/pb/matius/5/9
  ```
- **Ambil rentang ayat**
  ```http
  GET /api/pl/kejadian/1/3-5
  ```

---

## ⚠️ Catatan Lisensi

Teks Alkitab Terjemahan Baru adalah milik **Lembaga Alkitab Indonesia (LAI)**. Penggunaan data ini hanya untuk tujuan non-komersial atau sesuai ketentuan lisensi LAI.
