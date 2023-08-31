from ultralytics import YOLO

# loading the pretrained model
model = YOLO("Models/yolov8n-cls.pt")

# Training the model on our custom dataset
data_folder = "C:/Users/othma/Bureau/dataset"
model.train(data=data_folder, epochs=20, imgsz=64)