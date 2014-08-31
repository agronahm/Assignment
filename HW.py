__author__ = 'michael'
print("hello Ghana")
print("yes Lord")
import numpy
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
