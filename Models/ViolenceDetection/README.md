# Violence Detection in Videos

This Python script uses pre-trained deep learning models to detect instances of violence in video files. It utilizes Keras with OpenCV to process frames, predict violence, and visualize the results in real-time.

## Requirements
- Python 3.x
- OpenCV
- Keras
- Matplotlib
- Numpy

## Setup and Usage

1. **Installation:** Ensure you have Python installed along with the required libraries.
   
2. **Clone Repository:**

    ```bash
    git clone https://github.com/your_username/violence-detection.git
    ```

3. **Setup:**

    - Place your video files for analysis in the `vids` directory.
    - Ensure the pre-trained model `modelnew.h5` is in the root directory.
    
4. **Running the Script:**

    - For real-time violence detection and video processing, execute the script by providing the video file path:

    ```bash
    python violence_detection.py path/to/your/video.mp4
    ```

5. **Output:**

    - The script will process the video, display real-time analysis, and save the processed video in the `output` directory.
    - Detected instances of violence will be logged in the `logs` directory with timestamps in a CSV file.

## Note
- Adjust the threshold for violence detection by modifying the probability threshold in the code (currently set at 0.50).
- The script allows for customization in video path, model choice, and threshold for violence detection.
- Feel free to modify or enhance the code as needed for your specific use case.
