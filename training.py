from ultralytics import YOLO

model = YOLO("C:\\fruitDataset\\runs\\detect\\train-3\\weights\\best.pt")

results = model.train(data="C:\\fruitDataset\\dataset.yaml", epochs=50, imgsz=650)

