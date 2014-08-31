__author__ = 'michael'
print("hello Ghana")
print("yes Lord")
import numpy
from math import *
def rectangle_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle
    :parameters: length and width
    :return:(2*length + 2*width)
    rectangle_perimeter(length=5, width=6):
    10 + 12 =22
    """
    return 2*length + 2*width

if __name__ == "__main__":
    samplelength = 5
    samplewidth = 6
    print("perimeter:",
          rectangle_perimeter(samplelength, samplewidth))


def cone_volume(radius,height):
    """
     Calculate volume of sphere
     :parameter:
     :return:1/3 *numpy.pi*(radius**2)*height
     radius = 2, height = 4
     volume =
     """
    return 1/3*height*numpy.pi*(radius**2)

if __name__ == "__main__":
    sampleradius = 2
    sampleheight = 4
    print("volume:",
         cone_volume(sampleradius,sampleheight))


def triangle_area1(length):
    """
    Calculate the area of equilateral triangle side 2cm
    :param length: length of a side of the triangle
    :return: area
    >>>triangle_area1(2)
    """
    return 2*(sin(numpy.pi/3))

if __name__ == "__main__":
    samplelength = 2
    print("area1:",
          triangle_area1(samplelength))

def triangle_area(length, height):
    """
    Calculate area of an equilateral triangle
    :param length: length of base of triangle
    :param height: height of triangle
    :return: area
    >>>triangle_area(2,3**(1/2))
    1.73205
    """
    return (1/2)*(length*height)

    return 1/2*length*(tan(numpy.pi/3))

if __name__ == "__main__":
    samplelength = 2
    sampleheight = 3**(1/2)
    print("triangle area:",
          triangle_area(samplelength, sampleheight))