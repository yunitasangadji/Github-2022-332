# Klasifikasi Skintone pada Citra Wajah
<p align="center">
  <img src="https://github.com/user-attachments/assets/97ac893a-cc07-4a70-a18f-197639c6188c" width="600">
</p>

---

## Table of Content
1. [Deskripsi Proyek](#deskripsi-proyek)
   - [Latar Belakang](#latar-belakang)
   - [Tujuan Pengembangan](#tujuan-pengembangan)
2. [Dataset](#dataset)
3. [Preprocessing dan Pemodelan](#preprocessing-dan-pemodelan)
   - [Preprocessing Data](#preprocessing-data)
   - [Pemodelan](#pemodelan)
4. [Hasil Evaluasi dan Analisis](#hasil-evaluasi-dan-analisis)
   - [Classification Report](#classification-report)
   - [Confusion Matrix](#confusion-matrix)
   - [Tabel Perbandingan Model](#tabel-perbandingan-model)
5. [Sistem Website Sederhana](#sistem-website-sederhana)


---

## Deskripsi Proyek
Proyek ini merupakan bagian dari Ujian Akhir Praktikum Machine Learning yang bertujuan
untuk membangun sistem klasifikasi citra berbasis deep learning dan
mengintegrasikannya ke dalam website sederhana menggunakan Streamlit.

### Latar Belakang
Skintone merupakan salah satu karakteristik visual penting pada citra wajah manusia.
Dengan pendekatan deep learning, klasifikasi skintone dapat dilakukan secara otomatis
dan akurat.

### Tujuan Pengembangan
- Mengimplementasikan Neural Network dasar (CNN)
- Mengimplementasikan dua model pretrained (Transfer Learning)
- Membandingkan performa ketiga model
- Mengintegrasikan model ke website Streamlit

---

## Dataset
Dataset yang digunakan adalah **Skin Tone Dataset** dari Kaggle.

Link dataset:  
[https://www.kaggle.com/datasets/ducnguyen168/dataset-skin-tone](https://www.kaggle.com/datasets/ducnguyen168/dataset-skin-tone?utm_source=chatgpt.com&select=data_skintone)

Kelas skintone:
- dark
- mid-dark
- mid-light
- light

Dataset dibagi menjadi data train, validation, dan test.

---

## Preprocessing dan Pemodelan

### Preprocessing Data
Tahapan preprocessing yang dilakukan:
- Resize gambar menjadi 224x224
- Normalisasi nilai piksel (0–1)
- Data augmentation pada data training (flip, rotation, zoom)

Augmentasi dilakukan secara real-time dan tidak disimpan ke disk.

### Pemodelan
Tiga model yang digunakan:
1. CNN Base (Non-Pretrained)
2. MobileNetV2 (Transfer Learning)
3. ResNet50 (Transfer Learning)

---

## Hasil Evaluasi dan Analisis

### Classification Report
Evaluasi meliputi accuracy, precision, recall, dan F1-score
pada data test untuk setiap model.

### Confusion Matrix
Confusion matrix digunakan untuk menganalisis kesalahan klasifikasi antar kelas skintone.

### Learning Curve
Grafik loss dan accuracy digunakan untuk menganalisis stabilitas training
serta indikasi overfitting atau underfitting.

### Tabel Perbandingan Model

---

## Sistem Website Sederhana
Sistem website dibangun menggunakan Streamlit dan dijalankan secara lokal.

Fitur website:
- Upload gambar wajah
- Pemilihan model
- Menampilkan hasil prediksi skintone

File utama:
```bash
app.py


