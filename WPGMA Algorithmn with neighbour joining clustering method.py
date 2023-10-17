#!/usr/bin/env python
# coding: utf-8

# The following code implements UPGMA, WPGMA, and neighbour joining algorithms to draw philogenetic trees to 3 sets of examples

# In[6]:


import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Sample sequences
sequences = [
    "AGCTGACT",
    "AGCTGGCT",
    "AGCTCACT",
    "AGCTTAGT",
    "AGCTGATT"
]
# Sample distance matrix
distance_matrix = np.array([
    [0, 0.2, 0.4, 0.7, 0.9],
    [0.2, 0, 0.5, 0.8, 1.0],
    [0.4, 0.5, 0, 0.6, 0.8],
    [0.7, 0.8, 0.6, 0, 0.3],
    [0.9, 1.0, 0.8, 0.3, 0]
])

# Perform UPGMA clustering
upgma_tree = linkage(distance_matrix, method='average')

# Perform Neighbor-Joining clustering
nj_tree = linkage(distance_matrix, method='single')

# Plot UPGMA dendrogram
plt.figure(figsize=(8, 4))
dendrogram(upgma_tree, labels=sequences, orientation='right')
plt.title('UPGMA Dendrogram')
plt.show()

# Plot Neighbor-Joining dendrogram
plt.figure(figsize=(8, 4))
dendrogram(nj_tree, labels=sequences, orientation='right')
plt.title('Neighbor-Joining Dendrogram')
plt.show()

# Perform WPGMA clustering
wpgma_tree = linkage(distance_matrix, method='ward')

# Plot WPGMA dendrogram
plt.figure(figsize=(8, 4))
dendrogram(wpgma_tree, labels=species, orientation='right')
plt.title('WPGMA Dendrogram')
plt.show()


# 
# Using the following observed pairwise distance between hominoid sequences in primates:
# 	 Human	Chimp	Gorilla	Orang-utan	Gibbon
# Human	0	79	     92	    144     	162
# Chimp	79	0	     95	    154	        16
# Gorilla	92	102	      0	    150      	169
# Orang-utan	144	154	 150	 0	       169
# Gibbon	163	173	     169	169     	0
# 

# In[7]:


import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Primate species names
species = ["Human", "Chimp", "Gorilla", "Orang-utan", "Gibbon"]

# Sample distance matrix
distance_matrix = np.array([
    [0, 79, 92, 144, 162],
    [79, 0, 95, 154, 169],
    [92, 95, 0, 150, 169],
    [144, 154, 150, 0, 169],
    [162, 169, 169, 169, 0]
])

# Perform UPGMA clustering
upgma_tree = linkage(distance_matrix, method='average')

# Perform Neighbor-Joining clustering
nj_tree = linkage(distance_matrix, method='single')

# Plot UPGMA dendrogram
plt.figure(figsize=(8, 4))
dendrogram(upgma_tree, labels=species, orientation='right')
plt.title('UPGMA Dendrogram')
plt.show()

# Plot Neighbor-Joining dendrogram
plt.figure(figsize=(8, 4))
dendrogram(nj_tree, labels=species, orientation='right')
plt.title('Neighbor-Joining Dendrogram') 
plt.show()

# Perform WPGMA clustering
wpgma_tree = linkage(distance_matrix, method='ward')

# Plot WPGMA dendrogram
plt.figure(figsize=(8, 4))
dendrogram(wpgma_tree, labels=species, orientation='right')
plt.title('WPGMA Dendrogram')
plt.show()

