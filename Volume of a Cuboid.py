#Volume of a cuboid
def cuboid_volume(length, width, height):
    volume = length * width * height

    return volume

length_in = int(input("Enter the length of the cuboid: "))
width_in = int(input("Enter the width of the cuboid: "))
height_in = int(input("Enter the height of the cuboid: "))

volume_out = cuboid_volume(length_in, width_in, height_in)
print("The volume of the cuboid is " + str(volume_out))
