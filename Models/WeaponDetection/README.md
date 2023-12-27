# Weapon Detection using Convolutional Neural Networks (CNN)

This repository contains Python code snippets for weapon detection tasks using CNNs. The provided snippets cover model training, image prediction, and real-time video prediction.

## Tasks Covered

### 1. Model Training:
- **Purpose:** Train a CNN model to classify images of weapons (guns, knives, long guns) into respective categories.
- **Files:** `train_weapon_classifier.py`

### 2. Image Prediction using Trained Model:
- **Purpose:** Load a pre-trained model to predict the classes of weapon-related images from a specified test directory.
- **Files:** `predict_weapon_classes.py`

### 3. Real-Time Video Prediction:
- **Purpose:** Perform real-time weapon detection from a webcam feed using a pre-trained model.
- **Files:** `real_time_weapon_detection.py`

## Usage Instructions

### 1. Model Training:
- Run `train_weapon_classifier.py` to train the CNN model.
- Ensure the directory structure for training images is organized by weapon categories (e.g., 'Knife', 'Gun', 'Long Gun').

### 2. Image Prediction using Trained Model:
- Execute `predict_weapon_classes.py` to predict weapon classes from a specified test directory.
- Place images to be predicted in the test directory.

### 3. Real-Time Video Prediction:
- Run `real_time_weapon_detection.py` to perform real-time weapon detection using a webcam feed.
- Ensure a webcam is connected and accessible.

## Requirements
- Python 3.x
- Libraries: Keras, TensorFlow, OpenCV, NumPy, PIL (Python Imaging Library)

## Notes
- Modify file paths, model names, and image dimensions as needed.
- Adjust model hyperparameters, such as batch size, epochs, and layers, for optimal performance.
- The real-time video prediction script uses a webcam (default ID: 0). Modify the `cv2.VideoCapture()` argument for a different camera.

## Disclaimer
- This code serves as an educational example and might require modifications for specific use cases or deployment scenarios.
