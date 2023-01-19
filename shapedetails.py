from graphic.circle import pm1_cir,area1_cir
rad_cir=int(input("Enter the Radius of the circle"))
pm1_cir(rad_cir)
area1_cir(rad_cir)

from graphic.rectangle import pm1_rec,area1_rec
l_rec=int(input("Enter the Length of the Rectangle"))
b_rec=int(input("Enter the Breadth of the Rectangle"))
pm1_rec(l_rec,b_rec)
area1_rec(l_rec,b_rec)

from graphic.threeD_graphics.cuboid import pm1_cub,area1_cub
l_cub=int(input("Enter the Length of the cuboid"))
b_cub=int(input("Enter the Breadth of the cuboid"))
h_cub=int(input("Enter the Height of the cuboid"))
pm1_cub(l_cub, b_cub, h_cub)
area1_cub(l_cub, b_cub, h_cub)


from graphic.threeD_graphics.sphere import pm1_sph,area1_sph
rad_sph=int(input("Enter the Radius of the Sphere"))
area1_sph(rad_sph)
pm1_sph(rad_sph)
