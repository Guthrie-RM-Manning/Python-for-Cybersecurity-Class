##Wells.py
##Start by importing math so we can use it for math.pi
import math

##get inputs for height and radius
radiusInches =float(input("Please enter the radius of the well in inches: "))
heightFeet = float(input("please enter the height of the well in feet: "))

##Convert radiusInches to feet
radiusFeet = radiusInches / 12

##next we have to calculate the volume in cubic feet
cubicFeetVolume = math.pi * (radiusFeet ** 2) * heightFeet

##finally we convert the CubicFeetVolume into Gallons and print it

volumeWater = cubicFeetVolume * 7.48

print("the well can hold approximately " + str(volumeWater) + " gallons of water")

