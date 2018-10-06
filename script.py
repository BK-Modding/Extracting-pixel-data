from skimage import io
import numpy as np
from scipy import stats
np.set_printoptions(threshold=np.nan)

image = io.imread('test_img.jpg')

print("Max: {}".format(np.amax(image)))
print("Min: {}".format(np.amin(image)))
print("Mean: {}".format(np.mean(image)))
print("Mode: {} ({})".format(stats.mode(image, axis=None).mode[0], stats.mode(image, axis=None).count[0]))