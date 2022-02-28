# Tucil2_13520145
Program membentuk ConvexHull dari dataset tertentu

Program ini adalah program mencari convex hull dari suatu himpunan yang berasal dari dataset tertentu, dimulai dengan membentuk sub bagian dan mencari masing-masih hull dari tiap bagian,lalu menyatukan semua hull yang ditemukan lalu akan dilakukan visualisasi. Penjelasan lebih lengkap terdapat pada program dan juga laporan. 

Pastikkan IDE dan compiler anda support bahasa python.
Pastikan anda sudah mendownload modul/package yang akan digunakan ,yakni : numpy,pandas,math,matplotlib.pyplot. 

Jika anda belum memiliki salah satu package/modul diatas :
1. pandas
   Requirement : Python version support Officially Python 3.8, 3.9 and 3.10.
2. numpy
   Requirement : Python >=3.8
3. mathplotlib.pyploy version 3.1.2
   Matplotlib requires the following dependencies:
   Python (>= 3.6)
   FreeType (>= 2.3)
   libpng (>= 1.2)
   NumPy (>= 1.11)
   setuptools
   cycler (>= 0.10.0)
   dateutil (>= 2.1)
   kiwisolver (>= 1.0.0)
   pyparsing

Adapun beberapa dataset yang sudah dicoba untuk program ini : 
1. load_iris()
load_iris(*[, return_X_y, as_frame])
3. load_wine()
load_wine(*[, return_X_y, as_frame])
5. load_breast_cancer()
load_breast_cancer(*[, return_X_y, as_frame])

Untuk memulai program ini silahkan ikuti langkah berikut ini
1. Pastikan semua modul dan compiler sudah siap digunakan
2. Ganti {bagian ini} dengan 3 pilihan yang terdapat 
data = datasets.{bagian ini}
4. Lalu pilih kolom yang akan digunakan karena kita akan memanggil langsung fungsi visualisasinya,yakni displayConvexHull(df,a,b,hull)
5. Contoh: (untuk kolom : 0 dan 1 pada dataset iris) 

data = datasets.load_iris()
displayConvexHull(df,0,1,hull)

6. displayConvexHull(df,0,1,hull)
7. Klik tombol run.
8. Selamat ConvexHull sudah terbentuk!

Steven Gianmarg Haposan Siahaan/13520145
K01
