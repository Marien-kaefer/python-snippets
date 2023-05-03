# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import math
import numpy as np

filename = "qi_treated28_top-data-2023.04.26-17.04.50.562_processed-2023.04.26-17.23.59.tsv"
image_size_x = 128
image_size_y = 128


filename_without_extension = filename[:-4] 

dataset=pd.read_csv(filename,delimiter="\t")


image = np.zeros( (image_size_x, image_size_y) ) #initiate empty matrix the size of the final image

YM =dataset['Young\'s Modulus [Pa]']

#Populate image matrix with values of the Young's Modulus
j = 0
while j < image_size_y:
    i = 0
    while i < image_size_x:
      image[i,j] = YM[i + j * image_size_y]
      i += 1
    j += 1
    
np.savetxt(filename_without_extension + "YM-image.txt", image, delimiter=',')