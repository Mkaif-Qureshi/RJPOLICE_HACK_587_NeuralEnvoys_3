from keras.models import load_model
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import argparse
import pickle
import cv2
import time 
import os
import h5py
from collections import deque
from datetime import datetime
import csv
from multiprocessing import Process

def print_results(video, limit=None):
    if not os.path.exists('output'):
        os.mkdir('output')

    if not os.path.exists('logs'):
        os.mkdir('logs')

    print("Loading the model...")
    model = load_model('modelnew.h5')
    Q = deque(maxlen=128)
    vs = cv2.VideoCapture(video)
    writer = None
    (W, H) = (None, None)
    count = 0
    consecutive_detection = 0
    current_date = datetime.now().strftime("%Y-%m-%d")
    logs_folder = 'logs'
    log_filename = f"{current_date}_logfile.csv"
    log_path = os.path.join(logs_folder, log_filename)

    with open(log_path, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        
        if os.path.getsize(log_path) == 0:
            csv_writer.writerow(['Violence Detected', 'Filename/Cam Name', 'Time and Date', 'Probability'])

        while True:
            (grabbed, frame) = vs.read()

            if not grabbed:
                break

            if W is None or H is None:
                (H, W) = frame.shape[:2]

            output = frame.copy()

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (128, 128)).astype("float32")
            frame = frame.reshape(128, 128, 3) / 255

            preds = model.predict(np.expand_dims(frame, axis=0))[0]
            Q.append(preds)

            results = np.array(Q).mean(axis=0)
            i = (preds > 0.50)[0]

            # Log entry if violence detected with >= 0.50 probability for 3 consecutive frames
            if i:
                consecutive_detection += 1
                if consecutive_detection >= 3:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    csv_writer.writerow(['Yes', log_filename if log_filename else 'Unknown', timestamp, preds[0]])
                    consecutive_detection = 0 

            else:
                consecutive_detection = 0  

            text = "Violence: {}".format(i)
            FONT = cv2.FONT_HERSHEY_SIMPLEX 

            text_color = (0, 255, 0) 
            if i:
                text_color = (0, 0, 255)

            cv2.putText(output, text, (35, 50), FONT, 1.25, text_color, 3)

            if writer is None:
                fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                writer = cv2.VideoWriter(os.path.join('output', f"{current_date}_v_output.avi"), fourcc, 30, (W, H), True)

            writer.write(output)

            cv2.imshow("OUTPUT", output)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

    print("Closing...")
    if writer:
        writer.release()
    vs.release()
    cv2.destroyAllWindows()

def process_video(video_path):
    print_results(video_path)

if __name__ == "__main__":
    video_paths = [
        r"D:\KAIF\RJPOLICE_HACK_587_NeuralEnvoys_3\Models\ViolenceDetection\vids\fight05.mp4",
        r"D:\KAIF\RJPOLICE_HACK_587_NeuralEnvoys_3\Models\ViolenceDetection\vids\vid1.mp4",
    ]

    processes = []

    for video_path in video_paths:
        process = Process(target=process_video, args=(video_path,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
