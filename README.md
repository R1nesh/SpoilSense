# 🥬 SpoilSense: AI-Powered Produce Spoilage Detection Using YOLOv8

SpoilSense is a lightweight, real-time computer vision system built to detect spoilage in fresh produce using a custom-trained YOLOv8 object detection model. The project uses a dataset of 10,000+ annotated images across various fruit categories to distinguish between fresh and spoiled items — potentially enabling smart monitoring in agricultural, retail, and food supply chain environments.

---

## 🚀 Purpose

The primary objectives of SpoilSense are:

1. To develop a deep learning model capable of **real-time detection** of produce spoilage.
2. To enable accurate classification between **fresh** and **rotten** classes for various fruits.
3. To create a **lightweight**, deployable solution optimized for speed and size (under 6 MB).
4. To build a robust, diverse dataset with **custom annotations** for effective training and generalization.

---

## 🧠 Model Overview

- **Model Type**: YOLOv8 Object Detection (Ultralytics)
- **Architecture**: Convolutional Neural Network (CNN)
- **Dataset Size**: ~10,000 images (manually annotated)
- **Classes**:
  - `Fresh_Apple`, `Rotten_Apple`
  - `Fresh_Banana`, `Rotten_Banana`
  - `Fresh_Tomato`, `Rotten_Tomato`
  - `Fresh_Orange`, `Rotten_Orange`
- **Annotation Format**: YOLO format, with custom class definitions and spatial variance
- **Performance**: Achieved **90%+ mAP** on validation set

---

## 🛠️ Libraries & Tools

The following Python packages are required:

- `torch` – for deep learning operations  
- `ultralytics` – YOLOv8 training and inference  
- `opencv-python` – for image preprocessing and visualization  
- `Pillow` – image handling  
- `numpy` – numerical operations  
- `matplotlib` – plotting metrics  
- `tkinter`, `tkinterdnd2` – optional: GUI-based drag-and-drop demo  

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📊 Results & Model Performance

- **Model Size**: 6 MB  
- **mAP@0.5**: 90%+  
- **Real-Time Inference**: ~30 FPS on standard CPU  
- **Dataset Variance**: Includes lighting, occlusion, rotation, and spoilage stages  

---

## 🖼️ Sample Outputs

Example detections using SpoilSense:

| Input Image | Detection Output |
|-------------|------------------|
| ![input1](assets/example_outputs/input1.jpg) | ![output1](assets/example_outputs/output1.jpg) |
| ![input2](assets/example_outputs/input2.jpg) | ![output2](assets/example_outputs/output2.jpg) |

---

## 🔍 How to Use

### 1. **Clone the repository**
```bash
git clone https://github.com/your-username/SpoilSense.git
cd SpoilSense
```

### 2. **Run Inference**
```bash
python scripts/inference.py --source path/to/image_or_folder --weights model/best.pt
```

### 3. **Optional GUI (Drag-and-Drop Demo)**
```bash
python scripts/gui_demo.py
```

---

## 📦 Dataset

The dataset includes 8 classes:
- Fresh and Rotten variants of: **Apple**, **Banana**, **Tomato**, **Orange**

All images were annotated manually using [Roboflow](https://roboflow.com) and exported in YOLO format, with custom class mappings and varying conditions to simulate real-world environments (e.g., lighting, angle, partial rot).

---

## 💡 Potential Future Improvements

- Retrain the model with a larger set of photos for more accuracy
- Add more fruit/vegetable categories  
- Integrate temperature/humidity sensors for multi-modal spoilage detection  
- Build a mobile app version
- Optimize the model for edge use (such as with an Arduino, Raspberry PI, Jetson nano, etc.)

---

## 📬 Contact

For questions or collaboration:  
**Name** – [rajeshratnesh01@gmail.com]  
**LinkedIn** – [linkedin.com/in/Ratnesh-rajesh]  
**GitHub** – [https://github.com/R1nesh]
