from ultralytics import YOLO

model = YOLO('yolov8x-pose.pt')

model.train(data='/content/config.yaml', epochs=150, imgsz=640)