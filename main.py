from simulation import visualize
from vpython import *



def main():
    l1, l2, l3, c = visualize()
    while(1):
        angles = int(input("Enter angle"))
        c.rotate(angle=radians(angles), axis=vector(0, 0, 1), origin=c.pos)
    pass

if __name__ == '__main__':
    main()