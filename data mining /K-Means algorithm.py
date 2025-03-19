#A. MEMBACA DATA INPUT
import pandas as pd
es=pd.read_excel("EKGSet.xlsx")
ns=pd.read_excel("NH3Set.xlsx")
print(es.head(5))
print(ns.head(5))

#B. KARAKTERISASI EKG
#Inisialisasi
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
#Membuat Variabel X dan Variabel Y
X = np.array(es.index).reshape(-1, 1)
model = LinearRegression()
es = es.fillna(es.mean())
print(es[1])
data = {"nilai a": [], "nilai b": []}

for col in es.columns:
    Y = es[col].values.reshape(-1, 1)  # Data dari kolom Y
    model.fit(X, Y)  # Training model regresi
    slope = model.coef_[0][0]  # Kemiringan garis regresi
    intercept = model.intercept_[0]  # Intersep
    data["nilai a"].append(slope)
    data["nilai b"].append(intercept)
    df = pd.DataFrame(data)

print(df)
#print(f"Regresi untuk kolom {col}: Y = {slope:.2f}X + {intercept:.2f}")


df["nilai nh3"]= np.max(ns, axis=1)
print(df)

import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df)

# Konversi kembali ke DataFrame
df_scaled = pd.DataFrame(data_scaled, columns=df.columns)
print(df_scaled)

pca = PCA(n_components=3)
principal_components = pca.fit_transform(data_scaled)

# Simpan hasil PCA dalam DataFrame
df_pca = pd.DataFrame(principal_components, columns=["PC1", "PC2", "PC3"])
print(df_pca)


from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# Data
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