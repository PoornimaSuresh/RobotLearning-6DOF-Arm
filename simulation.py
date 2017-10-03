from vpython import *
#from visual import *

# sphere(color=cyan)

linklength = 10

# Initialize all joints and links
joint1 = sphere(pos = vector(0,0,0), color = vector(0,0,255))
link1 = cylinder(pos = joint1.pos, axis = vector(linklength,0,0))
joint2 = sphere(pos = link1.axis, color = vector(0,0,255))
link2 = cylinder(pos = vector(link1.axis), axis = vector(0, linklength, 0))
joint3 = sphere(pos = (link2.axis + link2.pos), color = vector(0,0,255))
link3 = cylinder(pos = vector(link2.pos + link2.axis), axis = vector(0, 0, linklength))
joint4 = sphere(pos = (link3.axis + link3.pos), color = vector(0,0,255))
link4 = cylinder(pos = vector(link3.pos + link3.axis), axis = vector(linklength, 0, 0))
joint5 = sphere(pos = (link4.axis + link4.pos), color = vector(0,0,255))
link5 = cylinder(pos = vector(link4.pos + link4.axis), axis = vector(0, -linklength, 0))
joint6 = sphere(pos = (link5.axis + link5.pos), color = vector(0,0,255))
link6 = cylinder(pos = vector(link5.pos + link5.axis), axis = vector(0, 0, -linklength))
endeffector = arrow(pos = link6.pos + link6.axis, axis = link6.axis, color = vector(255, 0, 0))
