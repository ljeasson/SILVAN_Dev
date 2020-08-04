import os
import sys
import cv2 as cv
import numpy as np

def crop_raster_rect(directory, corner_x, corner_y, width, height):
    # Crop image based on corners
    corner_x = int(corner_x)
    corner_y = int(corner_y)
    width = int(width)
    height = int(height)
    
    orig_image = cv.imread(directory)
    cropped_image = orig_image[corner_y:corner_y+height, corner_x:corner_x+width]
    cv.imshow("Cropped Image", cropped_image)
    cv.imwrite(directory[:-4]+"_cropped_rect.png",cropped_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def crop_raster_circle(directory, x, y, r):
    x = int(x)
    y = int(y)
    r = int(r)
    
    orig_image = cv.imread(directory)
    # crop image as a square
    orig_image = orig_image[y:y+r*2, x:x+r*2]
    # create a mask
    mask = np.full((orig_image.shape[0], orig_image.shape[1]), 0, dtype=np.uint8) 
    # create circle mask, center, radius, fill color, size of the border
    cv.circle(mask,(r,r), r, (255,255,255),-1)
    # get only the inside pixels
    fg = cv.bitwise_or(orig_image, orig_image, mask=mask)

    mask = cv.bitwise_not(mask)
    background = np.full(orig_image.shape, 255, dtype=np.uint8)
    bk = cv.bitwise_or(background, background, mask=mask)
    final = cv.bitwise_or(fg, bk)
    cv.imshow('Cropped Image',final)
    cv.imwrite(directory[:-4]+"_cropped_circle.png", final)
    cv.waitKey(0)
    cv.destroyAllWindows()

def patch_raster(directory):
    orig_image = cv.imread(directory)
    width, height = orig_image.shape[:2]

    for i in range(height):
        for j in range(width):
            k = orig_image[j,i]
            print(k, type(k))
            if k == 0:
                orig_image[j,i] = 255
    
    cv.imshow("Patched Image", orig_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def treshold_raster(directory, thresh):
    return

def smooth_raster(directory, kernel_size):
    orig_image = cv.imread(directory)
    
    smoothed_image = cv.medianBlur(orig_image,kernel_size)
    
    #kernel = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size * kernel_size)
    #smoothed_image = cv.filter2D(orig_image,-1,kernel)

    cv.imshow("Smoothed Image", smoothed_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def gradient_raster(directory, kernel_size):
    orig_image = cv.imread(directory)
    gradient_image = cv.Sobel(orig_image,cv.CV_64F,1,0,kernel_size)

    cv.imshow("Gradient Image", gradient_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    directory = sys.argv[1]
    corner_x = sys.argv[2]
    corner_y = sys.argv[3]
    width = sys.argv[4]
    height = sys.argv[5]

    crop_raster_rect(directory, corner_x, corner_y, width, height)
    #crop_raster_circle(directory, corner_x, corner_y, width)

    patch_raster(directory[:-4]+"_cropped_rect.png")
    
    #gradient_raster(directory[:-4]+"_cropped.png", 3)
    #smooth_raster(directory[:-4]+"_cropped.png", 3)