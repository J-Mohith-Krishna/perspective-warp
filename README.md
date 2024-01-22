# perspective-warp
## What is this repo?
  This repository includes two Python files and two images – one serving as an input and the other as the output. The primary focus of this repository is a computer vision model capable of executing Perspective Warp on a provided image. The detailed functionality and usage of the files are elaborated in the explanation section below.
## Why this repo?
  This repository was initially developed during a hackathon organized by The Greater Chennai Traffic Police at Anna University in December 2023. It serves as a solution or tool developed in response to challenges or objectives presented during the event.
## Explanations-
  ### Car Licence.py=
    **1. Importing Libraries:**
      -cv2: OpenCV library for computer vision tasks.
      -numpy: Numerical computing library for handling arrays.
      -keyboard: Library for working with keyboard events.
      -os: Library for interacting with the operating system.

    **2. Loading the Original Image:**
      -The path to the original image (Plate 1.jpg) is provided.
      -The image is loaded using OpenCV's cv2.imread function.

    **3. Defining Source and Destination Points for Perspective Transformation:**
      -Source points (src) are manually defined, representing the corners of the license plate in the original image.
      -Destination points (dst) are calculated based on a target width and height ratio, forming a rectangle.

    **4. Calculating Perspective Transformation Matrix:**
      -The perspective transformation matrix (M) is calculated using cv2.getPerspectiveTransform based on the source and destination points.

    **5. Applying Perspective Transformation:**
      -The original image is transformed using cv2.warpPerspective with the calculated matrix (M), resulting in the result image.

    **6. Displaying Original Image:**
      -The original image is displayed, and a message prompts the user to press the space bar to mark four matching points on the license plate.

    **7. Marking Points on Original Image:**
      -If the space bar is pressed, four green circles are drawn on the original image at the specified points.
    
    **8. Displaying Transformed Image:**
      -If the space bar is pressed again, the transformed image is displayed along with a message showing the destination points.
    
    **9. Image Saving:**
      -The script saves the transformed image (result) with the filename 'savedImage.jpg' in the specified directory.
      -The list of files in the directory is displayed before and after saving the image.
    
    **10. Closing Windows:**
      -If the space bar is pressed once more, all open windows are closed.
    
    **11. Additional Notes:**
      -The original image path and the save directory are provided as variables for easy customization.
    
    **12. Output:**
      -Success messages are printed indicating the successful completion of image saving.
  ### Vector Analysing.py=
    **1. Importing Libraries:**
      -cv2: OpenCV library for computer vision tasks.
      -numpy: Numerical computing library for handling arrays.
    
    **2. Loading the Original Image:**
      -The path to the original image (Plate 1.jpg) is provided.
      -The image is loaded using OpenCV's cv2.imread function.
    
    **3. Mouse Callback Handler:**
      -A mouse callback function (mouse_handler) is defined to handle left button clicks.
      -When a left button click is detected (cv2.EVENT_LBUTTONUP), the clicked coordinates (x, y) are added to the src list.
      -Green circles are drawn on the image at the selected points, and the updated image is displayed.
    
    **4. Named Window and Mouse Callback Setup:**
      -A named window ('Original Image - Car') is created.
      -The mouse callback function is set for the named window using cv2.setMouseCallback.
    
    **5. Displaying Original Image:**
      -The original image is displayed in the named window ('Original Image - Car').
      -The script waits for a key event (cv2.waitKey(0)) to close the window. In this case, it waits for the space bar (ASCII code 32).
    
    **6. Closing the Window:**
      -If the space bar is pressed, the script closes the window and terminates.
    
    **7. Additional Notes:**
      -The script allows the user to click four points on the image, presumably to be used as source points for a perspective transformation.
      -The selected points are printed as a NumPy array when four points are clicked.
## Conclusion-
  In summary, the provided Python scripts utilize the OpenCV library to perform perspective transformation on images. The first script applies a predefined transformation to correct the perspective of a license plate, allowing customization of source and destination points. The second script, on the other hand, provides an interactive interface for users to manually select four points on an image, potentially for perspective transformation. You can also modify the program for some specific use cases such as image processing and computer vision applications.
