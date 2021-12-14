'''
This script creates equal spacing positions on 
an imaginary circle whose center is (eccentricity, 0)

'''
from math import pi, cos, sin
import matplotlib.pyplot as plt
import random

def get_rotated_posi(posi_on_circle, ran_angle, center_x):
    '''
    posi_on_circle: corr of (x, y) on circle whose center is (center_x, 0)
    ran_angle: random angle that the posi rotate
    center_x: circle x corr, usually the eccentricity
    '''
    x2 = (posi_on_circle[0] - center_x) * cos(ran_angle) + posi_on_circle[1] * sin(ran_angle)
    y2 = -(posi_on_circle[0] - center_x) * sin(ran_angle) + posi_on_circle[1] * cos(ran_angle)
    return (x2 + center_x, y2)


def get_first_set_random_spacing_posis(setsize, eccentricity, radius):
    
    # calculate segmentation angle
    angle_seg = 2*pi/setsize
    
    positions = list()
    
    for i in range(0, setsize):
        x = r * cos(i * angle_seg)  + (eccentricity)
        y = r * sin(i * angle_seg)
        positions.append((x, y))
    
    return positions

if __name__ == '__main__':
    # TODO
    plot_new_positions = True
    eccentricity = 8 
    r = 3 # radius of the imaginary circle
    setsize = 6 # the number of equal-spacing positions

    positions = get_first_set_random_spacing_posis(setsize, eccentricity, r)

    ran_angle_to_rotate = random.uniform(0, 2*pi/setsize)
    
    new_posis= [get_rotated_posi(posi, ran_angle_to_rotate, eccentricity) for posi in positions]

    if plot_new_positions:

        fig, ax = plt.subplots()
        for posi in new_posis:
            ax.scatter(posi[0], posi[1])
        plt.axis('scaled')
