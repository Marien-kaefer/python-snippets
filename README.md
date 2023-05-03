# Python Snippets
short python scripts to make life easier


## JPK/Bruker results to image - Young's modulus

Script to pull Young's modulus data from a JPK AFM results file (.tsv). In the results file, the Young's modulus values are listed as a single column and converted to an xy image.  

The user is expected to provide the following: 
1. Copy the name of the file to be processed incl. extension and paste it to the filename variable. The file must reside in the same folder as the script. 
2. Supply the numbers of pixels in x and y for the image as recorded on the JPK/Bruker AFM. 

The resulting text file will be automatically saved in the same folder as the input file and named "originalFileName_YM-image.txt". This file can then be imported as an image in Fiji and processed further. The image file is 32 bit with the "intensities" representing the Young's modulus at the location of each pixel.  