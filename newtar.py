'''
the purpose of this script is to extract a tar file (extract_tar method) and return how many files of each type there
are in the extracted folder (read_tar method). 
'''

# import neccesary libraries
import tarfile
import sys, os

# Tar Object
class Tar:
    # initialize the tar object with file.tar
 
    def __init__(self, file, folder):
        self.file = file
        self.folder = folder



    # open, extract the file and close it. 
    def extract_tar(self, folder='/home/maia'):
        my_tar = tarfile.open(self.file)
        my_tar.extractall(self.folder)
        my_tar.close()
        # exporting the folder variable to the class (this is the way the interviewer asked me to do this)
        self.folder = folder + '/tarfolder'

    # read alll the files in the new extracted tar folder and its subfolder and return a dictionary of all of the types
    def read_tar(self,):
        type_dict = {}
        for path, subdirs, files in os.walk(self.folder):
            for name in files:fol
                # get only the extentsions and count them in a dictionary 
                file_extentsion = name.split('.')[-1]
                if file_extentsion in type_dict:
                    type_dict[file_extentsion] += 1
                else:
                    type_dict[file_extentsion] = 1
        return type_dict

#initializing a tar object 
tar_object = Tar('/home/maia/mytar.tar')

# extracting the file using the extract_tar method
tar_object.extract_tar()

# going through the extracted tar file and returning all the types in the directories and subdirectories
final_dict = tar_object.read_tar()
tar_object.folder()
# printing the dictionary in a nicer way
for file_ext in final_dict:
    print (file_ext + ': ' + str(final_dict[file_ext]))

