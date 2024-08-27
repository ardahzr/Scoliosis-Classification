# Scoliosis Detection Using YOLOv8x-Pose Model

This project utilizes the YOLOv8x Pose model for scoliosis detection. It employs deep learning techniques to analyze spinal curvature and identify potential cases of scoliosis.

## Project Stages:

1. **Data Preparation (COCO2YOLO.py):**
   - The scoliosis dataset in COCO format is converted to YOLOv8 format. 
   - The conversion includes bounding boxes and keypoints (points on the spine).
   - The `COCO2YOLO.py` script converts the COCO format `annotations.xml` file to YOLO format `.txt` label files.
2. **Model Training (train.py):**
   - A pre-trained YOLOv8x-Pose model is trained for scoliosis detection using the converted dataset.
   - The `train.py` script utilizes training parameters specified in the `config.yaml` file (e.g., epochs=150, imgsz=640).
3. **Prediction and Visualization (pred.py):**
   - The trained model is used to perform scoliosis detection on new images.
   - The `pred.py` script predicts on images in a specified directory and visualizes the results (bounding boxes and keypoints) using Matplotlib.

## Requirements:

- Python 3.7+
- Ultralytics YOLOv8
- Matplotlib

## Installation:

1. Install the required packages:
Use code with caution.
pip install -r requirements.txt
2. Download the dataset in COCO format and place it in the `data` directory.
3. Update the `config.yaml` file with your training parameters.

## Usage:

1. Run the `train.py` script to train the model:
   ```
   python train.py
   ```
2. Run the `pred.py` script to perform prediction on new images and visualize the results:
   ```
   python pred.py
   ```
## Notes:

- This project is intended as a starting point for scoliosis detection.
- Using larger and more diverse datasets is recommended for more accurate results.
- The performance of the model can be further improved by tuning the hyperparameters.

## Future Work:

- Estimation of scoliosis curvature degree.
- 3D spine reconstruction.
- Providing personalized recommendations for scoliosis treatment.
