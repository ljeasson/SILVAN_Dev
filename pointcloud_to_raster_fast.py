import os
import sys
import cv2 as cv
import numpy as np

def pointcloud_to_raster_fast(directory):
    directory_no_ext = directory[:-4]

    # Classify point cloud into ground and non-ground points using lasground
    print("RUNNING LASGROUND")
    lasground_command = "lasground -i " + str(directory) + " -o " + str(directory_no_ext) + "_segmented.las -fine -step 1 -cpu64"
    print(lasground_command)
    os.system(lasground_command)
    print("DONE\n")

    # Create raster from ground point cloud
    print("RUNNING BLAST2DEM")
    blast2dem_command = "blast2dem -i " + str(directory_no_ext) + "_segmented.las -o " + str(directory_no_ext) + "_segmented_ground.png -keep_class 2 -nbits 16 -step 1 -kill 999999"
    print(blast2dem_command)
    os.system(blast2dem_command)
    print("DONE\n")


if __name__ == "__main__":
    directory = sys.argv[1]
    pointcloud_to_raster_fast(directory)