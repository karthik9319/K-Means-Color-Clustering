import numpy as np
import cv2


def centroid_histogram(clt):
    numlabels = np.arange(0, len(np.unique(clt.labels_)) +1)
    (hist, _) = np.histogram(clt.labels_, bins=numlabels)
    
    hist = hist.astype("float")
    hist /= hist.sum()
    
    return hist
    