__author__ = 'michael'
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


def rhombus_perimeter(sidelength):
    """
    Calculate the perimeter of a
    :parameter:length of side
    :return: 4*sidelength
    let sidelength = 3
    perimeter = 12
    """
    return 4*sidelength

if __name__ == "__main__":
    samplesidelength = 3
    print("perimeter:",
          rhombus_perimeter(samplesidelength))



def circle_area(radius):
     """
     Calculating the area of a circle with radius 5cm
     :parameter: length of radius
     return: area of circle = numpy.pi*(r**2)
     area of circle with radius 5:
     78.5398163397
     """
     return numpy.pi*radius**2

if __name__ == "__main__":
     sampleradius = 5
     print("area:",
           circle_area(sampleradius))


def parallelogram_area(baselength,height):

   """Calculate area of a parallelogram
      :parameters:baselength and height
     :return:baselength*height
      baselength = 4, height = 4
      area= 16
    """
   return baselength*height

if __name__ == "__main__":
    samplebaselength = 4
    sampleheight = 4
    print("area:",
        parallelogram_area(samplebaselength,sampleheight))


def circlesector_area(sectorangle, radius):
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
    print("area",
          circlesector_area(sampleangle, sampleradius))

def triangle_area(baselength,height):
    """
     Calculate the area of an equilateral triangle with side 2
    :parameter: length of side and height of triangle
    :return: 1/2*length of base*height
    area of equilateral triangle with side length 2cm and height 3**1/2
     1/2*2*3**2=
    """
    return (baselength*height)*(1./2)

if __name__ == "__main__":
    samplebaselength = 2.0
    sampleheight = 3**(1./2)
    print("area:",
          triangle_area(samplebaselength, sampleheight))


def triangle_area1(slantedlength,angle):
    """area=1/2*slantedlength*numpy.cos(angle)"""

    return 1/2*slantedlength*(tan(angle))

if __name__ == "__main__":
    sampleangle = numpy.pi/3
    sampleslantedlength = 2
    print( "area1:",
          triangle_area1(sampleslantedlength, sampleangle))

def trapezium_area(horizontallength1,horizontallength2,height):

    """ area of a trapizium
        :parameter: horizontal length1,horizontal length2 and height
        :return: (horizontal length1 + horizontal length2)/2*height
            horizontal length1 = 4 horizontal length2 = 2 and height = 3
                area = 9
    """
    return (horizontallength1 + horizontallength2)/2*height

if __name__ == "__main__":
    samplehorizontallength1 = 4
    samplehorizontallength2 = 2
    sampleheight = 3
    print("area:",
          trapezium_area(samplehorizontallength1,samplehorizontallength2,sampleheight))


def circle_circumference(radius):
    """
    Calculating the circumference of a circle radius 5
    :parameter: radius
    :return:circumference = 2* numpy.pi * radius
    2* numpy.pi * (radius=6) =
    """
    return 2*numpy.pi*radius

if __name__ == "__main__":
    sampleradius = 5
    print("circumference:",
          circle_circumference(sampleradius))


def cylinder_volume(radius,height):
    """
        Calculate the volume of a cylinder
            :parameter:radius and height
            :return: numpy.pi*(radius**2)**height
            radius = 4, height = 7
             volume = 351.858377202
    """
    return numpy.pi*(radius**2)*height

if __name__ == "__main__":
    sampleradius = 4
    sampleheight = 7
    print("volume:",
          cylinder_volume(sampleradius,sampleheight))


def cuboid_volume(length, width, height):
    """
     Calculate volume of a cuboid
     :parameter:sides of length,width and height
     :return: length* width* height
     cuboid_volume(length= 4, width=3, height=2):
     24
    """
    return length*width*height

if __name__ == "__main__":
    samplelength = 4
    samplewidth = 3
    sampleheight = 2
    print("volume:",
          cuboid_volume(samplelength, samplewidth, sampleheight))


def sphere_volume(radius):
    """Calculate volume of sphere
     :parameter:radius
     :return:4/3 *numpy.pi*(radius**3)
     raduis = 2
     volume = 33.5103216383
     """
    return 4/3 *numpy.pi*(radius**3)

if __name__ == "__main__":
    sampleradius = 2
    print("volume:",
          sphere_volume(sampleradius))


def cone_volume(radius, height):
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
         cone_volume(sampleradius, sampleheight))



