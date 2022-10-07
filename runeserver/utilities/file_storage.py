import sys
from glob import glob
import os

# returns the static/uploads/fname path from an uploaded file.
def to_upload_path(fname):
        base = os.path.basename(fname)
        return os.path.join("static", "uploads", base) # Should work on Unix and windows

# find images in a directory
def find_image_files(dir):
    paths = []
    imgfiles = glob(dir + '\\*.jpg') + glob(dir + '\\*.png') + glob("\\*.bmp") + glob(dir + '\\*.gif')

    for img in imgfiles:
        imgpath = to_upload_path(img)
        paths.append(imgpath)
    
    return paths

def find_video_files(dir):
    paths = []
    vid_files = glob(dir + '\\*.mkv') + glob(dir + '\\*.mp4')

    for vid in vid_files:
        paths.append(os.path.basename(vid))
    
    return paths

def gather_images(dir): # gather all the images in a directory
    print("Gathering images from {}".format(dir))
    return find_image_files(dir)

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