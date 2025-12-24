<h1 align="center">Klasifikasi Skintone pada Citra Wajah</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/97ac893a-cc07-4a70-a18f-197639c6188c" width="450">
</p>

---

## Table of Content
1. [Deskripsi Proyek](#deskripsi-proyek)
   - [Latar Belakang](#latar-belakang)
   - [Tujuan Pengembangan](#tujuan-pengembangan)
2. [Dataset](#dataset)
   - [Dataset yang dipakai](#dataset)
4. [Preprocessing dan Pemodelan](#preprocessing-dan-pemodelan)
   - [Preprocessing Data](#preprocessing-data)
   - [Pemodelan](#pemodelan)
5. [Hasil Evaluasi dan Analisis](#hasil-evaluasi-dan-analisis)
   - [Classification Report](#classification-report)
   - [Grafik Loss dan Accuracy](#grafik-loss-dan-accuracy)
   - [Confusion Matrix](#confusion-matrix)
   - [Tabel Perbandingan Model](#tabel-perbandingan-model)
6. [Sistem Website Sederhana](#sistem-website-sederhana)


---

## Deskripsi Proyek
Proyek Klasifikasi Skintone pada Citra Wajah merupakan bagian dari Ujian Akhir Praktikum (UAP) Machine Learning. Tujuan utama project ini adalah membangun sistem klasifikasi citra wajah berbasis Deep Learning, serta mengintegrasikan model yang telah dilatih ke dalam website sederhana menggunakan Streamlit.
Sistem ini menerima input berupa citra wajah, kemudian memprediksi kategori skintone secara otomatis berdasarkan pola visual yang dipelajari oleh model.

### Latar Belakang
Pengolahan citra wajah dengan pendekatan Deep Learning semakin berkembang dan banyak digunakan. Salah satu karakteristik visual penting yang dapat dianalisis dari citra wajah manusia adalah skintone. Dengan pendekatan deep learning, klasifikasi skintone dapat dilakukan secara otomatis dan lebih akurat. Oleh karena itu, diperlukan sistem otomatis yang mampu mengklasifikasikan skintone secara sederhana dan konsisten.

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

### Dataset yang digunakan pada project
Total setelah sampling: **6.000** (1.500 per kelas)
Dataset asli memiliki jumlah data yang besar sehingga membutuhkan waktu komputasi yang cukup lama apabila digunakan secara penuh pada pelatihan model. Oleh karena itu, dataset dikurangi menggunakan random sampling menjadi 1.500 citra per kelas (total 6.000 citra) agar proses pelatihan dapat berjalan lebih efisien pada sistem lokal dan distribusi kelas tetap seimbang.

Dataset hasil seleksi kemudian dibagi menjadi:
  - training set (70%),
  - validation set (15%),
  - test set (15%).
Pembagian ini bertujuan untuk melatih model, memantau performa selama pelatihan, serta melakukan evaluasi akhir secara objektif.

## Preprocessing dan Pemodelan
### Preprocessing Data
- Ukuran gambar: **160x160**
- CNN Base: rescale 1./255 + augmentasi ringan
- Pretrained (MobileNetV2/ResNet50): preprocessing khusus menggunakan preprocess_input

Augmentasi (train):
- rotation_range=15
- zoom_range=0.1
- width/height_shift_range=0.1
- horizontal_flip=True

### Pemodelan
### 1) CNN Base (Non-Pretrained)
Model CNN dibangun dan dilatih dari awal tanpa menggunakan bobot pretrained. Model ini terdiri dari beberapa layer konvolusi dan pooling untuk mengekstraksi fitur dari citra wajah, kemudian diakhiri dengan layer klasifikasi untuk memprediksi 4 kelas skintone. Model CNN base digunakan sebagai pembanding (baseline) terhadap model transfer learning.

### 2) MobileNetV2 (Transfer Learning)
Model ini menggunakan MobileNetV2 pretrained ImageNet sebagai ekstraktor fitur. Lapisan utama model dibekukan agar bobot pretrained tetap, kemudian ditambahkan layer klasifikasi untuk memprediksi 4 kelas skintone. MobileNetV2 dipilih karena ringan dan efisien, sehingga cocok dijalankan pada perangkat lokal.
### 3) ResNet50 (Transfer Learning)
Model ini menggunakan ResNet50 pretrained ImageNet sebagai ekstraktor fitur dengan lapisan utama yang dibekukan. Selanjutnya ditambahkan layer klasifikasi untuk menyesuaikan output menjadi 4 kelas skintone. ResNet50 dipilih karena mampu menangkap fitur visual yang lebih kompleks sehingga umumnya memberikan performa yang baik.

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


