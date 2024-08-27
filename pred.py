from ultralytics import YOLO
import os
import matplotlib.pyplot as plt

# Load your custom trained model
model = YOLO("/content/runs/pose/train3/weights/best.pt")

                                            
images_dir = "/content/data/images/train"   # Specify the directory containing images you want to predict on
x = 0

for filename in os.listdir(images_dir):
    if filename.endswith((".jpg", ".png", ".jpeg")):
        image_path = os.path.join(images_dir, filename)
        x+=1
        if x == 100:
          break
        
        results = model(image_path)

        # Plot the results with Matplotlib
        plt.figure(figsize=(10, 10))  # Adjust figure size as needed
        plt.imshow(results[0].plot()[:, :, ::-1])  # Convert BGR to RGB for Matplotlib
        plt.axis('off')  
        plt.show()