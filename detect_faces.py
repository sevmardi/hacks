from __future__ import print_function
import cv2
import argparse
from  FaceDetector import *

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True,
                help="path to where the face cascade resides")
ap.add_argument("-i", "--image", required=True,
                help="path to where the image file resides")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fd = FaceDetector(args['face'])
faceReacts = fd.detect(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

print("I found {} face(s)".format(len(faceReacts)))

for (x, y, w, h) in faceReacts:-
    cv2.rectange(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)
