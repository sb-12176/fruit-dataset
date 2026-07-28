from ultralytics import YOLO
import cv2
import datetime
from pathlib import Path

target_dir = Path("C:\\fruitDataset\\runs\\detect")
newestTrain = ""
n = 1

# search through the folder of trains. find the newest one (highest number)
for file_path in target_dir.glob("*"):
    if str(file_path).rfind(str(n)):
        newestTrain = file_path
        n = n + 1

# 1. Load your trained or pre-trained YOLO model
model = YOLO(str(newestTrain) + "\\weights\\best.pt")  # Replace with your custom "best.pt" path if needed
print("You are using:" + str(newestTrain) + " model.")

#ask the user what is the name of the file they want to run the detection on
fileName = input("input the name of the file and extension")
# 2. Run inference on an image
results = model("C:\\fruitDataset\\detectionInputs\\" + fileName)

# 3. Get the annotated image array (returns a BGR numpy array)
annotated_image = results[0].plot()

# 4. Display the annotated image using OpenCV
cv2.imshow("YOLO Detections", annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#get the date to add to the file name
date = datetime.datetime.now().strftime("_%d-%m-%Y_%H%M")

# 5. Optional: Save the annotated image to a file
cv2.imwrite("C:\\fruitDataset\\detectionOutputs\\annotated_output" + date + ".jpg", annotated_image)
