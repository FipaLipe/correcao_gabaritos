import cv2

#cap = cv2.VideoCapture('assets/teste_01.jpeg')

width = 1000
height = 540

tresh = [0,0]
# def nothing(x):
#     pass

# cv2.namedWindow("Trackbars")
# cv2.createTrackbar("tresh_01", "Trackbars", 0, 1000, nothing)
# cv2.createTrackbar("tresh_02", "Trackbars", 0, 1000, nothing)


while True:
    #ret, frame = cap.read()

    frame = cv2.imread("assets/teste_01.jpeg")

    frame = cv2.resize(frame, (width, height))

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame_blur = cv2.GaussianBlur(frame_gray, (5,5), 0)

    #tresh = cv2.getTrackbarPos("tresh_01", "Trackbars"), cv2.getTrackbarPos("tresh_02", "Trackbars")
    tresh = [70, 160]
    frame_canny = cv2.Canny(frame_blur, tresh[0], tresh[1])

    contours = cv2.findContours(frame_canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow("FRAME", frame_canny)
    
    if cv2.waitKey(1) == ord('q'):
        break

#cap.release()
cv2.destroyAllWindows()