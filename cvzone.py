from cvzone.HandTrackingModule import HandDetector
import cv2
import os
import numpy as np
import win32com.client

# Initialize PowerPoint application
Application = win32com.client.Dispatch("PowerPoint.Application")
Presentation = Application.Presentations.Open(r"C:\Users\Vamsi\OneDrive\Documents\Custom Office Templates\UNIT-I IRS final.pptx")
print(Presentation.Name)
Presentation.SlideShowSettings.Run()

# Parameters
width, height = 900, 720
gestureThreshold = 300

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand Detector
detectorHand = HandDetector(detectionCon=0.8, maxHands=1)
# Variables
delay = 30
buttonPressed = False
counter = 0

while True:
    # Get image frame
    success, img = cap.read()
    imgCurrent = img.copy()
    # Find the hand and its landmarks
    hands, img = detectorHand.findHands(img)  # with draw
    if hands and buttonPressed is False:  # If hand is detected
        hand = hands[0]
        cx, cy = hand["center"]
        lmList = hand["lmList"]  # List of 21 Landmark points
        fingers = detectorHand.fingersUp(hand)  # List of which fingers are up
        if cy <= gestureThreshold:  # If hand is at the height of the face
            if fingers == [1, 1, 1, 1, 1]:
                print("Next")
                buttonPressed = True
                Presentation.SlideShowWindow.View.Next()
            if fingers == [1, 0, 0, 0, 0]:
                print("Previous")
                buttonPressed = True
                Presentation.SlideShowWindow.View.Previous()

    if buttonPressed:
        counter += 1
        if counter > delay:
            counter = 0
            buttonPressed = False

    cv2.imshow("Image", imgCurrent)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
Application.Quit()
