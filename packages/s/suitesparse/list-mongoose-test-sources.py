from subprocess import call, check_output
import os       # For filesystem access
import sys      # For sys.exit()
import argparse # For parsing command-line arguments
import urllib.request, urllib.parse, urllib.error   # For downloading the ssget index
import ssl
import tarfile  # For un-tar/unzipping matrix files
import csv      # For reading the ssget index
import shutil   # For using 'which'
import platform


# We only need the following matrix ids:
MATRIX_IDs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 21, 39, 57, 182, 191, 201, 242, 250, 353, 360, 505, 760, 1380, 1389, 1437, 1470, 1530, 1533, 1557, 1562, 2331, 2401, 2420, 2468, 2624]

def getMatrixDirectory():
    matrix_dir = "."
    if (not os.path.exists(matrix_dir)):
        os.makedirs(matrix_dir)
    return matrix_dir

def downloadStatsFile(matrix_dir):
    stats_file = "ssstats.csv"
    url = "http://sparse.tamu.edu/files/ssstats.csv"
    with urllib.request.urlopen(url) as response, open(stats_file, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    return stats_file

def runTests():
    # Create or locate matrix temporary storage directory
    matrix_dir = getMatrixDirectory()

    # Download the matrix stats csv file
    stats_file = downloadStatsFile(matrix_dir) 

    with open(stats_file, 'r') as f:
        reader = csv.reader(f)

        # Matrix IDs are not listed in the stats file - we just have to keep count
        matrix_id = 0
        sources_initial_num = 4
        for row in reader:

            if len(row) == 13: # Only rows with 13 elements represent matrix data
                matrix_id += 1

                # Check if the matrix ID is in the proper range and
                # that the matrix is real and symmetric
                isInBounds = ((matrix_id >= 1) and (matrix_id <= 2757))
                isSquare = (row[2] == row[3])
                isReal = (row[5] == '1')

                if (isInBounds and isSquare and isReal):
                    if True:
                        matrix_name = row[0] + '/' + row[1] + '.tar.gz'
                        gzip_path = matrix_dir + row[0] + '_' + row[1] + '.tar.gz'
                        matrix_path = matrix_dir + row[1] + '/' + row[1] + ".mtx"
                        # print("matrix_name: " + matrix_name)
                        # print("gzip_path:   " + gzip_path)
                        # print("matrix_path: " + matrix_path)

                        matrix_exists = os.path.isfile(gzip_path)
                        if False:
                            print("matrix exists at gzip_path")
                            tar = tarfile.open(gzip_path, mode='r:gz')
                            matrix_files = tar.getnames()
                            print(matrix_files)
                        else:
                            # Download matrix if it doesn't exist
                            if matrix_id in MATRIX_IDs:
                                sources_initial_num += 1
                                try:
                                    url = "https://sparse.tamu.edu/MM/" + matrix_name
                                    print("Source" + str(sources_initial_num) + ": " + url)
                                except:
                                    url = "http://sparse.tamu.edu/MM/" + matrix_name
                                    print("Source" + str(sources_initial_num) + ": " + url)
runTests()

