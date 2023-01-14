from PIL import ImageGrab
import cv2
import numpy as np

# Naming a window
cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)

# Using resizeWindow()
cv2.resizeWindow("Resized_Window", 900, 600)

while True:
    # Get the screen capture
    screen = ImageGrab.grab()

    # Convert the PIL image to a numpy array
    frame = np.array(screen)

    # convert from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Displaying the image
    cv2.imshow("Resized_Window", frame)

    # Check for a key press
    key = cv2.waitKey(1)
    if key == ord('q'):
        # 'q' key was pressed, so exit the loop
        break


# Close the window
cv2.destroyAllWindows()
