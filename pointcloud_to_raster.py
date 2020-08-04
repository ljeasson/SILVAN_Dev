import os
import sys

import matlab.engine

from segment_pointcloud import segment_point_cloud

def specify_directory(directory):
    # Change directory in PointCloudTerrainGenerator.m
    with open('PointCloudTerrainGenerator.m', 'r') as file:
        data = file.readlines()

    #data[0] = "a = importdata('" + str(directory) + "');\n"
    data[0] = "directory_ground = '" + str(directory) + "';\n"
    print(data[0])

    with open('PointCloudTerrainGenerator.m', 'w') as file:
        file.writelines( data )

    # Change directory in GroundDetection.m
    with open('GroundDetection.m', 'r') as file:
        data = file.readlines()

    data[0] = "directory_ground = '" + str(directory) + "';\n"

    with open('GroundDetection.m', 'w') as file:
        file.writelines( data )

def pointcloud_to_raster(directory):
    directory_no_ext = directory[:-4]

    # Classify point cloud into ground and non-ground points using lasground
    print("RUNNING LASGROUND")
    lasground_command = "lasground -i " + str(directory) + " -o " + str(directory_no_ext) + "_segmented.las -fine -step 1 -cpu64"
    print(lasground_command)
    os.system(lasground_command)
    print("DONE\n")

    # Segment ground and non-ground point cloud
    directory = directory_no_ext + "_segmented.las"
    directory_no_ext = directory_no_ext + "_segmented" 
    segment_point_cloud(directory, directory_no_ext)

    # Create heightmap from ground point cloud using MATLAB code
    print("CONVERTING GROUND POINTCLOUD TO HEIGHTMAP")
    specify_directory(str(directory[: directory.rfind(".")]) + "_ground.txt")
    eng = matlab.engine.start_matlab()
    eng.PointCloudTerrainGenerator(nargout=0)
    eng.Gradient(nargout=0)
    eng.GroundDetection(nargout=0)
    print("DONE\n")


if __name__ == "__main__":
    directory = sys.argv[1]
    pointcloud_to_raster(directory)