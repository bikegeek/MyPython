import re
import os
import sys


def get_filepaths(dir):
    """Generates the file names in a directory tree
       by walking the tree either top-down or bottom-up.
       For each directory in the tree rooted at
       the directory top (including top itself), it
       produces a 3-tuple: (dirpath, dirnames, filenames).

    Args:
        dir (string): The base directory from which we
                      begin the search for filenames.
    Returns:
        file_paths (list): A list of the full filepaths
                           of the data to be processed.


    """

    # Create an empty list which will eventually store
    # all the full filenames
    file_paths = []

    # Walk the tree
    for root, directories, files in os.walk(dir):
        for filename in files:
            # add it to the list only if it is a grib file
            match = re.match(r'.*(.txt)$',filename)
            if match:
                # Join the two strings to form the full
                # filepath.
                filepath = os.path.join(root,filename)
                file_paths.append(filepath)
            else:
                continue
    return file_paths



if __name__ == "__main__":
    parse_decode = False
   
    if parse_decode:    
        dir = sys.argv[1]
        files =  get_filepaths(dir)
        script_cmd = "parseMetar.pl  -L/home/idp/compare/ADDS/metars -t 2016042506 "
        cmd = script_cmd + "<" + file + ">>metars_adds.csv"
        os.system(cmd)
    else:
        file = sys.argv[1]
        script_cmd = "/usr/bin/perl metarCsv2Iwxxm-us.pl -L/home/idp/compare/ADDS/metars -O /home/idp/compare/ADDS/metars "
        cmd = script_cmd + "<" + file + ">>metars_adds.iwxxm"
        print "command for csv to xml: %s"%(cmd)
        os.system(cmd)

