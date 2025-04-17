import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# ======= 1. BACA DATA & GABUNGKAN =======
# Ganti nama kolom sesuai dengan file kamu
fitur = ['kolom1', 'kolom2', 'kolom3', 'kolom4']  # fitur yang sama di kedua file

ekg = pd.read_excel('EKGSet.xlsx')[fitur].dropna()
nh3 = pd.read_excel('NH3Set.xlsx')[fitur].dropna()

# Tambahkan kolom label asal data
ekg['source'] = 'EKG'
nh3['source'] = 'NH3'

# Gabungkan jadi satu dataframe
combined = pd.concat([ekg, nh3], ignore_index=True)

# Ambil data fitur dan label sumber
X = combined[fitur].values
source_label = combined['source'].values

# ======= 2. STANDARISASI =======
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ======= 3. CLUSTERING GMM SECARA GABUNGAN =======
gmm = GaussianMixture(n_components=4, covariance_type='full', random_state=42)
gmm.fit(X_scaled)
labels = gmm.predict(X_scaled)

# ======= 4. PCA KE 3D =======
pca = PCA(n_components=3)
X_3d = pca.fit_transform(X_scaled)

# ======= 5. VISUALISASI GABUNGAN (by sumber data) =======
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

colors = {'EKG': 'blue', 'NH3': 'green'}
for src in np.unique(source_label):
    idx = source_label == src
    ax.scatter(X_3d[idx,0], X_3d[idx,1], X_3d[idx,2], 
               label=f"{src}", c=colors[src], s=40, alpha=0.7)

ax.set_title('Visualisasi 3D Gabungan EKG & NH3')
ax.set_xlabel('PC 1')
ax.set_ylabel('PC 2')
ax.set_zlabel('PC 3')
ax.legend()
plt.show()

# ======= 6. OPSIONAL: Visualisasi berdasarkan cluster hasil GMM =======
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(X_3d[:,0], X_3d[:,1], X_3d[:,2], c=labels, cmap='tab10', s=40)
ax.set_title('Clustering Gabungan (GMM)')
ax.set_xlabel('PC 1')
ax.set_ylabel('PC 2')
ax.set_zlabel('PC 3')
plt.colorbar(sc, label='Cluster')
plt.show()