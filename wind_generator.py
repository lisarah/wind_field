# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:49:34 2022

@author: Sarah Li
"""
import numpy as np


def distance(x_1, x_2, y_1, y_2, length, width): # 1 norm distance
    vec_1 = np.array([x_1, x_2])
    vec_2 = np.array([y_1, y_2])
    return np.linalg.norm(vec_1 - vec_2, 2)

def check_region(s_x, s_y, square):
    region = 0 # 0 = calm, 1 = center, 2 = bad wind

    if s_x < 0 or s_y < 0: # negative row or column
        print(f'invalid square at {s_x}, {s_y}')
    elif s_y < square: # first row
        if s_x >= square and s_x < 3 * square:
            region = 2
    elif s_y < 2 * square: # 2nd row
        if s_x >= square and s_x < 2 * square:
            region = 1
        elif s_x >= 2 * square and s_x < 3 * square:
            region = 2
    # s_y < 3 square == all calm
    return region

def get_neighbors(s_x, s_y, s_length, s_width, a_ind):
    """ Returns neighbors in counterclock sequence, starting from the 
        rightmost neighbour.
    """
    s_ind = s_y * s_length + s_x
    ns = [s_ind + 1,  # right 0
          s_ind + s_length + 1, # upper right 1
          s_ind + s_length, # up 2
          s_ind + s_length - 1, # upper left 3
          s_ind - 1, # left 4
          s_ind - s_length - 1, # bottom left 5
          s_ind - s_length, # bottom 6
          s_ind - s_length + 1, # bottom right 7
          s_ind] # center
    # no wrap - stepping out of bounds = re-enter current state
    unreachable = []
    if s_x == 0:
        unreachable += [3, 4, 5]
    elif s_x == s_width - 1:
        unreachable += [0, 1, 7]
    if s_y == 0:
        unreachable += [5, 6, 7]
    elif s_y == s_length - 1:
        unreachable += [1, 2, 3]
        
    for i in unreachable:
        ns[i] = None
        
    # bad region
    blown_ns = []
    region = check_region(s_x, s_y, s_length/3)
    reacheable_neighbors = []
    if region == 2:
        if a_ind  == 0:
            reacheable_neighbors = [8, 6, 7]
            # reacheable_neighbors = [i for i in range(8)]
            # blown_ns.append(s_ind)
        elif a_ind == 1:
            reacheable_neighbors = [0, 6, 7]
        elif a_ind == 2:
            reacheable_neighbors = [1, 6, 7]
        elif a_ind == 3:
            reacheable_neighbors = [2, 6, 7]
        elif a_ind == 4: 
            reacheable_neighbors = [3, 6, 7]
        elif a_ind == 5:
            reacheable_neighbors = [4, 6, 7]
        elif a_ind == 6:
            reacheable_neighbors = [5, 6, 7]
            # blown_ns.append(s_ind)
        elif a_ind == 7: # down
            reacheable_neighbors = [6, 6, 7]
            # blown_ns.append(s_ind)
        elif a_ind == 8:
            reacheable_neighbors = [7, 6, 7]
    # wild region (center)
    elif region == 1:
        if a_ind == 0:
            blown_ns.append(s_ind)
        reacheable_neighbors = [i for i in range(8)]
    # origin, destination, and left
    elif region == 0:
        # blown_ns.append(s_ind)
        if a_ind == 0:
            reacheable_neighbors = [8]
            # reacheable_neighbors = [i for i in range(8)]
        elif a_ind == 1:
            reacheable_neighbors = [0,1,7]
        elif a_ind == 2:
            reacheable_neighbors = [0,1,2]
        elif a_ind == 3:
            reacheable_neighbors = [1,2,3]
        elif a_ind == 4:
            reacheable_neighbors = [2,3,4]
        elif a_ind == 5:
            reacheable_neighbors = [3,4,5]
        elif a_ind == 6:
            reacheable_neighbors = [4,5,6]
        elif a_ind == 7:
            reacheable_neighbors = [5,6,7]
        elif a_ind == 8:
            reacheable_neighbors = [6,7,0]
    [blown_ns.append(ns[i]) for i in reacheable_neighbors]
    # print(f'{s_x}, {s_y}, current blown_ns {blown_ns}')
    # remove all non-neighbors
    for i in range(len(blown_ns)):
        if blown_ns[i] is None:
            blown_ns[i] = s_ind
    blown_ns = list(filter((None).__ne__, blown_ns))     
    
    if len(blown_ns)==0: blown_ns.append(s_ind)
    return blown_ns        

def wind_field_gen(S, A, s_length):
    I = 2 # maximum number of different kernels
    P = np.zeros((S, S, A, I))
    C = np.zeros((S, A, 1))
    target = (s_length-1, s_length-1)
    for s in range(S):
        s_x = s % s_length 
        s_y = int(s / s_length)
        for a in range(A):
            C[s, a, 0] = distance(s_x, s_y, target[0], target[1], 
                                  s_length, s_length)
            if a > 0: # zeroth action uses no power
                C[s, a, 0] += 1 
            neighbors = get_neighbors(s_x, s_y, s_length, s_length, a)
            region = check_region(s_x, s_y, s_length/3)
            if region in [0, 1]: # calm region or wild region
                # even distribution to all neighbors
                for ns in neighbors:
                    P[ns, s, a, :] += 1
                P[:, s, a, :] = P[:, s, a, :] / len(neighbors)
            else: # region 2
                # two possibilities: 
                # 1) going the correct direction 
                # 2) pushed upwind           ')
                # first action is correct direction
                P[neighbors[0], s, a, 0] = 1
                # second action is pushed upwind
                for ns in neighbors[1:]:
                    P[ns, s, a, 1] += 1
                P[:, s, a, 1] = P[:, s, a, 1] / (len(neighbors) - 1)
    return P, C






