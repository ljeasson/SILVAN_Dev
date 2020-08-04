import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def generate_point_cloud_terrain(directory, fileName):
    print(str(directory)+"\\"+str(fileName))

    # Read data from text file
    '''
    a = open(str(directory) + "\\" + str(fileName), "r")
    a = a.read()
    a = a.split("\n")
    data = []
    '''
    x = []
    y = []
    heights = []    
    intensity = []
    
    with open(str(directory) + "\\" + str(fileName), "r") as a:
        for i in a:
            line = i.split(",")
            if len(line) > 1: 
                x.append(float(line[0]))
                y.append(float(line[1]))
                heights.append(float(line[2]))
                intensity.append(float(line[3]))

    print("x:",x[:4])
    print("y:",y[:4])
    print("heights:",heights[:4])
    print("intensity:",intensity[:4])
    print()

    # Set precision
    precision = 0.0625
    print("precision:",precision)
    print()

    # Set height values
    minH = min(heights)
    print("minH:",minH)

    for i in range(len(heights)):
        heights[i] = round(heights[i] - minH, 2)
    print("Averaged heights:",heights[:4])

    maxH = max(heights)
    print("maxH:",maxH)

    sizeH = len(heights)
    print("sizeH:",sizeH)

    rangeH = round(maxH - minH, 2)
    print("rangeH:",rangeH)
    print()

    # Set intensity values
    minInt = min(intensity)
    print("minInt:",minInt)

    maxInt = max(intensity)
    print("maxInt:",maxInt)
    print()

    # Set x,y coordinates with precision level
    minX = min(x)
    print("minX:",minX)

    minY = min(y)
    print("minY:",minY)
    
    xInd = []
    yInd = []
    for i in range(sizeH):
        xInd.append(int(round((x[i]-minX) * precision)))
        yInd.append(int(round((y[i]-minY) * precision)))
    print("xInd:",xInd[:4])
    print("yInd:",yInd[:4])
    print()
    
    # Initialize images
    imgl = np.zeros([int(max(xInd)+1), int(max(yInd)+1)], dtype=int)
    imgm = np.zeros([int(max(xInd)+1), int(max(yInd)+1)], dtype=int)
    texture = np.zeros([int(max(xInd)+1), int(max(yInd)+1)], dtype=int)
    imgl = imgl + 2 * maxH
    imgnorm = np.zeros([int(max(xInd)+1), int(max(yInd)+1)], dtype=int)

    # Produce images
    print("i","\t","x1","y1","\t","intensity[i]","\t","texture[x1][y1]","\t","imgl[x1][y1]","\t","imgm[x1][y1]")
    print("=======================================================================================")

    for i in range(sizeH):
        x1 = xInd[i] + 1
        y1 = yInd[i] + 1
        print(i,"\t",x1,"",y1,"\t",intensity[i])

        texture[x1][y1] = intensity[i]/maxInt
        
        if imgl[x1][y1] > heights[i]:
            imgl[x1][y1] = heights[i]
        
        if imgm[x1][y1] < heights[i]:
            imgm[x1][y1] = heights[i]

        print(i,"\t",x1,"",y1,"\t",intensity[i],"\t\t",texture[x1][y1],"\t\t\t",imgl[x1][y1],"\t\t\t",imgm[x1][y1])
     
    # Max correction
    # ___________________________________
    imglnorm = imgl / np.linalg.norm(maxH)


    imgdiff = imgm-imgl
    imgdnorm = imgdiff / np.linalg.norm(maxH)
    # ___________________________________
    # ___________________________________

    # Display images
    display_imglnorm = Image.fromarray(imglnorm, 'RGB')
    display_imgdnorm = Image.fromarray(imgdnorm, 'RGB')
    
    display_imglnorm.show()
    display_imgdnorm.show()


if __name__ == "__main__":
    generate_point_cloud_terrain("D:\PointClouds", "test_point_cloud.txt")
    #generate_point_cloud_terrain("D:\PointClouds", "USCAYF20180722f1a1_180722_181152_1_dem_filter_reproject.txt")