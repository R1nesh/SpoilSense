# SpoilSense: AI-Powered Produce Spoilage Detection Using YOLOv8

SpoilSense is a lightweight, real-time computer vision system model to detect spoilage in fresh produce using a custom-trained YOLOv8 object detection model. The project uses a dataset of 11,000+ annotated images across various fruit categories to distinguish between fresh and spoiled items — enabling smart monitoring in agricultural, retail, and food supply chain environments.

---

## Purpose

The primary objectives of SpoilSense are:

1. To develop a deep learning model capable of **real-time detection** of produce spoilage.
2. To enable accurate classification between **fresh** and **rotten** classes for various fruits.
3. To create a **lightweight**, deployable solution optimized for speed and size (under 6 MB).
4. To build a robust, diverse dataset with **custom annotations** for effective training and generalization.

---

## Model Overview

- **Model Type**: YOLOv8n Object Detection (Ultralytics)
- **Architecture**: YOLOv8n (Convolutional Neural Network)
- **Dataset Size**: ~11,000 images (manually & algorithmically annotated)
- **Classes**:
  - `Fresh_Apple`, `Rotten_Apple`
  - `Fresh_Banana`, `Rotten_Banana`
  - `Fresh_Tomato`, `Rotten_Tomato`
  - `Fresh_Orange`, `Rotten_Orange`
- **Annotation Format**: YOLO format, with custom class definitions and spatial variance
- **Performance**: Achieved **90%+ mAP** on validation set

---

## Libraries & Tools

The following Python packages are required:

- `Pillow`  
- `tk` 
- `ultralytics`
- `tkinterdnd2` 

Install all dependencies in Terminal with:

```bash
pip install Pillow tk ultralytics tkinterdnd2
```

---

## Results & Model Performance

- **Model Size**: 6 MB  
- **mAP@0.5**: 90%+  
- **Real-Time Inference**: ~30 FPS on standard CPU  
- **Dataset Variance**: Includes lighting, occlusion, rotation, and spoilage stages  

---

## Sample Outputs

Example detections using SpoilSense:

| Input Image | Detection Output |
|-------------|------------------|
| ![pexels-any-lane-5945883](https://github.com/user-attachments/assets/7eda636b-9b3c-45b4-96d1-a00b328c9254) | ![Adobe Express - file](https://github.com/user-attachments/assets/2db24ba3-82c4-4f28-94cc-5b021fd9a0fc) |
|![Malus_Ellison's_Orange (1)](https://github.com/user-attachments/assets/787e5714-5c09-481f-9ca3-287e65feff4a) | <img width="635" height="422" alt="Screenshot 2025-08-19 143607" src="https://github.com/user-attachments/assets/d3f9b960-9220-4b60-bcdc-0fb317ad85f5" /> |
|![Tomatoes-Farm-scaled-1](https://github.com/user-attachments/assets/479fe52e-05c8-4ca2-814d-8c37ed970040)|<img width="636" height="424" alt="Screenshot 2025-08-19 143743" src="https://github.com/user-attachments/assets/3b37ecb2-b35d-44a7-b286-ba26a0a15bde" />|



---

## How to Use

### 1. **Clone the repository**
```bash
git clone https://github.com/R1nesh/SpoilSense
cd SpoilSense
```

### 2. **Run the Inference GUI (Drag-and-Drop Demo)**
```bash
python Scripts/modelTest.py
```

---

## Dataset

The dataset includes 8 classes:
- Fresh and Rotten variants of: **Apple**, **Banana**, **Tomato**, **Orange**

All images were annotated manually using [Roboflow](https://roboflow.com) and exported in YOLO format, with custom class mappings and varying conditions to simulate real-world environments (e.g., lighting, angle, partial rot, size).

---

## Potential Future Improvements

- Retrain the model with a larger set of photoes for more accuracy (more unannotated photoes in validation)
- Potentially lower the confidence threshold for less background misses
- Add more fruit/vegetable categories  
- Integrate temperature/humidity sensors for multi-modal spoilage detection  
- Build a mobile app version
- Optimize the model for edge use (such as with an Arduino, Raspberry PI, Jetson nano, etc.)

---

## Contact

For questions or collaboration:  
**Name** – rajeshratnesh01@gmail.com  
**LinkedIn** – https://www.linkedin.com/in/ratnesh-rajesh  
**GitHub** – https://github.com/R1nesh
