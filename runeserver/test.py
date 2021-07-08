
import glob
target_dir = "D:/Code/GUI/RuneServer/Rune-Server/runeserver/static/uploads/"
for img in glob.glob(target_dir + '*.png'):
    print(img)
