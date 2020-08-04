import os
import glob
import sys

def segment_point_cloud(directory, directoryNoExt, denoise=False, interpolation=False, interpolation_factor=350):
    print("RUNNING LAS2TXT")
    las2txt_command = "las2txt -i " + str(directory) + " -o " + str(directoryNoExt) + ".txt -parse xyzic -sep comma"
    print(las2txt_command)
    os.system(las2txt_command)
    print("DONE\n")

    print("POPULATE GROUND, VEG, ETC TXT FILES")
    with open(str(directoryNoExt) + ".txt", "rt") as fin:
        with open(str(directoryNoExt) + "_ground.txt", "wt") as fout_G: #Ground
            for line in fin:
                line_split = line.split(',')
                if line_split[4] == '2\n':
                    fout_G.write(line)
            '''
            with open(str(directoryNoExt) + "_vegetation.txt", "wt") as fout_V: #Vegetation
                with open(str(directoryNoExt) + "_building.txt", "wt") as fout_B: #Building
                    with open(str(directoryNoExt) + "_unclassified.txt", "wt") as fout_U: #Unclassified
                        for line in fin:
                            line_split = line.split(',')
                            if line_split[4] == '1\n':
                                fout_U.write(line)
                            if line_split[4] == '2\n':
                                fout_G.write(line)
                            if line_split[4] == '3\n' or line_split[4] == '4\n' or line_split[4] == '5\n':
                                fout_V.write(line)
                            if line_split[4] == '6\n':
                                fout_B.write(line)
            '''         
    print("DONE\n")

    '''
    print("RUNNING TXT2LAS FOR GROUND")
    txt2las_ground_command = "txt2las -i " + str(directoryNoExt) + "_ground.txt -o " + str(directoryNoExt) + "_ground.las -parse xyzic"
    print(txt2las_ground_command)
    os.system(txt2las_ground_command)
    if denoise: os.system("lasnoise -i " + str(directoryNoExt) + "_ground.las -o "+ str(directoryNoExt) + "_ground_no_noise.las -remove_noise -ignore_class 2")
    print("DONE\n")

    print("RUNNING TXT2LAS FOR VEGETATION")
    txt2las_veg_command = "txt2las -i " + str(directoryNoExt) + "_vegetation.txt -o " + str(directoryNoExt) + "_vegetation.las -parse xyzic" 
    print(txt2las_veg_command)
    os.system(txt2las_veg_command)
    if denoise: os.system("lasnoise -i " + str(directoryNoExt) + "_vegetation.las -o "+ str(directoryNoExt) + "_vegetation_no_noise.las -remove_noise -ignore_class 2")
    print("DONE\n")

    print("RUNNING TXT2LAS FOR BUILDING")
    txt2las_building_command = "txt2las -i " + str(directoryNoExt) + "_building.txt -o " + str(directoryNoExt) + "_building.las -parse xyzic"
    print(txt2las_building_command)
    os.system(txt2las_building_command)
    if denoise: os.system("lasnoise -i " + str(directoryNoExt) + "_building.las -o "+ str(directoryNoExt) + "_building_no_noise.las -remove_noise -ignore_class 2")
    print("DONE\n")
    
    print("RUNNING TXT2LAS FOR UNCLASSIFIED")
    txt2las_unclassified_command = "txt2las -i " + str(directoryNoExt) + "_unclassified.txt -o " + str(directoryNoExt) + "_unclassified.las -parse xyzic"
    print(txt2las_unclassified_command)
    os.system(txt2las_unclassified_command)
    if denoise: os.system("lasnoise -i " + str(directoryNoExt) + "_unclassified.las -o "+ str(directoryNoExt) + "_unclassified_no_noise.las -remove_noise -ignore_class 2")
    print("DONE\n")
    '''

    if interpolation:
        print("RUNNING LAS2DEM FOR GROUND")
        os.system("las2dem -i " + str(directoryNoExt) + "_ground.las -o "+ str(directoryNoExt) + "_ground.laz -kill " + str(interpolation_factor))
        print("RUNNING LASZIP FOR GROUND")
        os.system("laszip -i " + str(directoryNoExt) + "_ground.laz")
        print("RUNNING LASTHIN FOR GROUND")
        os.system("lasthin -i " + str(directoryNoExt) + "_ground.las -o " + str(directoryNoExt) + "_ground_thinned.las -highest -step 2.0 -adaptive 0.2 5.0")
        print("RUNNING LAS2TXT FOR GROUND")
        os.system("las2txt -i " + str(directoryNoExt) + "_ground_thinned.las -o " + str(directoryNoExt) + "_ground_thinned.txt -parse xyzic -sep comma")
        print("DONE\n")

if __name__ == "__main__":
    directory = sys.argv[1]
    directory_no_ext = sys.argv[1][:-4]
    segment_point_cloud(directory, directory_no_ext)