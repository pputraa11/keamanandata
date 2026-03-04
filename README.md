# Implementasi Algoritma RC4 - Tugas Kriptografi 🔐

Repositori ini berisi implementasi **Algoritma RC4 (Rivest Cipher 4)** yang dibangun dari awal (*from scratch*) menggunakan bahasa pemrograman Python. Proyek ini dibuat untuk memenuhi tugas mata kuliah Kriptografi/Keamanan Informasi.

## 📝 Deskripsi Algoritma
RC4 adalah *Stream Cipher* simetris yang dirancang oleh Ronald Rivest. Algoritma ini bekerja dengan cara menghasilkan aliran bit acak (*keystream*) yang kemudian digabungkan dengan *plaintext* menggunakan operasi logika **XOR**.

### Fitur Program:
- **KSA (Key-Scheduling Algorithm):** Menginisialisasi dan mengacak array S-Box (256 byte) berdasarkan kunci.
- **PRGA (Pseudo-Random Generation Algorithm):** Menghasilkan aliran kunci (*keystream*) secara dinamis.
- **Interaktif:** Pengguna dapat memasukkan *Plaintext* dan *Key* melalui terminal secara langsung.

---

## 🚀 Cara Menjalankan

### Prasyarat
Pastikan Anda sudah menginstal **Python 3.x** di perangkat Anda.

### Langkah-langkah:
1. **Clone atau Download** repositori ini.
2. Buka terminal atau Command Prompt (CMD).
3. Arahkan ke direktori tempat file disimpan.
4. Jalankan perintah berikut:
   ```bash
   python keamanan.py
