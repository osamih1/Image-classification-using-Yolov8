from ultralytics import YOLO

# loading the trained model
model = YOLO("runs/classify/train/weights/last.pt")

# Making a prediction
results = model.predict("image.jpg")
classes = results[0].names
prediction = classes[results[0].probs.top1]
conf = float(results[0].probs.top1conf)

print(f"The predicted class is: {prediction}")
print(f"The confidence score: {conf}")