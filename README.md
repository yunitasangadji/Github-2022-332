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
Proyek Klasifikasi Skintone pada Citra Wajah merupakan bagian dari Ujian Akhir Praktikum (UAP) Machine Learning. Tujuan utama project ini adalah membangun sistem klasifikasi citra wajah berbasis Deep Learning, serta mengintegrasikan model yang telah dilatih ke dalam website sederhana menggunakan Streamlit.
Sistem ini menerima input berupa citra wajah, kemudian memprediksi kategori skintone secara otomatis berdasarkan pola visual yang dipelajari oleh model.

### Latar Belakang
Skintone merupakan salah satu karakteristik visual penting pada citra wajah manusia.
Dengan pendekatan deep learning, klasifikasi skintone dapat dilakukan secara otomatis
dan akurat.

### Tujuan Pengembangan
- Mengimplementasikan Neural Network dasar (CNN) sebagai pembanding awal
- Mengimplementasikan **dua model pretrained (Transfer Learning)**, yaitu **MobileNetV2** dan **ResNet50**
- Melakukan analisis dan perbandingan performa ketiga model
- Mengintegrasikan hasil model ke dalam sistem website sederhana menggunakan Streamlit


---

## Dataset
Dataset yang digunakan adalah Skin Tone Dataset yang diperoleh dari Kaggle:

🔗 Link dataset:
https://www.kaggle.com/datasets/ducnguyen168/dataset-skin-tone

Dataset terdiri dari empat kelas skintone, yaitu:
| Kelas | Jumlah Gambar |
|---------------|---------------|
| dark          | 8.640         |
| mid-dark      | 10.600        |
| mid-light     | 6.844         |
| light         | 9.769         |
| **Total**     | **35.853**    |

Dataset kemudian dibagi menjadi:
- Training set
- Validation set
- Testing set
Pembagian ini bertujuan untuk memastikan proses pelatihan, validasi, dan evaluasi dilakukan secara terpisah sehingga hasil model lebih objektif.

---

## Preprocessing dan Pemodelan

### Preprocessing Data
Tahapan preprocessing yang dilakukan:
- memastikan dataset untuk setiap kelas skintone tersedia dan berisi file citra yang valid
- Pembagian dataset menjadi:
  70% data training
  15% data validation
  15% data testing 
- Resize gambar menjadi 224x224
- Normalisasi nilai piksel (0–1)
- Data augmentation pada data training (flip, rotation, zoom, horizontal & vertikal)
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


