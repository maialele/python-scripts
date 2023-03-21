# the mission is tio make a class of a tar file and give it two methods:
# one: extract the file
# two: read all of the files in the directroty and return how many files there are of which kind

import tarfile
import sys, os


class Tar:
    def __init__(self, file):
        self.file = file

    def open_tar(self, folder='/tmp'):
        mytar = tarfile.open(self.file)
        mytar.extractall(folder)
        mytar.close()
        self.folder = folder

    def count_tar(self):
        type_dict = {}
        for path, subdirs, files in os.walk(self.folder):
            for name in files:
                print(name)



tar_file = '/tmp/test.tar' 
file = Tar(tar_file)
file.open_tar('/tmp/test')
file.count_tar()

