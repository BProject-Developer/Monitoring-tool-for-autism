import numpy 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

#Membaca data (ganti "data.csv" dengan nama file Anda)
data = pd.read_excel("DataSet_Final.xlsx")  # Pastikan file data.csv ada di direktori yang sama
features = data.iloc[:, :-1]  # Pilih semua kolom kecuali kolom target (sesuaikan jika perlu)

# Standarisasi data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# PCA untuk mengurangi dimensi menjadi 3
pca = PCA(n_components=3)
df_pca = pd.DataFrame(pca.fit_transform(scaled_features), columns=['PC1', 'PC2', 'PC3'])


X = df_pca.to_numpy()

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
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
