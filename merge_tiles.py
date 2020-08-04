import os
import glob
from multiprocessing import Process

def las2las_tile(directory, tile):
    las2las_tile_command = "las2las -i " + str(directory) + "\\" + str(tile) + " -set_version 1.4 -keep_random_fraction 0.1 -odir " + str(directory) + "\converted_subsampled"
    #print(las2las_tile_command)
    #print("Process Start:", tile)
    os.system(las2las_tile_command)
    #print("Processing",directory,tile,"Done")

def merge_tiles(directory, subsample_factor, multiprocess=False, remove_buffer=False):  
    # If directory ends with "\", remove it and get file name
    if directory.strip()[-1] is "\\": directory = directory[:-1]
    filename = directory[directory.rfind("\\")+1 :]
    
    os.system("mkdir " + directory + "\converted_subsampled")
    os.system("mkdir " + directory + "\merged")

    print("RUNNING LAS2LAS ON TILES")
    # https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists
    if multiprocess:
        processes = []
        tiles = os.listdir(directory)
        tile_chunks = [tiles[x:x+20] for x in range(0, len(tiles), 20)]

        for chunk in tile_chunks:
            print("Processing",chunk[:5])
            
            for tile in chunk:
                p = Process(target=las2las_tile, args=(directory, tile))
                processes.append(p)

            for p in processes: p.start()
            for p in processes: p.join()

            print("Processing Done\n")
            processes = []

    else:    
        las2las_command_las = "las2las -i " + str(directory) + "\*.las -set_version 1.4 -keep_random_fraction 0.1 -odir " + str(directory) + "\converted_subsampled" 
        print(las2las_command_las)
        os.system(las2las_command_las)

        las2las_command_laz = "las2las -i " + str(directory) + "\*.laz -set_version 1.4 -keep_random_fraction 0.1 -odir " + str(directory) + "\converted_subsampled" 
        print(las2las_command_laz)
        os.system(las2las_command_laz)
        
    print("DONE\n")
    
    print("RUNNING LASMERGE")
    if remove_buffer:
        os.system("lastile -i " + str(directory) + "\*.las -remove_buffer -odir " + str(directory) + "\converted_subsampled")
    lasmerge_command = "lasmerge -i " + str(directory) + "\converted_subsampled\*.las -o " + str(directory) + "\merged\\" + str(filename) + "_merged.las"
    print(lasmerge_command)
    os.system(lasmerge_command)
    print("DONE\n")

    print("RUNNING LAS2LAS ON MERGED POINT CLOUD")
    las2las_command = "las2las -i " + str(directory) + "\merged\*.las -set_version 1.4 -keep_random_fraction " + str(subsample_factor) + " -o " + str(directory) + "\merged\\" + str(filename) + "_merged_subsampled.las" 
    print(las2las_command)
    os.system(las2las_command)
    print("DONE\n")