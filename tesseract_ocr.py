import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import re

from itertools import izip


img = cv2.imread('image.jpg')

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

# TESSERACT
def image_to_text(filePath):
    image = cv2.imread(filePath)

    gray = get_grayscale(image)
    # thresh = thresholding(gray)
    # opening2 = opening(gray)
    # canny2 = canny(gray)

    # tesseract run on subject
    text = pytesseract.image_to_string(gray, lang='ind')
    return text

def image_to_data(filePath):
    # tesseract run on subject
    data = pytesseract.image_to_data(filePath, lang='ind', output_type=Output.DICT)
    return data

def slice_per(source, step):
    return [source[i::step] for i in range(step)]

filePath = "../sample/s_tugas1.jpeg"
a = image_to_data(filePath)
# print(a['text'])
# print(b[11])
# list1 = np.array_split(b, 11)
# print(list1[0])
# i = iter(data)
# b = dict(izip(i, i))



# print(image_to_text(filePath))
# print(image_to_text("/opening.png"))
# print(image_to_text("/canny.png"))

# cv2.imwrite('./thresh.png', thresh)
# cv2.imwrite('./opening.png', opening)
# cv2.imwrite('./canny.png', canny)
