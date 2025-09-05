# Calculate a cylinder volume, the formula is = πr²h

def find_cylinder_volume(radius, height):
    print("radius: ", radius)
    print("height: ", height)
    volume = 3.14*(radius**2)*height
    return volume

r = 10
h = 7

volume = find_cylinder_volume(r,h)
print("Cylinder Volume is", volume)

