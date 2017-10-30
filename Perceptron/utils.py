"""
Utility functions needed for the project
"""
import os
import imageio
from PIL import Image
def mapping(value, istart, istop, ostart, ostop):
    """Maps value from istart to istop to ostart to ostop"""
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
def sign(num):
    return 1 if num >= 0 else -1
def f(x):
    return .3*x + .2
def genGIF(tmp_dir, dir_OUT):
        filenames = os.listdir(tmp_dir)
        for item in filenames:
            im = Image.open(tmp_dir + item)
            imResize = im.resize((int(im.size[0]),int(im.size[1])), Image.ANTIALIAS)
            imResize.save(tmp_dir + item,'JPEG', quality=100)
        # filenames.sort(key= lambda x: float(x.strip('.jpeg')))
        images = []
        for filename in filenames:
            images.append(imageio.imread(tmp_dir + filename))
        imageio.mimwrite(dir_OUT + "/solution" + ".gif", images)