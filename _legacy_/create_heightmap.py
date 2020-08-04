import os
import random
import matlab.engine

def get_index_positions(listOfElements, element):
    indexPosList = []
    indexPos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            indexPos = listOfElements.index(element, indexPos)
            # Add the index position in list
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
    return indexPosList

def get_lasheader_info(pc):
    header_info = []
    os.system("lasinfo -i " + pc + " -o info.txt")
    file = open("info.txt", "r")
    info = file.read()
    info = info.split("\n")
    for i in info:
        i = i.split(' ')
        #blank_indices = get_index_positions(i, '')
        i = [e for e in i if e not in ('')]
        header_info.append(i)
    return header_info

def count_points(info):
    num_ground=num_veg = 0
    for i in info:
        if 'ground' in i:
            num_ground = int(i[0])
        if 'vegetation' in i:
            num_veg = int(i[0])
    num_points = num_ground + num_veg
    return num_points

def get_boundaries(info):
    minx=maxx=miny=maxy=minz=maxz = 0
    for i in info:
        if 'min' in i:
            minx = float(i[4])
            miny = float(i[5])
            minz = float(i[6])
        if 'max' in i:
            maxx = float(i[4])
            maxy = float(i[5])
            maxz = float(i[6])
        '''
        if 'X' in i:
            minx = int(i[1])
            maxx = int(i[2])
        if 'Y' in i:
            miny = int(i[1])
            maxy = int(i[2])
        if 'Z' in i:
            minz = int(i[1])
            maxz = int(i[2])
        '''
    return (minx, maxx, miny, maxy, minz, maxz)

def normalize(z, Zmin, Zmax):
    return int((z - Zmin) / (Zmax - Zmin) * 255)

def scale(Z, minimum, s):
    return (2**16 - 1) * ((Z - minimum)/s)

def find_2nd(string, substring):
   return string.find(substring, string.find(substring) + 1)

def create_heightmap(point_cloud, fileName):
    # Extract information using LASHEADER 
    header_info = get_lasheader_info(point_cloud)

    # Get min and max z values 
    #pc_num_points = count_points(header_info)
    boundaries = get_boundaries(header_info)
    print("Boundaries:",boundaries)

    # Set Zmax and Zmin based on boundaries
    Zmin = boundaries[4]
    Zmax = boundaries[5]
    scaling_factor = Zmax - Zmin
    print("\nZmin:",Zmin,"\nZmax:",Zmax,"\nScaling Factor:",scaling_factor)

    with open(str(fileName) + "_ground.txt", "rt") as fin:
        with open("RESCALED_" + str(fileName) + "_ground.txt", "wt") as fout:  
        
            for line in fin:
                info = line.split(",")
                    
                currentZ = float(info[2])
                scaledZ = scale(currentZ, Zmin, Zmax)

                newline = line.replace(line[find_2nd(line, ',')+1:], str("%.2f" % scaledZ)+"\n")
                fout.write(line.replace(line[find_2nd(line, ',')+1:], str("%.2f" % scaledZ)+"\n"))

    print("\nRUNNING BLAST2DEM")
    #os.system("dir/s/b RESCALED*.txt > ground_txt_tile_list.txt")
    #os.system("blast2dem -lof ground_txt_tile_list.txt -merged -elevation -o UAV_LIDAR_GROUND_HEIGHTMAP_FINAL_FROM_FILE.tif")
    os.system("blast2dem -i RESCALED_" + str(fileName) + "_ground.txt" + " -merged -elevation -o " + str(fileName) + "_NEW.tif")
    #os.system("blast2dem -i " + str(point_cloud) + " -merged -elevation -o " + str(fileName) + "_NEW.tif")
    print("DONE\n")

    print("RUNNING GDAL_TRANSLATE")
    gdal_translate_command = "gdal_translate -of GTiff -ot Byte -scale 0 65535 0 255 "+str(fileName)+"_NEW.tif "+str(fileName)+"_NEW_RESCALED.tif"
    os.system(gdal_translate_command)
    print("DONE")


def create_heightmap_v2(directory, fileName):
    print(str(directory)+"\\"+str(fileName))

    eng = matlab.engine.start_matlab()
    eng.PointCloudTerrainGenerator(nargout=0)
    eng.Gradient(nargout=0)
    eng.GroundDetection(nargout=0)

if __name__ == "__main__":
    create_heightmap_v2("D:\PointClouds", "test_point_cloud.txt")