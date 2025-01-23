import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_objects(frame,min_size= -1,display=True):
    _, binary = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY)
    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Minimum size for distinct objects

    # List to store cropped objects
    cropped_objects = []
    # Draw bounding boxes for contours that meet the size criteria
    output_image = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)  # Convert grayscale to RGB for visualization
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_size:
            x, y, w, h = cv2.boundingRect(contour)
            
            cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Crop the region inside the bounding box
            cropped_object = frame[y:y+h, x:x+w]
            #if cropped object not all black
            if np.any(cropped_object):
                cropped_objects.append((cropped_object, (x, y, w, h)))
    if display:
        # Display the result with bounding boxes
        plt.figure(figsize=(10, 10))
        plt.imshow(output_image)
        plt.axis("off")
        plt.show()
    return cropped_objects

def visualize_transitions(frame1, frame2, transitions):
    # Convert grayscale frames to RGB for visualization
    frame1_rgb = cv2.cvtColor(frame1, cv2.COLOR_GRAY2RGB)
    frame2_rgb = cv2.cvtColor(frame2, cv2.COLOR_GRAY2RGB)

    # Iterate through each transition
    for i, transition in enumerate(transitions):
        frame1_bbox, frame2_bbox = transition

        # Make copies of the frames for each individual visualization
        frame1_copy = frame1_rgb.copy()
        frame2_copy = frame2_rgb.copy()

        # Draw the bounding box on frame1
        x1, y1, w1, h1 = frame1_bbox
        cv2.rectangle(frame1_copy, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)

        # Draw the bounding box on frame2
        x2, y2, w2, h2 = frame2_bbox
        cv2.rectangle(frame2_copy, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)

        # Display the frames with bounding boxes
        plt.figure(figsize=(12, 6))
        
        plt.subplot(1, 2, 1)
        plt.title(f"Frame 1: Transition {i+1}")
        plt.imshow(frame1_copy)
        plt.axis("off")
        
        plt.subplot(1, 2, 2)
        plt.title(f"Frame 2: Transition {i+1}")
        plt.imshow(frame2_copy)
        plt.axis("off")
        
        plt.show()