from ultralytics import YOLO

model = YOLO("C:\\fruitDataset\\runs\\detect\\train-2\\weights\\best.pt")

results = model.train(data="C:\\fruitDataset\\dataset.yaml", epochs=25, imgsz=650)

