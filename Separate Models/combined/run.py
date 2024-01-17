from ultralytics import YOLO
import cv2
import numpy as np
import math
import datetime
import os
import csv
from keras.models import load_model
from collections import deque
from multiprocessing import Process, Queue

# Function to perform violence detection using a TensorFlow-trained model
def violence_detection(frame, violence_model, Q, consecutive_detection, writer):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (128, 128)).astype("float32")
    frame = frame.reshape(1, 128, 128, 3) / 255  # Reshape to match model input shape

    preds = violence_model.predict(frame)[0]
    Q.put(preds)

    results = np.array(Q.queue).mean(axis=0)
    i = (preds > 0.50)[0]

    if i:
        consecutive_detection += 1
        if consecutive_detection >= 3:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.put(['Violence', 'True', log_filename if log_filename else 'Unknown', timestamp, preds[0]])
            consecutive_detection = 0
    else:
        consecutive_detection = 0

    text = "Violence: {}".format(i)
    FONT = cv2.FONT_HERSHEY_SIMPLEX

    text_color = (0, 255, 0)
    if i:
        text_color = (0, 0, 255)

    cv2.putText(frame, text, (35, 50), FONT, 1.25, text_color, 3)

# Function to process a video file
def process_video(video_path, weapon_model, accident_model, violence_model, log_queue):
    cap = cv2.VideoCapture(video_path)

    # Initialize violence detection variables
    Q = deque(maxlen=128)
    consecutive_detection = 0
    (W, H) = (None, None)  # Add this line to initialize W and H
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    logs_folder = 'logs'
    log_filename = f"{current_date}_logfile.csv"
    log_path = os.path.join(logs_folder, datetime.datetime.now().strftime("%Y"), datetime.datetime.now().strftime("%b"), log_filename)

    os.makedirs(os.path.dirname(log_path), exist_ok=True)  # Ensure the directory exists

    with open(log_path, mode='a', newline='') as file:
        csv_writer = csv.writer(file)

        if os.path.getsize(log_path) == 0:
            csv_writer.writerow(['Detection Type', 'Class', 'Frame Number', 'Timestamp', 'Confidence'])

        while True:
            (grabbed, frame) = cap.read()

            if not grabbed:
                break

            if W is None or H is None:
                (H, W) = frame.shape[:2]

            output = frame.copy()

            # Weapon detection
            weapon_results = weapon_model(frame, stream=True)

            for r in weapon_results:
                boxes = r.boxes
                for box in boxes:
                    conf = box.conf[0]
                    if conf >= 90.0:
                        weapon_detected = True

                        x1, y1, x2, y2 = box.xyxy[0]
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        w, h = x2 - x1, y2 - y1

                        conf = math.ceil((conf * 100)) / 100

                        class_index = int(box.cls[0])
                        class_name = weapon_class_names[class_index]

                        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        log_message = f"Weapon | {class_name} | {cap.get(cv2.CAP_PROP_POS_FRAMES)} | {current_time} | {conf}"

                        csv_writer.writerow(["Weapon", class_name, cap.get(cv2.CAP_PROP_POS_FRAMES), current_time, conf])

                        # Display class name on the frame
                        # cv2.putText(frame, f"{class_name} {conf}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

                        print(log_message)

            # Violence detection
            violence_detection(frame, violence_model, Q, consecutive_detection, log_queue)

            # Accident detection
            accident_results = accident_model(frame, stream=True)

            for r in accident_results:
                boxes = r.boxes
                for box in boxes:
                    conf = box.conf[0]
                    if conf >= confidence_threshold:
                        class_index = int(box.cls[0])
                        class_name = accident_class_names[class_index]

                        if class_name != 'no_accident':
                            accident_detected = True

                            x1, y1, x2, y2 = box.xyxy[0]
                            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                            w, h = x2 - x1, y2 - y1

                            conf = math.ceil((conf * 100)) / 100

                            color = (0, 0, 255)  # Red for accidents
                            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

                            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            log_message = f"Accident | {class_name} | {cap.get(cv2.CAP_PROP_POS_FRAMES)} | {current_time} | {conf}"

                            csv_writer.writerow(["Accident", class_name, cap.get(cv2.CAP_PROP_POS_FRAMES), current_time, conf])

                            # Display class name on the frame
                            cv2.putText(frame, f"{class_name} {conf}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                            print(log_message)

            # Display the processed frame
            cv2.imshow("Image", frame)

            # Check for user exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()

# Create a Queue for inter-process communication
log_queue = Queue()

# List of video file paths to process
video_paths = [
    "D:/KAIF/RJPOLICE_HACK_587_NeuralEnvoys_3/Models/ViolenceDetection/vids/fight04.mp4",
    "D:/KAIF/RJPOLICE_HACK_587_NeuralEnvoys_3/Models/ViolenceDetection/vids/fight02.mp4",
    # Add more file paths as needed
]

weapon_model = YOLO('D:/KAIF/combined/models/customWeapon.pt')
accident_model = YOLO('D:/KAIF/combined/models/RAccidents.pt')

# Load violence detection model
violence_model = load_model('D:/KAIF/combined/models/modelnew.h5')

# Create a Process for each video file
processes = []
for video_path in video_paths:
    process = Process(target=process_video, args=(video_path, weapon_model, accident_model, violence_model, log_queue))
    processes.append(process)
    process.start()

# Wait for all processes to finish
for process in processes:
    process.join()

# Process results from the log_queue if needed
while not log_queue.empty():
    result = log_queue.get()
    print(result)

cv2.destroyAllWindows()