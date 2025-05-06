# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya-Jaya Maju

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang telah beroperasi sejak tahun 2000 dengan lebih dari 1.000 karyawan di berbagai lokasi. Meskipun skalanya besar, perusahaan menghadapi tantangan dalam mengelola karyawan, yang tercermin dari tingginya attrition rate (rasio karyawan yang keluar) melebihi 10%. Tingkat pergantian karyawan yang tinggi ini dapat berdampak negatif pada produktivitas dan biaya operasional. Oleh karena itu, departemen HR ingin mengidentifikasi faktor-faktor penyebab masalah ini dan mengembangkan business dashboard untuk memantau serta mengambil tindakan pencegahan yang efektif.

### Permasalahan Bisnis

Berikut ini adalah beberapa permasalahan bisnis yang perlu diselesaikan berdasarkan latar belakang yang telah dijelaskan pada bagian sebelumnya:
    - Identifikasi Faktor Penyebab Tingginya Attrition Rate (Perusahaan belum memahami akar penyebab karyawan resign (misal: lingkungan kerja, kepuasan kerja, atau hal-hal lainnya). Tanpa identifikasi ini, upaya pencegahan tidak akan tepat sasaran.)
    - Ketidakefektifan Strategi Retensi (Kebijakan retensi karyawan yang ada tidak efektif, sehingga perlu evaluasi dan penyesuaian berbasis data untuk mengurangi risiko kehilangan talenta kunci.)
    - Kebutuhan Dashboard Pemantauan Proaktif (Perusahaan memerlukan alat visual (dashboard) yang dapat memantau indikator attrition, memberikan early warning, dan mendukung keputusan berbasis data secara cepat.)
Dengan demikian, permasalahan ini perlu diselesaikan untuk menstabilkan SDM, meningkatkan efisiensi operasional, dan mengurangi biaya jangka panjang terkait pergantian karyawan.

### Cakupan Proyek

**1. Data Understanding & Exploratory Data Analysis**  
- Memahami setiap variable pada kolom dataset
- Mencari adanya noise pada dataset (missing value, data duplikat, dll.)
- Memahami statistik deskriptif pada setiap kolom numerik dalam dataset 
- Mengecek nilai setiap kategori dalam kolom-kolom tertentu untuk melihat adanya kemungkinan kesalahan penulisan
- Melakukan visualisasi dan eksplorasi pada data untuk melihat faktor-faktor yang menyebabkan terjadinya attrition

**2. Data Preparation / Preprocessing**  
- Melakukan penanganan terhadap missing value 
- Melakukan penambahan fitur untuk dimasukkan juga dalam proses pemodelan (Feature Engineering)
- Melakukan seleksi fitur variable berdasarkan hasil EDA sebelumnya
- Menormalisasi dan encoding pada kolom fitur tertentu
- Membagi dataset menjadi 80% train dan 20% test  

**3. Pembuatan & Evaluasi Hasil Model Prediksi**  
- Jenis pemodelan yang digunakan yaitu Klasifikasi dengan 3 model berbeda untuk melihat hasil terbaik (Logistic Regression, Decision Tree, & K-NN).
- Terdapat juga penerapan GridSearch untuk menentukan parameter terbaik dari setiap model  
- Hasil pemodelan akan dievaluasi dengan beberapa metrik (Akurasi, Precision, Recall, F1-Score) 

**4. Pengembangan Dashboard**  
- Membuat dashboard dengan menggunakan Metabase untuk pemantauan real-time.  
- Beberapa visualisasi utama dari dashboard ini yaitu attrition rate berdasarkan kenyamanan kerja karyawan dan latar belakang pendidikan & pekerjaan karyawan.
- Diharapkan akan mendukung pengambilan keputusan HR untuk strategi-strategi tertentu.  

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment:
Berikut ini adalah beberapa tahapan yang diperlukan untuk menyiapkan environment agar nantinya file dapat dijalankan dengan baik:
1. Clone Repository terlebih dahulu
```
git clone https://github.com/hardiantots/penerapan-ds-1
```

2. Install Dependencies yang diperlukan
```
pip install -r requirements.txt
```

```
# Jika ingin mengaktifkan di conda
conda create --name [berikan nama yang sesuai] python=3.11
conda activate [berikan nama yang sesuai]

# Lakukan install dependencies yang diperlukan
pip install -r requirements.txt

# Akses jupyter notebook
jupyter-notebook
```

2. Jika ingin mencoba prediksi dengan data baru, dapat membuka file prediction.py dan mengganti file yang diload pada bagian komentar 'Load Data Test' (saat ini hanya menerima file dalam format .csv)

3. Setelah itu, filenya dapat di-run dan nantinya akan menghasilkan prediksi untuk beberapa sample data yang telah dimasukkan dalam bentuk csv

4. Email dan Password untuk Metabase:
```
email: root@mail.com
password: root123
```

## Business Dashboard

Beberapa hal yang ditampilkan dalam business dashboard yang telah dibuat yaitu:
1. Rangkuman KPI
    - Attrition Rate: 12.18% (Tingkat karyawan yang keluar dari perusahaan lebih dari 10%)
    - Active Employee: 879 orang masih aktif.
    - Average Total Working Years: 11.3 tahun (Rata-rata pengalaman kerja cukup tinggi.)
    - Average Employee Income: $6,503 (Pendapatan bulanan karyawan cukup baik secara rata-rata.)

2. Analisis Berdasarkan Variable
    - OverTime
        - Karyawan yang bekerja lembur memiliki attrition rate dua kali lipat lebih tinggi (31.92%) dibandingkan yang tidak lembur (10.79%).
        - Lembur yang berlebihan meningkatkan risiko attrition hingga tiga kali lipat, menandakan potensi kelelahan dan ketidakpuasan kerja.
    - Marital Status
        - Single: tingkat attrition tertinggi (26.7%)
        - Married & Divorced: jauh lebih rendah (<14%)
        - Karyawan lajang lebih rentan keluar, menunjukkan bahwa komitmen personal berpengaruh terhadap retensi.
    - Work Life Balance
        - Untuk skor WLB pada rentang 2-4, tingkat attrition rate tidak terlalu tinggi.
        - Sedangkan untuk skor 1, cukup tinggi (sekitar 32%), yang menandakan bahwa keseimbangan kerja-hidup yang buruk secara langsung berkorelasi dengan meningkatnya keinginan untuk keluar.
    - Education Field
        - Marketing dan Technical Degree menunjukkan attrition lebih tinggi dibandingkan bidang seperti Medical.
    - Education
        - Terlihat bahwa pada Level 1 dan 3 lebih cenderung untuk keluar. Sedangkan pada Level tertinggi (5) hanya sedikit yang keluar
        - Pendidikan tingkat rendah hingga menengah menunjukkan kecenderungan lebih tinggi untuk attrition dibanding level tertinggi.
    - Department
        - Sales: attrition tertinggi (26.49%)
        - Human Resources & R&D: lebih stabil (attrition <16%)
        - Divisi Sales mengalami turnover tertinggi, menunjukkan kemungkinan tekanan target atau kepuasan kerja rendah.
    - Business Travel
        - Travel Frequently: attrition tinggi (24.03%)
        - Travel Rarely & Non-Travel: lebih rendah (~15%)
        - Frekuensi perjalanan tinggi berasosiasi dengan stress yang berdampak pada tingginya attrition.
    - Job Role
        - Sales Representative dan Laboratory Technician merupakan kedua role dengan attrition rate tertinggi.
        - Manager dan R&D role lebih stabil dengan attrition <10%
    - Job Level
        - Level rendah cenderung memperlihatkan attrition rate yang tinggi
        - Sedangkan untuk Level 4–5 itu sangat rendah (<10%)
        - Jabatan senior cenderung lebih loyal dan Jabatan tingkat bawah cenderung keluar lebih sering, menandakan kebutuhan akan pengembangan karier dan insentif.
    - Years at Company
        - Masa kerja karyawaan <5 tahun memperoleh attrition paling tinggi (25.84%)
        - Semakin lama masa kerja, semakin kecil kemungkinan keluar.
    - Job Satisfaction
        - Semakin tinggi kepuasan kerja → attrition menurun.
        - Skor 1: attrition 22.44%, Skor 4: hanya 11.47%
        - Kepuasan kerja rendah berbanding lurus dengan niat resign, sehingga perlu peningkatan motivasi dan lingkungan kerja.
    - Environment Satisfaction
        - Skor 1: attrition 27.27%
        - Skor 4: attrition 12.74%
        - Lingkungan kerja yang memuaskan menekan niat karyawan keluar.
    - Distance to Work
        - Jarak <5 km: attrition 22.55%
        - Jarak 5–10 km: attrition menurun (14.11%)
        - Jarak >10 km: dikisaran 15%
        - Jarak ekstrem (terlalu dekat atau terlalu jauh) memicu ketidaknyamanan yang bisa memengaruhi retensi.
    - Years in Current Role
        - 10 tahun: attrition hanya 7.89%
        - <10 tahun: jauh lebih tinggi (17.47%)
        - Stabilitas dalam peran selama lebih dari 10 tahun menunjukkan loyalitas yang tinggi.
    - Distribusi Umur dan Gaji Bulanan terhadap Attrition Rate
        - Semakin tua dan semakin tinggi gaji → ukuran bubble kecil → attrition rendah.
        - Banyak bubble besar di usia <35 dengan gaji < $6,000 → rentan keluar.
        - Titik kritis: karyawan muda dengan gaji rendah berisiko tinggi keluar.

## Conclusion

1. Faktor-Faktor yang mempengaruhi Attrition Rate
Faktor risiko tinggi attrition utamanya berasal dari karyawan muda, bergaji rendah, berstatus lajang, serta yang sering lembur. Job level rendah dan kepuasan terhadap pekerjaan maupun lingkungan kerja yang rendah juga memperbesar kemungkinan mereka untuk keluar. Selain itu, jarak ke kantor yang terlalu jauh justru berkorelasi dengan attrition yang lebih tinggi, kemungkinan karena kurangnya komitmen atau kenyamanan jangka panjang. Sebaliknya, faktor-faktor protektif seperti senioritas, tidak lembur, serta tingkat kepuasan dan pendapatan yang tinggi cenderung menurunkan risiko attrition.

2. Hasil Pembuatan Model
Berdasarkan hasil percobaan terhadap 3 model yang berbeda dengan menerapkan GridSearch untuk mengoptimalkan parameter pada setiap jenis model, diperoleh hasil akhir bahwa Logistic Regression ('clf__C': 0.1, 'clf__class_weight': 'balanced', 'clf__penalty': 'l2') memperoleh hasil terbaik dengan Akurasi 77.8%, Precision 43.3%, Recall 69.2%, dan F1-Score 52.5% (Lebih seimbang dibandingkan 2 model lainnya). Hasil evaluasi metrik memperlihatkan bahwa model sebenarnya masih belum memperoleh hasil yang baik dikarenakan faktor imbalanced class pada variable target (83% karyawan tidak keluar dari perusahaan & 17% karyawan keluar dari perusahaan).

3. Dashboard
Dashboard yang telah dibuat mencakup beberapa visualisasi dan informasi untuk menyajikan ringkasan metrik utama seperti attrition rate sebesar 12.18%, jumlah karyawan aktif, rata-rata pengalaman kerja dan pendapatan bulanan. Selain itu, terdapat analisis mendalam terhadap faktor-faktor yang memengaruhi attrition seperti lembur, status pernikahan, keseimbangan kerja-hidup, dan kepuasan kerja. Visualisasi juga menunjukkan bagaimana departemen, peran pekerjaan, dan jenjang jabatan berdampak pada tingkat keluar masuknya karyawan. Faktor lingkungan seperti jarak ke tempat kerja, frekuensi perjalanan dinas, dan durasi bekerja di posisi yang sama turut dievaluasi. Data juga dianalisis berdasarkan karakteristik demografis seperti usia dan penghasilan untuk mengidentifikasi kelompok berisiko tinggi. Keseluruhan dashboard memberikan gambaran komprehensif mengenai pola attrition karyawan dan indikator-indikator utama yang menyertainya.

### Rekomendasi Action Items

1. Kurangi Beban Lembur dan Perbaiki Work‑Life Balance
Terapkan kebijakan lembur terukur (misalnya batas maksimum jam ekstra) dan program fleksibilitas (remote day, jam kerja fleksibel) untuk menurunkan kelelahan dan stres.

2. Fokus Retensi Karyawan Entry‑Level dan yang Baru Bergabung (< 5 tahun)
Buat program onboarding dan mentoring intensif, plus jalur karier yang jelas agar karyawan baru merasa cepat “nyambung” dan termotivasi.

3. Penyesuaian Kompensasi Berdasarkan JobLevel dan Pasar
Lakukan review gaji secara berkala terutama untuk level rendah dan role teknis/marketing yang menunjukkan tren attrition tinggi, agar tetap kompetitif dan adil.

4. Perkuat Kepuasan Kerja & Lingkungan
Jalankan survei rutin untuk mengidentifikasi titik rentan (lingkungan, budaya, kebutuhan fasilitas) dan tanggapi dengan perbaikan (penataan ruang, program wellbeing, social events).

5. Segmentasi Program Retensi Berdasarkan Profil Risiko
Targetkan intervensi khusus untuk karyawan muda, lajang, dan yang sering melakukan business travel (misalnya paket benefit keluarga, dukungan relokasi, atau cuti tambahan) guna mengurangi beban non‑moneter yang memicu keluarnya karyawan tersebut dari perusahaan.
