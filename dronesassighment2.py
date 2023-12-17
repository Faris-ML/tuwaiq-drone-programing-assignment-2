from djitellopy import tello
from cvzone.FaceDetectionModule import FaceDetector
import cv2

drone = tello.Tello()
drone.connect()
drone.stream_on()
drone.takeoff()
drone.move_up(60)
drone.rotate_clockwise(45)
drone.move_forward(20)

detector = FaceDetector()
cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    img, bbox = detector.findFaces(img, draw=True)
    cv2.imshow("image", img)
    if cv2.waitKey(5) & 0xFF == ord ("q"):
        break
drone.land()