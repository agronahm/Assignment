__author__ = 'michael'
import numpy
from math import *

def rectangle_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle
    :param length: length of rectangle
    :param width:  width of rectangle
    :return:perimeter
    >>>rectangle_perimeter(5,6)
    22
    """
    return 2*length + 2*width

if __name__ == "__main__":
    samplelength = 5
    samplewidth = 6
    print("perimeter of rectangle:",
        rectangle_perimeter(samplelength, samplewidth))


def rhombus_perimeter(length):
    """
    Calculating the perimeter of a rhombus
    :param length: length of side of rhombus
    :return:perimeter
    >>>rhombus_perimeter(3)
    12
    """
    return 4*length

if __name__ == "__main__":
    samplelength = 3
    print("perimeter of rhombus:",
          rhombus_perimeter(samplelength))


def circle_area(radius):
    """
     Calculating the area of a circle
     :param radius:radius of the circle
     :return:area
     >>>circle_area(5)
     78.5398
    """
    return numpy.pi*(radius**2)

if __name__ == "__main__":
     sampleradius = 5
     print("area of circle:",
           circle_area(sampleradius))


def circlesector_area(angle, radius):
    """
    Calculating area of a sector of a circle
    :param angle: angle of sector of the circle
    :param radius: the radius of circle
    :return: area of the sector of the circle
    >>>circlesector_area(30, 5)
    6.54498
    """
    return numpy.pi*(radius**2)*angle/360

if __name__ == "__main__":
    sampleradius = 5
    sampleangle = 30
    print("area sector of circle",
          circlesector_area(sampleangle, sampleradius))

def circle_circumference(radius):
    """
    Calculating the circumference of a circle
    :param radius: radius of circle
    :return:circumference
    >>>circle_circumference(5)
    31.4159
    """
    return 2*numpy.pi*radius

if __name__ == "__main__":
    sampleradius = 5
    print("circumference of circle:",
          circle_circumference(sampleradius))


def parallelogram_area(base, height):
    """
    Calculating area of a parallelogram
    :param base: length of base of parallelogram
    :param height:height of parallelogram
    :return:area
    >>>parallelogram_area(4, 4)
    16
    """
    return base*height

if __name__ == "__main__":
    samplebase = 4
    sampleheight = 4
    print("area of parallelogram:",
         parallelogram_area(samplebase, sampleheight))


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

if __name__ == "__main__":
    samplelength = 2
    sampleheight = 3**(1/2)
    print("area of triangle first method:",
          triangle_area(samplelength, sampleheight))


def triangle_area1(length):
    """
    Calculate the area of equilateral triangle side 2cm
    :param length: length of a side of the triangle
    :return: area
    >>>triangle_area1(2)
    1.73205
    """
    return 1/2*length*(tan(numpy.pi/3))

if __name__ == "__main__":
    samplelength = 2
    print("area of triangle second method:",
          triangle_area1(samplelength))

def trapezium_area(length1, length2, height):
     """
     Calculate area of trapezium
     :param length1: length of one horizontal side of the trapezium
     :param length2:length of the other horizontal side of the trapezium
     :param height:height of the trapezium
     :return:area
     >>>trapezium_area(4,2,3)
     9
     """
     return height*(length1 + length2)/2

if __name__ == "__main__":
    samplelength1 = 4
    samplelength2 = 2
    sampleheight = 3
    print("area of trapezium:",
          trapezium_area(samplelength1, samplelength2, sampleheight))


def kite_area(diagonal1, diagonal2):
    """
    Calculating area of kite
    :param diagonal1: length of short diagonal
    :param diagonal2: length of long diagonal
    :return:area
    >>>kite_area(2, 3)
    6
    """
    return diagonal1 * diagonal2

if __name__ == "__main__":
    samplediagonal1 = 2
    samplediagonal2 = 3
    print("area of kite:",
          kite_area(samplediagonal1,samplediagonal2))


def cylinder_volume(radius,height):
    """
     Calculate the volume of a cylinder
     :param radius of cylinder
     :param height of cylinder
     :return: volume
     >>>cylinder_volume(4,7)
     351.858377202
    """
    return numpy.pi*(radius**2)*height

if __name__ == "__main__":
    sampleradius = 4
    sampleheight = 7
    print("volume of cylinder:",
          cylinder_volume(sampleradius, sampleheight))


def cuboid_volume(length, width, height):
    """
    Calculate volume of a cuboid
    :param length: length of cuboid
    :param width: width of cuboid
    :param height: height of cuboid
    :return:volume
     >>>cuboid_volume( 4,3,2):
     24
    """

    return length*width*height

if __name__ == "__main__":
    samplelength = 4
    samplewidth = 3
    sampleheight = 2
    print("volume of cuboid:",
          cuboid_volume(samplelength, samplewidth, sampleheight))


def sphere_volume(radius):
    """
    Calculate volume of sphere
     :param radius:radius of sphere
     :return:volume
     raduis
     >>>sphere_volume(2)
      33.5103216383
     """
    return 4/3 *numpy.pi*(radius**3)

if __name__ == "__main__":
    sampleradius = 2
    print("volume of sphere:",
          sphere_volume(sampleradius))


def cone_volume(radius, height):
    """
    Calculate volume of cone
    :param radius: radius of cone
    :param height: height of cone
    :return:volume
    >>>cone_volume(2,4)
    16.75516
    """

    return 1/3*height*numpy.pi*(radius**2)

if __name__ == "__main__":
    sampleradius = 2
    sampleheight = 4
    print("volume of cone:",
         cone_volume(sampleradius, sampleheight))



