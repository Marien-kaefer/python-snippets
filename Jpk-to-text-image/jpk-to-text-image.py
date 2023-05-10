# -*- coding: utf-8 -*-
"""
Script to pull Young's modulus data from a JPK AFM results file. The Young's modulus values are listed as a single column and converted to an xy image.  
Copy the name of the file to be processed incl. extension and paste it to the filename variable. The file must reside in the same folder as the script. 
Also supply the numbers of pixels in x and y for the image. 
The resulting image will be automatically saved in the same folder as the input file and named "originalFileName_YM-image.txt". 

												- Written by Marie Held [mheldb@liverpool.ac.uk] May 2023
												  Liverpool CCI (https://cci.liverpool.ac.uk/)
________________________________________________________________________________________________________________________

BSD 2-Clause License

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 

"""

import pandas as pd
import numpy as np


" USER INPUT START " 
filename = "qi_treated28_top-data-2023.04.26-17.04.50.562_processed-2023.04.26-17.23.59.tsv"
image_size_x = 128
image_size_y = 128
" USER INPUT END "

filename_without_extension = filename[:-4] 

dataset=pd.read_csv(filename,delimiter="\t")


image = np.zeros( (image_size_x, image_size_y) ) #initiate empty matrix the size of the final image

YM =dataset['Young\'s Modulus [Pa]']

#Populate image matrix with values of the Young's Modulus
j = 0
while j < image_size_y:
    i = 0
    while i < image_size_x:
      image[i,j] = YM[i + j * image_size_x]
      i += 1
    j += 1


np.savetxt(filename_without_extension + "_YM-image.txt", image, delimiter=',')

" clean up, delete all variables"
del dataset, filename, filename_without_extension, i, j, image, image_size_x, image_size_y
