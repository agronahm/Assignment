__author__ = 'michael'
print("I love Jesus" )
import numpy
from numbers import Number
def square_perimeter(side : Number) -> Number:
    """
    Calculate perimeter of a square from side length.
    @param side: the side length
    @return: the perimeter (same units as side length)
    >>> square_perimeter(4)
    16
    """
    return 4*side


def square_area(side):
    """
    Calculate area of a square from side length.
    :param side: the side length
    :return: the area (units^2 from side)
    >>> square_area(4)
    16
    """
    return side*side


def rectangle_area(length, width):
        """
        Calculate area of rectangle from side length and width.
        :parameters side: sides of length and width
        :return:area (length * width)
        rectangle_area(4,2)
        8
        """
        return length*width

def rectangle_perimeter(length, width):
    """
    Calculate perimeter of a rectangle from length and with
    :parameters: length and width
    return: perimeter (2*length + 2*width)
    rectangle_perimeter(length=5, width=4):
    10+8=18
    """
    return 2*length + 2*width


if __name__ == "__main__":
    sampleSide=4
    samplewidth = 4
    samplelength = 5
    print("area:",
          square_area(sampleSide),
          "perimeter:",
          square_perimeter(sampleSide),
          "rectangle_area",
          rectangle_area(samplelength, samplewidth),
          "perimeter",
          rectangle_perimeter(samplelength, samplewidth))

if __name__ == "__main__":
    samplewidth = 6
    samplelength = 5

    print("perimeter:",
          rectangle_perimeter(samplelength, samplewidth))

def circle_area(radius):
     """
     Calculating the area of a circle with radius 5cm
     :parameter: length of radius
     return: area of circle = numpy.pi*(r**2)
     area of circle with radius 5:
     12.571428571
     """
     return numpy.pi*radius**2

if __name__ == "__main__":
     sampleradius = 5
     print("area:",
           circle_area(sampleradius))
      area of a sector of a circle  angle 30 in degrees
    : parameter: lengthof raduis and angle formed by the ci
    area of an equalateral traingle with side 2 and height 3**1/2
    return 1/2*base*sampleheight
        return 1/2*numpy.sin(numpy.pi/3)

if __name__ == "__main__":
    samplelength = 2
    print("area:",
          triangle_area(samplelength))

def circlesector_area(angle, radius):
    """
     Calcualating the area of a sector of a circle with radius
     5 and angle 30 in degrees
    :parameter: angle of sector and length of radius
    :return:2*numpy.pi*radius*(sector angle)/360
    """
    return 2*numpy.pi*radius*sectorangle/360

if __name__ == "__main__":
    sampleradius = 5
    sampleangle = 30
    print("circumference:",
          circle_circumference(sampleradius),
          "area",
          circlesector_area(sampleangle, sampleradius))


def circle_area(radius):
    return numpy.pi* radius**2
if __name__ == "__main__":
    sampleradius = 2
    print("area:",
          circle_area(sampleradius))






