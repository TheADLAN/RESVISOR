import cv2
import imutils

cam = cv2.VideoCapture(0)

#cv2.namedWindow("image")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    frame = cv2.resize(frame, (800, 480))
    cv2.imshow("IMAGE XD", frame)


    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "Picture_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()

cv2.destroyAllWindows()