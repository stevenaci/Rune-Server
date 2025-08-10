
class file_extensions():
    image = ["jpg", "png", "bmp", "gif"]

    video = ["mkv", "mp4"]

    @property
    def all(self):
        return file_extensions.image + file_extensions.video

    video_html_encodings = {
        "mp4" : "video/mp4",
        "mkv" : None
    }

def allowed_file(filename):
    r = filename.split('.')[-1].lower()
    return '.' in filename and filename.split('.')[-1].lower() in file_extensions.all
