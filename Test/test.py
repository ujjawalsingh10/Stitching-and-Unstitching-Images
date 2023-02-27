import cv2 as cv
import numpy as np
import os

#img1 = cv.imread('cap_left/cap_left_0.jpg')
#mg2 = cv.imread('cap_right/cap_right_0.jpg')

#stitch = cv.hconcat((img1, img2))

#cv.imshow('Using hstack', stitch)

# defining the kernel for Erosion and Dilation
#kernel = np.ones((5, 5), np.uint8)
kernel = np.ones((12, 12), np.uint8)
kernel2 = np.ones((13, 13), np.uint8)

def load_images_from_folder(left, right):
    images = []
    i = 0
    for filename1, filename2 in zip(os.listdir(left), os.listdir(right)):
        img1 = cv.imread(os.path.join(left, filename1))
        img2 = cv.imread(os.path.join(right, filename2))

        
        #Grayscaling
        img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        img1_gray = cv.Canny(img1_gray, 50, 75 )
        img2_gray = cv.Canny(img2_gray, 50, 75 )


        #Binarize the image
        # img1binr = cv.threshold(img1_gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
        # img2binr = cv.threshold(img2_gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]

        # opening the image
        # opening = cv.morphologyEx(img1binr, cv.MORPH_TOPHAT,kernel, iterations=1)
        # closing = cv.morphologyEx(img2binr, cv.MORPH_TOPHAT,kernel2, iterations=1)
        
        opening = cv.morphologyEx(img1_gray, cv.MORPH_TOPHAT,kernel, iterations=1)
        closing = cv.morphologyEx(img2_gray, cv.MORPH_BLACKHAT,kernel2, iterations=1)
        
        #### Morphological operations
        #Erosion
        # img1Erosion = cv.erode(img1_gray, kernel, iterations=1)
        # ##Dilation
        # img2Dilation = cv.dilate(img2_gray, kernel2, iterations=1)


        ###Writing on the image
        cv.putText(opening, "Opening", (50,50), cv.FONT_HERSHEY_DUPLEX, 1.5,(255, 165, 0),2,cv.LINE_AA)
        cv.putText(closing, "Closing", (50,50), cv.FONT_HERSHEY_DUPLEX, 1.5,(255, 165, 0),2,cv.LINE_AA)


        #if img is not None:
        #    images.append(img)
        
        #stitched_image = cv.hconcat((img1Erosion,img2Dilation))
        stitched_image = cv.hconcat((opening,closing))
        
        #cv.imshow("stitched_image", stitched_image)
        # filename = 'test/Stitched_images/Image'+str(i)+'.png'
        # cv.imwrite(filename, stitched_image) #  .png !
        # i +=1

        if not os.path.exists("test/Stitched_images/"):
           print("Hello")
           os.makedirs("test/Stitched_images")
           print("YOYO whatup")
           filename = 'test/Stitched_images/Image'+str(i)+'.png'
           cv.imwrite(filename, stitched_image) #  .png !
           i +=1

def load_images_for_unstitching(folder3):
    i = 0
    for filename in os.listdir(folder3):
        img = cv.imread(os.path.join(folder3, filename))

        img1 = img[:, :640, :]
        img2 = img[:, 640:1280, :]

        if not os.path.exists("test/unstitched/left_cap/"):
            os.makedirs("test/unstitched/left_cap")
            filename = 'test/unstitched/left_cap/img'+str(i)+'.png'
            print(filename)
            cv.imshow("left side", img1)
            cv.imshow("right side", img2)
            cv.imwrite(filename, img1)
            i +=1

        
            

load_images_from_folder('test/cap_left', 'test/cap_right')
load_images_for_unstitching('test/Stitched_images')
cv.waitKey(0)

