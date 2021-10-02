from vpython import *
canvas(background=color.black)
donut =ring(radius=0.5,thickness=0.25,color=vector(400,100,1))
chocolate =ring(radius=0.55,thickness=0.25,color=vector(0.4,0.2,0))

donut.rotate(angle=1,axis=vector(0,1,0))

chocolate.rotate(angle=1,axis=vector(0,1,0))
