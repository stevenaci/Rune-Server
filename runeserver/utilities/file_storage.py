import sys
from glob import glob
import os

def find_image_files(dir):
    paths = []
    print("globbing: " + dir)

    imgfiles = glob(dir + '\\*.jpg') + glob(dir + '\\*.png') + glob("\\*.bmp") + glob(dir + '\\*.gif')

    for img in imgfiles:
        img = os.path.basename(img)
        print("globbed: " + img)
        fullpath = os.path.join("static", "uploads", img) # Should work on Unix and windows
        paths.append( fullpath)
    
    return paths
def gather_images(dir): # gather all the images in a directory

    print("Gathering images from {}".format(dir))
    files = []
    imgpaths = find_image_files(dir)

    print(imgpaths)
    return imgpaths

def isvalidfile(length, filename, ftype):
    ext = filename[length-3:]

    if (ext == "jpg") or (ext == "gif") or (ext == "bmp") or (ext == "png"):
        if ftype == "image":
            return True

    if (ext == 'txt') or (ext == 'pdf'):
        if ftype == "text":
            return True
    if ftype == "video":
        return True
    return False

def validate_folder(dir):
    print("\nvalidating folder {}".format(dir))
    if not os.path.exists(dir):   # if upload folder doesnt exist, create it.
        print("dir {} doesn't exist, creating it here".format(dir))
        try:
            os.makedirs(dir)
            return True
        except OSError as e:
            print(e)
            print("\ncouldnt create folder")
            return False
            
    print("\nfolder exists")
    return True