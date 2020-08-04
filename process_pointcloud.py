#!/usr/bin/python

import os
import glob
import sys, getopt
import matlab.engine

from merge_tiles import merge_tiles
from segment_pointcloud import segment_point_cloud

# https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
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

def process_las_file(directory):
    # Get point cloud file name without ".las"
    directory_no_ext = directory[ : directory.index(".")]
    print(directory_no_ext,"\n")

    # Segment Point Cloud into vegetation and ground
    segment_point_cloud(directory, directory_no_ext)
    
    print("CONVERTING GROUND POINTCLOUD TO HEIGHTMAP")
    specify_directory(str(directory[: directory.rfind(".")]) + "_ground.txt")
    eng = matlab.engine.start_matlab()
    eng.PointCloudTerrainGenerator(nargout=0)
    eng.Gradient(nargout=0)
    eng.GroundDetection(nargout=0)

def main(argv):
    #print('Number of arguments:', len(sys.argv), 'arguments.')
    #print('Argument List:', str(sys.argv))
    
    directory = ''
    directory_no_ext = ''
    print(directory,"\n",directory_no_ext)

    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print('USAGE: process_pointcloud.py -i <input file or directory>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print('USAGE: process_pointcloud.py -i <input file or directory>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            directory = arg

    # If input ends with .laz
    if directory.endswith(".laz"):
        print('Incorrect file format\nUse .las or .laz point clouds')
        sys.exit()
    
    print('Input: ', directory, '\n')

    # IF INPUT IS A POINT CLOUD
    if directory.endswith(".las"):
        directory_no_ext = directory[:directory.rfind(".")]
        
        os.system("mkdir " + str(directory_no_ext))

        process_las_file(directory)

    # IF INPUT IS A DIRECTORY
    else:
        directory_no_ext = directory[:directory.rfind(".")]

        os.system("mkdir " + str(directory_no_ext) + "\\" + str(directory_no_ext[directory_no_ext.rfind("\\")+1:]))

        for subdir, dirs, files in os.walk(directory):
            for file in files:
                process_las_file(os.path.join(subdir, file))
        
        '''
        # Merge directory of tiles
        merge_tiles(directory, 0.1, multiprocess=True)

        merged_directory = ""

        for dirpath,_,filenames in os.walk(directory+"\merged"):
            for f in filenames:
                merged_directory = os.path.abspath(os.path.join(dirpath, f))
        
        merged_directory_no_ext = merged_directory[: merged_directory.index(".")]

        print("merged_directory:",merged_directory,"\n")
        print("merged_directory_no_ext:",merged_directory_no_ext)
        print()

        # Segment Point Clouds into vegetation and ground
        segment_point_cloud(merged_directory, merged_directory_no_ext)
        '''

    '''    
    # Create heightmap from Ground point cloud
    # https://stackoverflow.com/questions/51406331/how-to-run-a-matlab-code-on-python
    # https://www.mathworks.com/help/matlab/matlab-engine-for-python.html

    print("CONVERTING GROUND POINTCLOUD TO HEIGHTMAP")
    specify_directory(str(directory) + "\\merged\\" + str(directory[directory.rfind("\\")+1: ]) + "_merged_subsampled_ground.txt")
    eng = matlab.engine.start_matlab()
    eng.PointCloudTerrainGenerator(nargout=0)
    eng.Gradient(nargout=0)
    eng.GroundDetection(nargout=0)

    print("SAVING HEIGHTMAP TO " + str(directory[:directory.rfind('\\')+1]))   
    os.system('copy "' + str(os.getcwd()) + '\\Heighmap Median 3x3.png" "' + str(directory[:directory.rfind('\\')+1]) + '"')
    print("DONE\n")

    print("ADDING POINTCLOUDS TO UE4")   
    os.system('copy "' + str(directory_no_ext) + '_ground.las" "' + str(os.getcwd()) + '\Content\PointClouds"')
    os.system('copy "' + str(directory_no_ext) + '_vegetation.las" "' + str(os.getcwd()) + '\Content\PointClouds"')
    print("DONE\n")
    '''

if __name__ == "__main__":
    #print(sys.argv[1:])
    main(sys.argv[1:])