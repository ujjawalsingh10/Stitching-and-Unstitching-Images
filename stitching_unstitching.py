import cv2 as cv
import numpy as np
import os

#img1 = cv.imread('cap_left/cap_left_0.jpg')
#mg2 = cv.imread('cap_right/cap_right_0.jpg')

#stitch = cv.hconcat((img1, img2))

#cv.imshow('Using hstack', stitch)

#Defining the kernel for Erosion and Dilation
kernel = np.ones((5,5), np.uint8)

def load_images_from_folder(folder1, folder2):
    i = 0
    for filename1, filename2 in zip(os.listdir(folder1), os.listdir(folder2)):
        img1 = cv.imread(os.path.join(folder1, filename1))
        img2 = cv.imread(os.path.join(folder2, filename2))
        
        ####Performing GrayScaling
        img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        #### Morphological operations
        #Erosion
        img1Erosion = cv.erode(img1, kernel, iterations=1)
        ##Dilation
        img2Dilation = cv.dilate(img2, kernel, iterations=1)

        ### Adding text on the image
        cv.putText(img1Erosion, "Erosion", (50,50), cv.FONT_HERSHEY_DUPLEX, 1.5,(255, 165, 0),2,cv.LINE_AA)
        cv.putText(img2Dilation, "Dilation", (50,50), cv.FONT_HERSHEY_DUPLEX, 1.5,(255, 0, 0),2,cv.LINE_AA)


        ####
        #if img is not None:
        #    images.append(img)
        stitched_image = cv.hconcat((img1Erosion,img2Dilation))
        #print(f"Image shape {img1.shape}  |  StitchedImage shape: {stitched_image.shape}")

        try:
            if not os.path.exists("Stitched_images/"):
                os.makedirs("Stitched_images")
            
        except OSError:
            print("Error creating directory")
        
        filename = 'Stitched_images/Image'+str(i)+'.png'
        cv.imwrite(filename, stitched_image) #  .png !
        i +=1

def load_images_for_unstitching(folder3):
    i = 0
    j = 0
    for filename in os.listdir(folder3):
        img = cv.imread(os.path.join(folder3, filename))

        img1 = img[:, :640, :]
        img2 = img[:, 640:1280, :]

        # if not os.path.exists("Unstitched/left_cap/"):
        #     os.makedirs("Unstitched/left_cap")
        #     file = 'Unstitched/left_cap/img'+str(i)+'.png'
        #     #print(filename)
        #     #cv.imshow("left side", img1)
        #     #cv.imshow("right side", img2)
        #     cv.imwrite(file, img1)
        #     i +=1
        
        # if not os.path.exists("Unstitched/right_cap/"):
        #     os.makedirs("Unstitched/right_cap")
        #     file2 = 'Unstitched/right_cap/img'+str(j)+'.png'
        #     #print(filename)
        #     #cv.imshow("left side", img1)
        #     #cv.imshow("right side", img2)
        #     cv.imwrite(file2, img2)
        #     j +=1

        if not os.path.exists("Unstitched/left_cap/"):
            os.makedirs("Unstitched/left_cap")
            os.makedirs("Unstitched/right_cap")
        file1 = 'Unstitched/left_cap/img'+str(i)+'.png'
        file2 = 'Unstitched/right_cap/img'+str(i)+'.png'
        #print(filename)
        #cv.imshow("left side", img1)
        #cv.imshow("right side", img2)
        cv.imwrite(file1, img1)
        cv.imwrite(file2, img2)
        i +=1

load_images_from_folder('cap_left', 'cap_right')
load_images_for_unstitching('Stitched_images')

#cv.waitKey(0)

