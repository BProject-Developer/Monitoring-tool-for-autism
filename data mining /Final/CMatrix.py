from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, adjusted_rand_score
from K-MEANS import df_pca
df_cluster = df_pca.copy()
df_cluster["KMeans_Cluster"] = kmeans_labels
df_cluster["GMM_Cluster"] = gmm_labels
df_cluster.to_excel("Hasil_KMeans_vs_GMM.xlsx", index=False)
print("✔️ Hasil klaster disimpan ke 'Hasil_KMeans_vs_GMM.xlsx'")

# F. CONFUSION MATRIX
cm = confusion_matrix(kmeans_labels, gmm_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[f"Cluster {i}" for i in range(4)])
disp.plot(cmap='Blues')
plt.title("Confusion Matrix: K-Means vs GMM")
plt.show()

# G. ADJUSTED RAND INDEX
ari = adjusted_rand_score(kmeans_labels, gmm_labels)
print(f"\nAdjusted Rand Index (K-Means vs GMM): {ari:.4f}")
