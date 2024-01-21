import cv2
import time

class ImageCam:
    imagePath = "test.jpg"
    def SaveImage(self):
        cap = cv2.VideoCapture(1)
        TIMER = int(10)
        while True:
            # ret, img = cap.read()
            # cv2.imshow('a', img)
            if True:
                prev = time.time()
                while TIMER >= 0:
                    ret, img = cap.read()

                    # Display countdown on each frame
                    # specify the font and draw the
                    # countdown using puttext
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img, str(TIMER),
                                (200, 250), font,
                                7, (0, 255, 255),
                                4, cv2.LINE_AA)
                    cv2.imshow('currency', cv2.resize(img, (800, 600)))
                    cv2.waitKey(125)

                    # current time
                    cur = time.time()

                    # Update and keep track of Countdown
                    # if time elapsed is one second
                    # than decrease the counter
                    if cur - prev >= 1:
                        prev = cur
                        TIMER = TIMER - 1

                else:
                    ret, img = cap.read()

                    # Display the clicked frame for 2
                    # sec.You can increase time in
                    # waitKey also
                    cv2.imshow('a', cv2.resize(img, (800, 600)))

                    # time for which image displayed
                    cv2.waitKey(10)

                    # Save the frame
                    cv2.imwrite('test.jpg', img)
                    cap.release()
                    cv2.destroyAllWindows()
                    break