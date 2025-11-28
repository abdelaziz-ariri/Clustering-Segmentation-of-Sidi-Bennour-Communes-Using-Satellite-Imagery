# 🌍 Clustering & Segmentation of Sidi Bennour Communes Using Satellite Imagery

## 📌 Project Overview
This project focuses on **clustering and segmenting the communes of the Sidi Bennour province (Morocco)** using satellite imagery and machine learning techniques.  
It aims to extract land-use patterns to support **agricultural planning**, **urban development**, and **environmental monitoring**.

---

## 🛰️ Data Sources
- Satellite images collected from Google Maps.
- Preprocessing steps:
  - RGB extraction  
  - Normalization  
  - Patch generation  
  - Geospatial alignment (if applicable)

---

## 🧠 Methods & Models

### **1. Feature Extraction**
- Convolutional Neural Networks (CNN)
-Using MobileNetV2 as a lightweight and efficient CNN to extract high-level features from satellite imagery.

### **2. Clustering Approaches**
- **K-Means**
- Applying K-Means to group communes based on visual similarity and extracted features.
---

## 📊 Results
- Segmented maps of Sidi Bennour communes  
- Cluster visualizations  
- Feature-space diagrams  
- Evaluation metrics:  
  - Silhouette score  
  - Segmentation accuracy  
---

## 🛠 Technologies Used
- Python  
- NumPy / Pandas  
- Scikit-Learn  
- TensorFlow / PyTorch  
- OpenCV  
- GeoPandas  
- Rasterio  
- Streamlit  

---

## 📁 Project Structure
<img width="702" height="130" alt="image" src="https://github.com/user-attachments/assets/13b7e12e-a811-499d-aa69-8c163f79a982" />

---
## Pipeline
<img width="419" height="256" alt="pipeline" src="https://github.com/user-attachments/assets/0bd1697b-ebbd-469c-8732-4797d1babe67" />

## 🛰️ Data Description

### **Satellite Images**
The folder `images_redimensionnees/` contains resized satellite images of the communes.  
These images are used for:
- Feature extraction  
- Clustering (KMeans or others)  
- Visualization

### **Population Data**
The file `communes_population` contains population values for each commune.  
This allows:
- Statistical analysis  
- Linking demographic and spatial data  

---

## 🧠 Methods Used

### **1. Image Processing**
- Resizing  
- Normalization  
- Conversion to arrays  
- Feature extraction (MobileNetV2)
- Using MobileNetV2 as a lightweight and efficient CNN to extract high-level features from satellite imagery.

### **2. Clustering Techniques**
- K-Means  
- Applying K-Means to group communes based on visual similarity and extracted features.
- Similarity analysis between communes  

### **3. Visualization**
- Interactive dashboard using **Streamlit** (`app.py`)  
- Cluster maps  
- Commune statistics  

---
## 📊 Results

### ✔️ ** Commune Clustering Using Satellite Images**
<img width="748" height="366" alt="result1" src="https://github.com/user-attachments/assets/4e7b00a3-f6d4-4404-8522-c58092462117" />
<img width="731" height="404" alt="result2" src="https://github.com/user-attachments/assets/db799a0e-2831-4a71-a626-693c6d4be314" />



## ▶️ Running the Streamlit App

To launch the interactive dashboard:

```bash
streamlit run app.py


