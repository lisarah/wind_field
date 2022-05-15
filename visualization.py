# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:09:38 2021

@author: Sarah Li
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def policy_arrow_gen(policy_ind):
    lookup = {
        0: (0, 0), # no action
        1: (1, 0), # right,
        2: (1, 1), # upper_right
        3: (0, 1), # top, 
        4: (-1, 1), # top left
        5: (-1, 0), # left
        6: (-1, -1), # bottom left
        7: (0, -1), # bottom
        8: (1, -1) # bottom right
        }
    return lookup[policy_ind]

def draw_policies(s_width, s_length, policy, axis):
    color = 'xkcd:coral'
    # color = 'xkcd:pale yellow'
    # color = 'xkcd:lemon'
    for x_ind in range(s_length):
        for y_ind in range(s_width):   
            # print(f'grid {x_ind}, {y_ind}')
            length =  0.3 
            dx, dy = policy_arrow_gen(policy[y_ind*s_length + x_ind])
            axis.arrow(x_ind + 0.5, -y_ind+0.5, 
                       dx * length, -dy * length, 
                       head_width=0.3, head_length=0.15, 
                       fc=color, ec=color)
    
def init_grid_plot(Rows, Columns, base_color, v_max, v_min):
    f, axis = plt.subplots(1)
    color_map, norm, sm = color_map_gen(base_color, v_max, v_min)
    
    value_grids = []
    for y_ind in range(Rows):
        value_grids.append([])
        for x_ind in range(Columns):
            R,G,B,_ = color_map(norm((base_color[y_ind*Columns+ x_ind])))
            color = [R,G,B]  
            value_grids[-1].append(plt.Rectangle((x_ind, -y_ind), 1, 1, 
                                                 fc=color, ec='xkcd:greyish blue'))
            axis.add_patch(value_grids[-1][-1])
    plt.axis('scaled')

    plt.colorbar(sm)
    axis.xaxis.set_visible(False)  
    axis.yaxis.set_visible(False)
    return axis, value_grids, f

def color_map_gen(base_color, v_max, v_min):
    norm = mpl.colors.Normalize(vmin=v_min, vmax=v_max)
    color_map = plt.get_cmap('coolwarm')  
    sm = plt.cm.ScalarMappable(cmap=color_map, norm=norm)
    sm.set_array([])
    return color_map, norm, sm

    
    
    
    
    
    
    
    
    
    