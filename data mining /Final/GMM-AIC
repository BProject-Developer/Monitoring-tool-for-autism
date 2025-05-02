# A. IMPORT LIBRARY
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

# B. AMBIL DATA PCA
from PCA import df_pca
X = df_pca.to_numpy()

# C. PENGELOMPOKAN DATA
def process_clustering(X, title='Hasil Pengelompokan'):
    print("\n=== Memproses Pengelompokan ===")
    # C.1. Hitung AIC 4 Kelompok
    gmm = GaussianMixture(n_components=4, covariance_type='full', random_state=42)
    gmm.fit(X)
    aic_score = gmm.aic(X)
    # C.2. Tampilkan AIC
    print(f"AIC untuk 4 Kelompok: {aic_score}")
    plt.figure(figsize=(6, 4))
    plt.plot([4], [aic_score], marker='o')
    plt.title('AIC untuk GMM (4 Kelompok)')
    plt.xlabel('Jumlah Kelompok')
    plt.ylabel('AIC')
    plt.grid(True)
    plt.show()
    # C.3. Fit dan prediksi cluster
    labels = gmm.predict(X)
    # C.4. Membuat Plot
    pca = PCA(n_components=3)
    X_3d = pca.fit_transform(X)
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2], c=labels, cmap='tab10', s=40)
    centers = gmm.means_
    ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], 
           c='black', s=200, marker='X', label='Pusat Kelompok')
    for i, (x, y, z) in enumerate(centers):
        ax.text(x, y, z, f' {i}', color='black', fontsize=10, weight='bold')
    ax.set_title(f'Pengelompokkan GMM dalam 3D - {title}')
    ax.set_xlabel('PC 1')
    ax.set_ylabel('PC 2')
    ax.set_zlabel('PC 3')
    plt.colorbar(sc, label='Kelompok')
    plt.show()
    # C.5. Simpan hasil plot ke gambar
    plt.savefig("GMM_Gambar.png")
    plt.close()
    print("Plot disimpan sebagai GMM_Gambar.png")
    # C.5. Menyimpan Pusat Kelompok
    print("\nPusat Kelompok (PC1, PC2, PC3):")
    centers_df = pd.DataFrame(centers, columns=["PC1", "PC2", "PC3"])
    centers_df[""] = range(4)
    print(centers_df)
    centers_df.to_excel('GMM_Pusat.xlsx', index=False)
    # C.6. Menyimpan Hasil Kelompok
    df_pca["Kelompok GMM"] = labels
    df_pca.to_excel("GMM_Hasil.xlsx", index=False)
    print("Hasil klasterisasi per data disimpan di 'GMM_Hasil.xlsx'")
# Panggil fungsi
process_clustering(X, title='df_pca')
