import cv2
import numpy as np

cap = cv2.VideoCapture("C:\\Users\\pavani.k\\OneDrive\\Pictures\\cv images\\video 1.htm")

if not cap.isOpened():
    print("Error: Unable to open video file")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Unable to read frame")
        break
    
    pts1 = np.float32([[200, 300], [5, 2], [0, 4], [6, 0]])
    pts2 = np.float32([[0, 0], [4, 0], [0, 1], [4, 6]])
    
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    
    # Check if the frame is not empty before performing the perspective transformation
    if frame.size > 0:
        result = cv2.warpPerspective(frame, matrix, (frame.shape[1], frame.shape[0]))
        
        cv2.imshow('frame', frame)  # Initial Capture
        cv2.imshow('frame1', result)  # Transformed Capture
        
        if cv2.waitKey(24) == 27:
            break
    else:
        print("Error: Empty frame")

cap.release()
cv2.destroyAllWindows()

