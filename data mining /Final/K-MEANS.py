# A. IMPORT LIBRARY
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D  # Untuk plot 3D
import pandas as pd
import numpy as np

# B. AMBIL HASIL PCA         
from PCA import df_pca
X = df_pca.to_numpy()

# C. METODE K-MEANS (4 klaster)
kmeans = KMeans(n_clusters=4, random_state=0, n_init=10)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# D. MENAMPILKAN HASIL PENGELOMPOKAN
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = ['r', 'g', 'b', 'c'] # Warna untuk 4 kelompok
# D.1. Plot Data Sesuai Kelompok
for i in range(len(X)):
    ax.scatter(X[i, 0], X[i, 1], X[i, 2], c=colors[labels[i]], marker='o')
# D.2. Plot Pusat Kelompok
ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2],
           c='black', s=200, marker='X', label='Pusat Kelompok')
# D.3. Memberi Nama Pusat Kelompok
for i, (x, y, z) in enumerate(centroids):
    ax.text(x, y, z, f' {i}', color='black', fontsize=10, weight='bold')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
ax.set_title('Pengelompokkan K-Means 3D (4 Klaster)')
ax.legend()
#plt.colorbar(sc, label='Kelompok')
plt.show()
    
# D.4. Simpan hasil plot ke gambar
plt.savefig("KMeans_Gambar.png")
plt.close()
print("Plot disimpan sebagai KMeans_Gambar.png")

# E. MENYIMPAN HASIL DALAM EXCEL
# E.1. Pusat Kelompok
print("\nPusat Kelompok (PC1, PC2, PC3):")
centers_df = pd.DataFrame(centroids, columns=["PC1", "PC2", "PC3"])
centers_df["Kelompok"] = range(4)  # Disesuaikan ke 4 klaster
print(centers_df)
centers_df.to_excel('KMeans_Pusat.xlsx', index=False) #Simpan ke Excel
# E.2. Menyimpan Hasil
df_pca["Kelompok KMeans"] = labels
df_pca.to_excel("KMeans_Hasil.xlsx", index=False)
print("File 'KMeans_Hasil.xlsx' berhasil dibuat.")
