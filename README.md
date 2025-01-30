# Finding Object Transitions Like Humans

## Overview

Humans are easily able to track unknown objects as they move throughout the environment. This ability is very useful since it allows one to quickly learn about unknown objects
since one can assume that a tracked object is the same object at each time-step, thus evidence regarding the attributes of the object can be aggregated across a duration in time.
This project aims to make an explicit algorithm for tracking unknown objects across timesteps. Inductive biases are made explicit in the algorithm and may be similar to 
inductive biases humans hold about object tracking. For example

1. **Objects Do Not Scale Up Too Fast**
    - Given an object A in frame 1 and two candidate objects B and C in frame 2 (where a candidate object is a candidate for where A transitioned to), if B is more similar in
    appearance to A than C is, but B is much larger than A whereas C is a similar size to A, consider C to be the transitioned object.
    - (A second inductive bias here is that transitioning is a 1 to 1 function).

2. **Objects Do Not Move Too Quickly**
    - Only search for candidate transitions within a window of the first object (do not assume objects teleport, a more likely explanation of a similar object appearing in a 
 new far away location is that it is a new distinct object).

3. **If There Exists an Object in the Same Exact Location in the Next Frame, Lower the Similarity Threshold**
    - It is more likely that the same object is changing shape or color than a different object ending up in the same exact spot as the initial object in the first frame. 

There are of course more inductive biases, different ones that can be used, and more sophisticated ways of implementing inductive biases (i.e. wheighted approaches), 
but making them explicit offers and interpretable approach that can also operate quickly and reflect psychology experiments.

## Approach

1. **Object Detection**  
   - Extract objects from two consecutive frames using OpenCV's contour detection function.  
   - Each detected object is represented by its pixel mask and bounding box coordinates `(x, y, h, w)`.  

2. **Object Matching**  
   - Compare detected objects across frames based on:  
     - **Intersection over Union (IoU)**: Measures spatial overlap.  
     - **Area Similarity**: Ensures size consistency.  
     - **Euclidean Distance**: Ensures physical proximity.  
   - Remove exact match transitions.  

3. **Apply Inductive Biases**  
   - Rank candidate matches based on distance and IoU score.  
   - Apply inductive biases to break 1 to N matches.
   - Ensure final match dictionary is 1 to 1
  
## Example Current State of Transition Detector on one Pair of Frames
(The third pair shows one of the remaining challenges for detecting transitions).
![Jan_30_Transitions](https://github.com/user-attachments/assets/3b679d6e-00d3-4f5d-8ab7-149be7250961)
![t5](https://github.com/user-attachments/assets/e9ae3934-11e1-4697-b97e-d7df4a5994f3)
![t4](https://github.com/user-attachments/assets/8e30be2f-87c0-4b9a-b452-cace2740b286)
![t3](https://github.com/user-attachments/assets/1d91a500-9caa-4f69-93a2-c1dbf45fa39d)
![t2](https://github.com/user-attachments/assets/440a6707-518a-4034-ae32-c8e3c26a1490)



