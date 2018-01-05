from pyimagesearch.facedetector import FaceDetector
from pyimagesearch import imutils
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="Path to where the face cascade resides")
ap.add_argument("-v", "--video", help="path to the (optional) video file")
args = vars(ap.parse_args())

fd = FaceDetector(args["face"])
