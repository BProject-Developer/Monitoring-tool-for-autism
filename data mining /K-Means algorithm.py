import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# Data
X = np.array([
    [799161, -544.65, 2.13],
    [788771, -562.239, 2.73],
    [799084, -538.53, 7.58],
    [572321, -854.718, 0.53],
    [711943, -602.017, 0.47]
])

# K-Means clustering
kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plot hasil klaster dalam 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for i in range(len(X)):
    ax.scatter(X[i, 0], X[i, 1], X[i, 2], c=colors[labels[i]], marker='o')

ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], c='black', marker='X', s=200, label="Centroid")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('K-Means Clustering 3D')
ax.legend()

# Simpan gambar
plt.savefig("output.png")
plt.close()

print("Gambar telah disimpan sebagai output.png")