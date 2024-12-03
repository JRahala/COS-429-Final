import cv2

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    if not ret: print("Error recieving frame"); break
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"): break

capture.release()
cv2.destroyAllWindows()