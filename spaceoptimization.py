import cv2
import torch
import numpy as np
from ultralytics import YOLO
from sklearn.cluster import KMeans

# Load YOLO model
model = YOLO("yolov8n.pt")  # Use 'yolov8s.pt' for better accuracy

# Open webcam
cap = cv2.VideoCapture(0)

# Get frame size
FRAME_WIDTH = int(cap.get(3))
FRAME_HEIGHT = int(cap.get(4))
TOTAL_AREA = FRAME_WIDTH * FRAME_HEIGHT

def calculate_efficiency(occupied_areas):
    """Calculate percentage of space occupied."""
    if not occupied_areas:
        return 0
    return (sum(occupied_areas) / TOTAL_AREA) * 100

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame)

    object_positions = []
    occupied_areas = []

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            area = (x2 - x1) * (y2 - y1)  # Object area
            occupied_areas.append(area)

            # Store center positions for clustering
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2
            object_positions.append([center_x, center_y])

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Compute space efficiency
    efficiency = calculate_efficiency(occupied_areas)
    cv2.putText(frame, f"Space Efficiency: {efficiency:.2f}%", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # AI-based optimization: Clustering object positions
    if len(object_positions) > 1:
        kmeans = KMeans(n_clusters=min(3, len(object_positions)), random_state=42, n_init=10)
        clusters = kmeans.fit_predict(object_positions)
        centers = kmeans.cluster_centers_

        # Draw suggested reposition points
        for center in centers:
            cv2.circle(frame, (int(center[0]), int(center[1])), 10, (255, 0, 0), -1)  # Suggested position

    # Show frame
    cv2.imshow("AI Space Optimization", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()