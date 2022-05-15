# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:41:22 2022

@author: Sarah Li
"""
import wind_generator as mdp_gen


def test_simple_kernel(kernel_func):
    test_states = [(0, 0), (4, 1), (8, 2), 
                   (1, 3), (3, 4), (8, 5),
                   (0, 8), (5, 7), (8, 8)]
    
    print(' -------testing right action--------- ')
    for s in test_states:
        # going to the right
        print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 1)}')
    
    print(' -------testing left action --------- ')    
    for s in test_states:
        print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 5)}')
    print(' -------testing up action --------- ')    
    for s in test_states:
        print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 3)}')
    print(' -------testing down action --------- ')    
    for s in test_states:
        print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 7)}')

    print(' -------testing staying still--------- ')
    for s in test_states:
        # going to the right
        print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 0)}')
        
    print(' -------testing up right--------- ')
    for s in test_states:
        # going to the right
        print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 2)}')
    print(' -------testing up left--------- ')
    for s in test_states:
        # going to the right
        print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 4)}')
        
    print(' -------testing down right--------- ')
    for s in test_states:
        # going to the right
        print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 8)}')

# def test_simple_kernel(kernel_func):
#     test_states = [(0, 0), (4, 1), (8, 2), 
#                    (1, 3), (7, 4), (8, 5),
#                    (0, 8), (5, 7), (8, 8)]
    
#     print(f' -------testing right action--------- ')
#     for s in test_states:
#         # going to the right
#         print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 1)}')
    
#     print(f' -------testing left action --------- ')    
#     for s in test_states:
#         print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 5)}')
#     print(f' -------testing up action --------- ')    
#     for s in test_states:
#         print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 3)}')
#     print(f' -------testing down action --------- ')    
#     for s in test_states:
#         print(f' neighbors of {s}, {s[1]*9 + s[0]}= {kernel_func(s[0], s[1], 9, 9, 7)}')
        
test_simple_kernel(mdp_gen.new_kernel)
print('################# containment kernel ##################')
# test_simple_kernel(mdp_gen.containment_kernel)