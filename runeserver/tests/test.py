
import glob
import os

def test_uploads_folder(dir):
    if not os.path.exists(dir):
        return False
    return True
