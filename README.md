# Object Transition Matching for Unlabeled Objects

## Overview

This project aims to identify transitions of unknown objects between consecutive frames in a video or image sequence. The primary goal is to generate high-quality training data for a machine learning model that can track objects despite not having predefined object classes.

## Motivation

Traditional object tracking relies on object classification, where models are trained to recognize specific object categories. However, in many real-world applications, objects may not belong to a known class or may lack labeled data. This project tackles the problem by focusing on object transitions rather than classifications, enabling the detection and tracking of arbitrary objects across frames.

## Approach

1. **Object Detection**  
   - Extract objects from two consecutive frames using an object detection function (`detect_objects`).  
   - Each detected object is represented by its pixel mask and bounding box coordinates `(x, y, h, w)`.  

2. **Object Matching**  
   - Compare detected objects across frames based on:  
     - **Intersection over Union (IoU)**: Measures spatial overlap.  
     - **Area Similarity**: Ensures size consistency.  
     - **Euclidean Distance**: Ensures physical proximity.  
   - Remove exact matches to focus only on transitions.  

3. **Filtering and Assignment**  
   - Rank candidate matches based on distance and IoU score.  
   - Ensure each object has at most one match in the next frame.  
   - Store matched object bounding boxes as training data.

## Key Features

- **Class-Agnostic Matching**: Tracks objects based purely on their features, without needing class labels.  
- **Robust Transition Detection**: Prioritizes real transitions over identical object reappearances.  
- **Training Data Generation**: Outputs matched object pairs for supervised learning.  

## Installation

To use this project, ensure you have the following dependencies installed:

```bash
pip install numpy opencv-python
