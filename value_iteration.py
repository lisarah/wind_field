# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:21:26 2019

@author: craba
"""
import numpy as np


def value_iteration_polytopes(P, C, gamma = 0.9):
    S, S, A, Ip = P.shape
    V_min =  float("-inf")*np.ones(S)
    V_max =  float("-inf")*np.ones(S)
    C_max = np.max(C, axis=2)
    C_min = np.min(C, axis=2) 
    V_next_min = np.zeros(S) # float("-inf")*np.ones(S)
    V_next_max = np.zeros(S) # float("-inf")*np.ones(S)
    it = 0
    pi_opt = np.zeros(S)
    pi_rbt = np.zeros(S)
    Iterations = 1e3
    while np.linalg.norm(V_min - V_next_min, ord = 2) >= 1e-5 and \
          np.linalg.norm(V_max - V_next_max, ord = 2) >= 1e-5 and \
          it < Iterations:
        print(f'\r it {it}         ', end = '')
        V_min = 1 * V_next_min
        V_max = 1 * V_next_max
        for s in range(S):
            q_max = np.zeros((A, Ip))
            q_min = np.zeros((A, Ip))
            for i in range(Ip):
                q_max[:,i] = np.squeeze(C_max[s,:]) + gamma*np.einsum('jk,j',P[:, s, :, i], V_max)
                q_min[:,i] = np.squeeze(C_min[s,:]) + gamma*np.einsum('jk,j',P[:, s, :, i], V_min) 
            pseudo_v_min = np.min(q_min, 0) # take minimum over all actions for each case
            pseudo_v_max = np.min(q_max, 0)
            V_next_min[s] = np.min(pseudo_v_min) # hbar operation
            V_next_max[s] = np.max(pseudo_v_max)
            # print(f' s = {s}, previous V: {V_min[s]} new V: {V_next_min[s]}')
        # print (f'errors {np.linalg.norm(V_min - V_next_min, ord = 2) } {np.linalg.norm(V_max - V_next_max, ord = 2)}')
        it += 1
    for s in range(S):
        q_min = np.zeros((A, Ip))
        q_max = np.zeros((A, Ip))
        for i in range(Ip):
                q_max[:,i] = C_max[s,:] + gamma*np.einsum('ij,i',P[:, s, :, i], V_max)
                q_min[:,i] = C_min[s,:] + gamma*np.einsum('ij,i',P[:, s, :, i], V_min) 
        max_ind = np.argmax(q_max, 1)[0]
        min_ind = np.argmin(q_min, 1)[0]
        pi_opt[s] = np.argmin(q_min[:, min_ind], 0)
        pi_rbt[s] = np.argmin(q_max[:, max_ind], 0)
    return V_min, V_max, pi_opt, pi_rbt


def value_iteration_rectangular(P, C, gamma = 0.9):
    S, S, A, Ip = P.shape
    V_min =  float("-inf")*np.ones(S)
    V_max =  float("-inf")*np.ones(S)
    C_max = np.max(C, axis=2)
    C_min = np.min(C, axis=2) 
    V_next_min = np.zeros(S) # float("-inf")*np.ones(S)
    V_next_max = np.zeros(S) # float("-inf")*np.ones(S)
    it = 0
    pi_opt = np.zeros(S)
    pi_rbt = np.zeros(S)
    Iterations = 1e3
    while np.linalg.norm(V_min - V_next_min, ord = 2) >= 1e-5 and \
          np.linalg.norm(V_max - V_next_max, ord = 2) >= 1e-5 and \
          it < Iterations:
        print(f'\r it {it}         ', end = '')
        V_min = 1 * V_next_min
        V_max = 1 * V_next_max
        for s in range(S):
            q_min = np.zeros(A)
            q_max = np.zeros(A)
            for a in range(A):
                q_min_a = C_min[s,a] + gamma*np.einsum('ij,i',P[:, s, a, :], V_min)
                q_max_a = C_max[s,a] + gamma*np.einsum('ij,i',P[:, s, a, :], V_max)
                q_min[a] = np.min(q_min_a)
                q_max[a] = np.max(q_max_a)
            V_next_min[s] = np.min(q_min)
            V_next_max[s] = np.min(q_max)
        it += 1
    for s in range(S):
        q_min = np.zeros(A)
        q_max = np.zeros(A)
        for a in range(A):
            q_min_a = C_min[s,a] + gamma*np.einsum('ij,i',P[:, s, a, :], V_next_min)
            q_max_a = C_max[s,a] + gamma*np.einsum('ij,i',P[:, s, a, :], V_next_max)
            q_min[a] = np.min(q_min_a)
            q_max[a] = np.max(q_max_a)
        pi_opt[s] = np.argmin(q_min)
        pi_rbt[s] = np.argmin(q_max)
    return V_min, V_max, pi_opt, pi_rbt

