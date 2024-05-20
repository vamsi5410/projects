import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize the camera
cap = cv2.VideoCapture(0)

# Initialize the hand detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # Get the frame from the camera
    success, img = cap.read()

    # Detect hands
    hands, img = detector.findHands(img)

    # Display the resulting frame
    cv2.imshow("Image", img)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
