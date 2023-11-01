import sys
import cv2
# Create VideoCapture to read
# video
cap = cv2.VideoCapture("mindcraft.mp4")

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), cap.get(cv2.CAP_PROP_FPS), (960, 540))

# Check if video opened successfully
if not cap.isOpened():
    print("Unable to open video...")
    sys.exit()
flower_img = cv2.imread("flower.jpg")
while 1:
    # Read frame from video
    ret, frame = cap.read()
    # Check if frame read 
    # successfully
    if ret == False:
        print("Reched the end of the video...")
        break
    # Resize frame
    ## Display the selfie
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    height, width, _ = frame.shape
    bg_img = cv2.resize(flower_img, dsize=(width, height))
    Green = frame[:, :, 1]
    _,dst = cv2.threshold(Green,200,255,cv2.THRESH_BINARY_INV)
    frame[dst==0] = bg_img[dst==0]
    print(frame.shape)
    # Display the resulting frame
    out.write(frame)
    cv2.imshow('frame', frame)


    if cv2.waitKey(20) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
