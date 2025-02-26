import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Fungsi untuk menghitung jarak Euclidean
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2, axis=1))

# Kelas K-Means Clustering
class KMeans:
    def __init__(self, k=3, max_iters=100, tol=1e-4):
        self.k = k
        self.max_iters = max_iters
        self.tol = tol  # Batas toleransi untuk konvergensi

    def fit(self, X):
        # Inisialisasi centroid secara acak
        np.random.seed(42)
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        
        for _ in range(self.max_iters):
            # Mengelompokkan data ke centroid terdekat
            clusters = [[] for _ in range(self.k)]
            for x in X:
                distances = euclidean_distance(x, self.centroids)
                cluster_idx = np.argmin(distances)
                clusters[cluster_idx].append(x)
            
            # Konversi list ke numpy array
            clusters = [np.array(cluster) for cluster in clusters]
            
            # Menyimpan centroid lama untuk pengecekan konvergensi
            old_centroids = np.copy(self.centroids)
            
            # Mengupdate centroid dengan rata-rata cluster
            for i in range(self.k):
                if len(clusters[i]) > 0:
                    self.centroids[i] = np.mean(clusters[i], axis=0)

            # Cek konvergensi
            if np.linalg.norm(self.centroids - old_centroids) < self.tol:
                break
        
        self.labels_ = np.zeros(X.shape[0])
        for i, x in enumerate(X):
            self.labels_[i] = np.argmin(euclidean_distance(x, self.centroids))

# Generate dataset contoh
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Inisialisasi dan jalankan K-Means
kmeans = KMeans(k=3)
kmeans.fit(X)

# Plot hasil clustering
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', alpha=0.5)
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='red', marker='X', s=200, label='Centroid')
plt.legend()
plt.title("K-Means Clustering")
plt.show()

# user by BProject Developer
