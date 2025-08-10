from glob import glob
import os
from runeserver.utilities.extensions import file_extensions

def get_upload_path(fname):
        base = os.path.basename(fname)
        return os.path.join("static", "uploads", base) # Should work on Unix and windows

def find_files(dir, exts: list[str] = []):
    """ find files with an extension filter"""
    files = []
    for ext in exts:
         files += glob(dir + f'\\*.{ext}')
    return files

def find_video_files(dir):

    return [os.path.basename(fn)
        for fn in find_files(dir, exts=file_extensions.video)
    ]
    
def find_image_files(dir):
    return [os.path.basename(fn) for fn in find_files(dir, exts=file_extensions.image)]

def get_ext(fn): return fn.split('.')[-1]

def is_valid_file(filename, ftype):
    ext = get_ext(filename)

    if ftype == "image":
        if ext in file_extensions.image:
                return True
    if ftype == "text":
        if ext in file_extensions.text:
            return True
    if ftype == "video":
        if ext in file_extensions.video:
            return True
    return False

def touch_folder(dir):
    print("\nvalidating folder {}".format(dir))
    if not os.path.exists(dir):   # if folder doesnt exist, create it.
        print("dir {} doesn't exist, creating it here".format(dir))
        try:
            os.makedirs(dir)
            return True
        except OSError as e:
            print(e)
            print("\nCouldnt create folder")
            return False
            
    print("\nFolder exists")
    return True