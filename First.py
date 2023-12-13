import cv2
from cvzone.FaceDetectionModule import FaceDetector
from djitellopy import tello 
detector = FaceDetector
cam = cv2.VideoCapture(0)
drone = tello.Tello()

drone.connect
drone.takeoff 
drone.streamon()
drone.move_up(60)

for i in range(4):
    img = drone.get_frame_read().frame
    img, bboxs = detector.findFaces(img,draw = True)
    cv2.imshow("image",img )
    drone.rotate_counter_clockwise(45)
    drone.move_forward(30)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

drone.land()