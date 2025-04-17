import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import os

# ========== SETTING ==========
files = ['EKGSet.xlsx', 'NH3Set.xlsx']

def process_clustering(filename):
    print(f"\n=== Memproses file: {filename} ===")
    if not os.path.exists(filename):
        print(f"File {filename} tidak ditemukan.")
        return
    
    # Baca data dari Excel
    data = pd.read_excel(filename)
    X = data.dropna().values

    # Hitung BIC untuk berbagai jumlah cluster
    bic_scores = []
    n_range = range(1, 11)
    for n in n_range:
        gmm = GaussianMixture(n_components=n, covariance_type='full', random_state=42)
        gmm.fit(X)
        bic_scores.append(gmm.bic(X))

    # Tampilkan grafik BIC
    plt.figure(figsize=(6, 4))
    plt.plot(n_range, bic_scores, marker='o')
    plt.title(f'BIC untuk {filename}')
    plt.xlabel('Jumlah Cluster')
    plt.ylabel('BIC')
    plt.grid(True)
    plt.show()

    # Tentukan cluster optimal
    optimal_n = n_range[np.argmin(bic_scores)]
    print(f"Cluster optimal untuk {filename}: {optimal_n}")

    # Fit GMM
    gmm = GaussianMixture(n_components=optimal_n, covariance_type='full', random_state=42)
    gmm.fit(X)
    labels = gmm.predict(X)

    # PCA ke 3D
    pca = PCA(n_components=4)
    X_3d = pca.fit_transform(X)

    # Visualisasi 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2], c=labels, cmap='tab10', s=40)
    ax.set_title(f'Clustering GMM dalam 3D - {filename}')
    ax.set_xlabel('PC 1')
    ax.set_ylabel('PC 2')
    ax.set_zlabel('PC 3')
    plt.colorbar(sc, label='Cluster')
    plt.show()

# ========== PROSES KEDUA FILE ==========
for file in files:
    process_clustering(file)
