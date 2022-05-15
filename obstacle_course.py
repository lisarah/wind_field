# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 02:12:21 2021

@author: craba
"""
import numpy as np
import wind_generator as wind
import value_iteration as vi
import matplotlib.pyplot as plt
import visualization as vs


# np.random.seed(456)
length = 9
width = 9
N = 20
mag_bounds = (np.ones(N), np.ones(N) * 2)


# --------- generate max/min bounds on the polytopic MDP ------------
S = length * width
A = 9
P, C = wind.wind_field_gen(S, A, length)
abs_min = np.inf
abs_max = -np.inf
v_min, v_max, pi_opt, pi_rbt = vi.value_iteration_polytopes(P, C, gamma = 0.9)
abs_min = min(abs_min, min(v_min))   
abs_max = max(abs_max, max(v_max)) 


value_grid_min = v_min.reshape((width, length))
value_list_min = value_grid_min.flatten()
cost_plot, val_grids, _ = vs.init_grid_plot(width, length, value_list_min, abs_max, abs_min)
vs.draw_policies(width, length, pi_opt, cost_plot)
plt.show()

value_grid_max = v_max.reshape((width, length))
value_list_max = value_grid_max.flatten()
cost_plot, val_grids, _ = vs.init_grid_plot(width, length, value_list_max, abs_max, abs_min)
vs.draw_policies(width, length, pi_rbt, cost_plot)
plt.show()

# --------- generate a random MDP based on wind sampling --------- 
# wind_min, wind_max, angles_min, angles_max = wind_bound_gen(length)    
# P, R = wind.bound_mdp_gen(angles_min, angles_max, wind_min, wind_max)   
# values, policy = dp.value_iteration(P, R, minimize=True, g=0.5)

# S = length * width
# _, A = R.shape 
# print(f'values shape {values.shape}')
# value_grid = values.reshape((width, length))
# print(f'value grid shape {value_grid.shape}')


# r_max = np.max(R, axis=1)
# r_grid = r_max.reshape((width, length))
# plt.figure()
# plt.imshow(r_grid, interpolation='nearest')
# # plt.imshow(value_grid.T, interpolation='nearest')
# plt.colorbar()
# plt.show() 

# plt.figure()
# # plt.imshow(r_grid.T, interpolation='nearest')
# plt.imshow(value_grid, interpolation='nearest')
# plt.colorbar()
# plt.show()


# value_list = value_grid.flatten()
# cost_plot, val_grids, _ = vs.init_grid_plot(width, length, value_list)

# original_policy = []
# for s in range(S):
#     pol, = np.argwhere(policy[s, s*A:(s+1)*A] == 1) 
#     print(f' state {s}, policy {pol[0]}')
#     original_policy.append(pol[0])
    
    
# wind.draw_policies(width, length, original_policy, cost_plot)
# plt.show()