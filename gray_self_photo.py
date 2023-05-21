import numpy as np
import cv2 as cv
import datetime
import os

cap = cv.VideoCapture(0)
i = 1
selected_images = []

if not os.path.exists('photo'):
    os.makedirs('photo')
    
letter = "Press 's' to capture, 'c' to cancel." 

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Frame capture
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break
    letter2 = "Captured "+str(i-1)+" images"

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    show = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.putText(show , letter, (10, 100), cv.FONT_ITALIC, 1, (0, 255, 0))
    cv.putText(show , letter2, (10, 400), cv.FONT_ITALIC, 1, (0, 255, 0))
    cv.imshow('camera', show)

    key = cv.waitKey(1)
    




    if key == ord('q'):
        if len(selected_images) < 4:
            letter = "Select at least four images by pressing 's' before 'q'."
        else:
            selected_images = [cv.resize(img, (0, 0), fx=0.5, fy=0.5) for img in selected_images]
            montage = np.hstack(selected_images)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            result_filename = 'photo/result_' + timestamp + '.jpg'
            cv.imshow('result', montage)
            cv.imwrite(result_filename, montage)
            cv.waitKey(0)
            break

    if key == ord('w'):
        if len(selected_images) < 4:
            letter = "Select at least four images by pressing 's' before 'q'."
        else:
            
            montage = np.vstack(selected_images)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            result_filename = 'photo/result_' + timestamp + '.jpg'
            cv.imshow('Montage', montage)
            cv.imwrite(result_filename, montage)
            cv.waitKey(0)
            break

    if key == ord('s'):
        letter = "Press 's' to capture, 'c' to cancel." 
        #cv.imwrite('gray/' + str(i) + '.jpg', gray)
        cv.imshow('gray' + str(i), gray)
        i += 1
        selected_images.append(gray)
        cv.imshow('selected',np.hstack([cv.resize(img, (0, 0), fx=0.5, fy=0.5) for img in selected_images]))
        
        if len(selected_images) >= 4:
            letter = "Press 'q' : horizontally or 'w' : vertically"
    
    if key == ord('c'):
        if i==1:
            letter = "no photo to cancel"
            
        else:
            i -= 1
            selected_images.pop()
            cv.destroyWindow('gray' + str(i)) 
            if i != 1:
                cv.imshow('selected',np.hstack([cv.resize(img, (0, 0), fx=0.5, fy=0.5) for img in selected_images]))
            else:
                cv.destroyWindow('selected')
        if len(selected_images) < 4:
            letter = "Press 's' to capture, 'c' to cancel."

        
os.startfile('photo')
cap.release()
cv.destroyAllWindows()
