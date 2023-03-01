from Rectangle import Rectangle, Cuboid

cuboid = Cuboid(Rectangle(20, 15), 10)
print("volume:", cuboid.count_volume())
print("surface area:", cuboid.count_surface_area())
