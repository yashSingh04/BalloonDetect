import cv2 as cv
import numpy as np


def imag():
    img = cv.imread('/home/yash/file/task/task.png')
    img2 = img.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
    t1 = cv.imread('/home/yash/file/task/red.png')
    t2 = cv.imread('/home/yash/file/task/green.png')
    t3 = cv.imread('/home/yash/file/task/yellow.png')
    t1 = cv.cvtColor(t1, cv.COLOR_BGR2GRAY)
    t2 = cv.cvtColor(t2, cv.COLOR_BGR2GRAY)
    t3 = cv.cvtColor(t3, cv.COLOR_BGR2GRAY)
    w, h = t1.shape[::-1]
    w, h = t2.shape[::-1]
    w, h = t3.shape[::-1]
    # for red bouy
    meth = cv.matchTemplate(img, t1, cv.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(meth)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    img2 = cv.rectangle(img2,top_left, bottom_right, (0, 0, 255), 2)
    cv.circle(img2, ((top_left[0] + 31, top_left[1] + 42)), 2, (255, 255, 255),-1)
    print(f'the x for Red Bouy is : {top_left[0] + 35} \nthe y for Red Bouy is : {top_left[1] + 40}')
    cv.putText(img2, "Red color", max_loc, cv.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 255)) 



#for green bouy 

    meth2 = cv.matchTemplate(img, t2, cv.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(meth2)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    img2 = cv.rectangle(img2,top_left, bottom_right, (0, 255, 0), 2)
    cv.circle(img2, ((top_left[0] + 35, top_left[1] + 40)), 2, (255, 255, 255),-1)
    print(f'the x for Green Bouy is : {top_left[0] + 35} \nthe y for Green Bouy is : {top_left[1] + 40}')
    cv.putText(img2, "Green color", max_loc, cv.FONT_HERSHEY_SIMPLEX, 0.4,(0, 255, 0)) 


#for yellow bouy
    meth3 = cv.matchTemplate(img, t3, cv.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(meth3)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    img2 = cv.rectangle(img2,top_left, bottom_right, (0, 255, 255), 2)
    cv.circle(img2, ((top_left[0] + 35, top_left[1] + 40)), 2, (255, 255, 255),-1)
    b = f'the x for Yellow Bouy is : {top_left[0] + 35} \nthe y for Yellow Bouy is : {top_left[1] + 40}'
    cv.putText(img2, "Yellow color", max_loc, cv.FONT_HERSHEY_SIMPLEX, 0.4,(0, 255, 255)) 
    print(b)
    cv.imshow("display", img2)



    k = cv.waitKey(0)
    if k == ord('q'): 
        exit()


avg = imag()

print(avg)