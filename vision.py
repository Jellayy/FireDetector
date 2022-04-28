import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import numpy as np
import eel


def monitor_feed():
    # Init segmentor and background frame for background removal
    segmentor = SelfiSegmentation()
    bg_frame = cv2.imread('assets/background.png')
    bg_frame = cv2.resize(bg_frame, (1280, 720))

    # Init Webcam capture
    video = cv2.VideoCapture(0)
    # Init Video file test
    # video = cv2.VideoCapture("IMG_1832.MOV")

    # Color bounds for fire detection
    lower_bound_fire = np.array([252, 254, 254])
    upper_bound_fire = np.array([253, 255, 255])

    # Color bounds for stove top detection
    lower_bound_stove_flame = np.array([125, 58, 5])
    upper_bound_stove_flame = np.array([255, 80, 60])

    # Runtime loop
    while True:
        # Read video feed
        check, frame = video.read()

        # Process Feed
        # Resize Feed
        frame = cv2.resize(frame, (1280, 720))
        # Remove static background from feed
        out = segmentor.removeBG(frame, bg_frame, threshold=0.1)
        # Apply gaussian blur
        processed_frame = cv2.GaussianBlur(out, (9, 9), 0)

        # Create zeroed mask for frame
        mask = np.zeros_like(frame)
        mask[0:1280, 0:720] = [255, 255, 255]

        # Search frame for fire bounds
        image_binary_fire = cv2.inRange(processed_frame, lower_bound_fire, upper_bound_fire)
        # Search frame for lit stove bounds
        image_binary_stove_flame = cv2.inRange(processed_frame, lower_bound_stove_flame, upper_bound_stove_flame)

        # Display video feed
        cv2.imshow("Video Feed", frame)
        cv2.imshow("Processed Feed", image_binary_fire)
        # cv2.imshow("Processed Feed 2", out)
        # cv2.imshow("Processed Feed 2", image_binary_stove_flame)

        # Check if fire bounds are within threshold
        fire_check = cv2.countNonZero(image_binary_fire)
        if fire_check > 30:
            print("A FIRE? AT A SEA PARKS?")
            eel.say_words("dear sir stroke madam FIRE EXCLAMATION MARK")()
        else:
            eel.say_words("no fires at sea parks")()

        # Check if stove top bounds are within threshold
        stove_check = cv2.countNonZero(image_binary_stove_flame)
        if stove_check > 10:
            print("Stove on")

        # Exit case for no video feed
        if not check:
            break
        # Exit case for Q pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()
    video.release()
