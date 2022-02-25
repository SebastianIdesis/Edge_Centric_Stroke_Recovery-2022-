# -*- coding: utf-8 -*-
"""
Created on Thu Feb  24 14:10:52 2022

@author: Sebastian Idesis
contact: sebastian.idesis@upf.edu
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import itertools
import pandas as pd  

def oneDArray(x):
    return list(itertools.chain(*x))
from scipy.io import loadmat

# Load dataset
annots = loadmat('C:/Seba/Barcelona/PhD_material/Paper_edge_recovery/Script and results/14_participation_coefficient/data_for_seaborn.mat')


lesion = oneDArray(annots['lesion_volume']) #Extract feature of lesion from the loaded matrix
nihss_score = oneDArray(annots['nihss']) #Extract feature of nihss values from the loaded matrix
part_coeff =oneDArray(np.transpose(annots['parti_coeff_t1'])) #Extract feature of participation coefficient from the loaded matrix

df = pd.DataFrame({'lesion':lesion,'nihss':nihss_score,'part_coeff':part_coeff}) #Create dataframe

#Visualize correlation plots

sns.set_style("darkgrid")
sns.jointplot(data=df,x='part_coeff', y='lesion', s=100)
plt.grid()  
plt.savefig('part_coeff_with_lesion.svg', dpi=300)
plt.show()

sns.set_style("darkgrid")
sns.jointplot(data=df,x='part_coeff', y='nihss')
plt.grid()  #just add this
plt.savefig('part_coeff_with_nihss.svg', dpi=300)
plt.show()