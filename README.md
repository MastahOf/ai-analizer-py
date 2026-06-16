# ai-analizer-py
This is the application from python with purpose to analyze binary vulnerabilities base on CWE with 17 class. This application use codebert fine-tuning AI to analyze the code

---

# AI Code Analizer 🚀

Aplikasi GUI (Graphical User Interface) berbasis Python Tkinter yang berfungsi untuk menganalisis dan mendeteksi potensi kerentanan atau celah keamanan (vulnerability) pada potongan kode bahasa C menggunakan model AI lokal berbasis CodeBERT, serta dilengkapi fitur verifikasi Google GenAI API.

## ✨ Fitur Utama
- **Dual-Frame GUI:** Halaman otentikasi API Key GenAI di awal, dan halaman analisis kode C di lembar kedua.
- **Model Inferensi Lokal:** Menggunakan arsitektur `transformers` (Hugging Face) untuk mengklasifikasikan jenis kerentanan kode secara offline.
- **Manajemen Memori Efisien:** Konversi jalur logistik data langsung menggunakan Array murni NumPy 1D untuk kecepatan eksekusi data yang optimal.
- **Sasis Jalur Relatif:** Aplikasi dapat dipindahkan dan dijalankan di direktori mana saja tanpa merusak jalur pustaka file internal.

---

## 🛠️ Persyaratan Sistem (Prerequisites)

Aplikasi ini berjalan menggunakan Python 3.x dan membutuhkan beberapa library eksternal. Daftar lengkap pustaka yang digunakan adalah:
- `torch`
- `transformers`
- `numpy`
- `google-genai`

---

## 📦 Panduan Instalasi & Persiapan Lokal

### 1. Kloning Repositori
Unduh atau simpan seluruh file kode yang ada di dalam repositori ini ke dalam satu folder lokal di komputer Anda. Pastikan strukturnya berisi file-file berikut:
- `code-analizer.py`
- `classes.npy`
- `requirements.txt`

### 2. Instalasi Library Dependency
Buka Terminal atau Command Prompt di direktori folder tersebut, lalu jalankan perintah berikut untuk menginstal seluruh pustaka sekaligus:
```bash
pip install -r requirements.txt
