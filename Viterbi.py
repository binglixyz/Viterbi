# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:01:32 2018

@author: bingl
"""

states = ('Healthy', 'Fever')
 
observations = ('normal', 'cold', 'dizzy')
 
start_probability = {'Healthy': 0.6, 'Fever': 0.4}
 
transition_probability = {
   'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
   'Fever' : {'Healthy': 0.4, 'Fever': 0.6},
   }
 
emission_probability = {
   'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
   'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
   }

def viterbi(obs, states, start_p, trans_p, emiss_p):
    T1 = [{}]
    path = {}
    
    for state in states:
        T1[0][state] = start_p[state] * emiss_p[state][obs[0]]
        path[state] = [state]

    for t in range(1, len(obs)):
        T1.append({})
        newpath = {}
        for current_state in states:
            (prob, state) = max([(T1[t-1][s] * trans_p[s][current_state] * emiss_p[current_state][obs[t]], s) for s in states])
            T1[t][current_state] = prob
            newpath[current_state] = path[state] + [current_state]
        path = newpath
    (max_prob, most_likely_path) = max([(T1[len(obs) - 1][s], s) for s in states])
    print(path[most_likely_path])
    
viterbi(observations, states, start_probability, transition_probability, emission_probability);