# Monitoring Tool for Autism
### Clustering ASD Severity Levels Using EKG and NH3 Data

## Overview

This project presents a data-driven approach to classify Autism Spectrum Disorder (ASD) severity levels using physiological indicators:

- Electrocardiogram (EKG) signals  
- Ammonia (NH3) concentration levels  

The study compares two clustering algorithms:

- K-Means Clustering  
- Gaussian Mixture Model (GMM) with Akaike Information Criterion (AIC)

The goal is to determine which method provides better clustering performance in separating ASD severity levels.

---

## Research Objectives

- Compare the performance of K-Means and GMM-AIC in clustering ASD severity.
- Analyze differences in cluster characteristics.
- Evaluate clustering quality using Silhouette Score.

---

## Dataset

The dataset is based on research conducted by:

Marchelliant et al. (2021) – *Analysis of Electrocardiogram Signal and Ammonia Concentration for Clustering ASD Condition.*

Dataset composition:
- 20 Normal samples
- 54 ASD samples

Extracted features:
- EKG line equation coefficient
- EKG constant
- Maximum NH3 concentration

---

## Methodology

The research pipeline consists of four stages:

### 1. Data Characterization
- Missing value handling (mean imputation)
- Duplicate removal
- Feature selection

### 2. Feature Extraction
- Feature standardization
- Principal Component Analysis (PCA)
- Extraction of PC1, PC2, and PC3

### 3. Clustering
- K-Means (k = 4)
- GMM with AIC (optimal k = 4)

Clusters represent:
- Normal
- Mild ASD
- Moderate ASD
- Severe ASD

### 4. Evaluation
- Silhouette Score comparison
- Visual cluster analysis

---

## Results

| Method  | Silhouette Score | Interpretation        |
|---------|------------------|-----------------------|
| K-Means | 0.72             | Clear separation      |
| GMM-AIC | 0.42             | Overlapping clusters  |

K-Means demonstrated better structural separation and higher clustering quality for this dataset.

---

## Technologies Used

- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- Matplotlib  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/BProject-Developer/Monitoring-tool-for-autism.git
cd Monitoring-tool-for-autism

Install dependencies

```bash
pip install numpy pandas scikit-learn matplotlib

---

## Conclusion
K-Means clustering outperformed GMM-AIC in grouping ASD severity levels based on EKG and NH3 data, achieving a higher Silhouette Score and clearer cluster separation.

---

## Authors
Rachel Dorothy Tomasoa
Alief Bintang Ramadhan

---

## Contributing  
We welcome contributions from developers and collaborators.  
Feel free to open an issue or submit a pull request if you’re interested in improving this project.  
You can also contact us via Instagram: [@decatech.id](https://instagram.com/decatech.id)

## About DecaTech  
**DecaTech** is a team that came together unexpectedly through a competition.  
The team was founded by **Mr. Faisal** and **Ms. Bella**, with **Rachel** and **Bintang** as core members.