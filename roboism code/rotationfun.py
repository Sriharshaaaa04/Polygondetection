import cv2
import numpy as np
def rotate(im1,angle,rotPoint=None):
    [height,width]=im1.shape[:2]
    
    if rotPoint is None:
      rotPoint=(width//2,height//2)
    rotMat=cv2.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv2.warpAffine(im1,rotMat,dimensions)
