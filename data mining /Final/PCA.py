# A. IMPORT KEBUTUHAN LIBRARY
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# B. MEMBACA DATA SET
df_EKG = pd.read_excel('DataSet_Final.xlsx',sheet_name='EKGSet')
df_NH3 = pd.read_excel('DataSet_Final.xlsx',sheet_name='NH3Set')

# C. KARAKTERISASI
# C.1. Membersihkan Data
df_EKG = df_EKG.fillna(df_EKG.mean())
df_NH3 = df_NH3.fillna(df_NH3.mean())
#Menyiapkan array untuk menyimpan hasil
data = {"Nilai a": [], "Nilai b": [],"Nilai Max":[]} 
# C.2. Ciri EKG
X = np.array(df_EKG.index).reshape(-1, 1)
model = LinearRegression()
for col in df_EKG.columns:
    Y = df_EKG[col].values.reshape(-1, 1)
    model.fit(X, Y)
    slope = model.coef_[0][0]
    intercept = model.intercept_[0]
    data["Nilai a"].append(slope)
    data["Nilai b"].append(intercept)
# C.3. Ciri NH3
data["Nilai Max"] = df_NH3.max().values
# C.4. Menyimpan ke Data Frame Baru
data = pd.DataFrame(data)

# D. EKSTRAKSI
# D.1. Standarisasi Data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
df_scaled = pd.DataFrame(data_scaled, columns=data.columns)
# D.2. PCA Tiga Komponen
pca = PCA(n_components=3)
principal_components = pca.fit_transform(data_scaled)
df_pca = pd.DataFrame(principal_components, columns=["PC1", "PC2", "PC3"])
# D.3. Simpan Hasil PCA
print(df_pca)
df_pca.to_excel('PCA.xlsx', index=False)
