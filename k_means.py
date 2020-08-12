from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import cv2
import utils


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
ap.add_argument("-c", "--clusters", required=True, type=int, help="# of clusters")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure()
plt.axis("off")
plt.imshow(image)