# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:25:34 2018

@author: ashut
"""

import numpy as np
import math
import matplotlib.pyplot as plt
max_lim = 40
min_lim = 1

possible_states = np.arange(min_lim,max_lim+1).tolist()

j5_xk = np.log(possible_states).tolist()

def mdp_descrete(possible_states, k_xk):
    max_bet = []
    j4_xk = []
    for i in possible_states:
        u1 = np.arange(0,max_lim-i+1)
        u2 = np.arange(0, i)
        u = np.intersect1d(u1,u2)
        bet_arr = []
        for j in u:
        
            ind1 = possible_states.index(i+j)
            ind2 = possible_states.index(i-j)
                
            bet_arr.append(0.7*(k_xk[ind1]) + 0.3*(k_xk[ind2]))
        inde3 = bet_arr.index(max(bet_arr))
        
        max_bet.append(u[inde3])
        j4_xk.append(bet_arr[inde3])
        
    return max_bet, j4_xk


j4_mb,j4_xk = mdp_descrete(possible_states, j5_xk)
j3_mb,j3_xk = mdp_descrete(possible_states, j4_xk)
j2_mb,j2_xk = mdp_descrete(possible_states, j3_xk)
j1_mb,j1_xk = mdp_descrete(possible_states, j2_xk)


######for j_0(20)

i = 20
u1 = np.arange(0,max_lim-i+1)
u2 = np.arange(0, i)
u = np.intersect1d(u1,u2)
bet_arr = []
for j in u:
    
    ind1 = possible_states.index(i+j)
    ind2 = possible_states.index(i-j)
                
    bet_arr.append(0.7*(j1_xk[ind1]) + 0.3*(j1_xk[ind2]))
inde3 = bet_arr.index(max(bet_arr))
j0_mb = u[inde3]
j0_xk = 20


p_vict = 0.7
def log_gambler_cont(possible_states, p_vict):
    optimal_val = []
    for i in possible_states:
        optimal_val.append(i*(p_vict -1 + p_vict))
    return optimal_val
        

j4_c = log_gambler_cont(possible_states, 0.7)
j3_c = log_gambler_cont(possible_states, 0.7)
j2_c = log_gambler_cont(possible_states, 0.7)
j1_c = log_gambler_cont(possible_states, 0.7)

j0_c = 20*(p_vict -1 + p_vict)

plt.plot(possible_states,j4_mb, label =  "Descrete")
plt.plot(possible_states,j4_c, label = "Continuous")

plt.show()
