import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox


def count(x):
    im = cv2.imread(x)
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    # plt.imshow(output_image)
    # plt.show()
    """print('Number of cars in the image is '+str(label.count('car')))
    print('Number of persons in the image is '+str(label.count('person')))
    print('Number of motorcycle in the image is ' + str(label.count('motorcycle')))
    print('Number of truck in the image is '+str(label.count('truck')))"""
    return str(label.count('car')), str(label.count('person')), str(label.count('motorcycle')), str(label.count('truck'))
