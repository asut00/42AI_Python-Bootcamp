# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asuteau <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/13 09:31:59 by asuteau           #+#    #+#              #
#    Updated: 2024/06/13 09:32:01 by asuteau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from PIL import Image
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import os

class ImageProcessor:

	def is_file_empty(self, path):
		return os.path.getsize(path) == 0

	def load(self, path):

		
		if not os.path.exists(path):
			# raise FileNotFoundError(f"No such file or directory: '{path}'")
			print(f"No such file or directory: '{path}'")
			exit(1)
		if self.is_file_empty(path):
			# raise FileNotFoundError(f"File is empty: '{path}'")
			print(f"File is empty: '{path}'")
			exit(1)
		img = plt.imread(path)  # avec matplotlib
		# img = Image.open(path) # avec PIL
		# img = imageio.imread(path) # avec imageio

		arr_img = np.array(img)
		width = len(arr_img[0])
		height = len(arr_img)
		print(f"Loading image of dimensions {width} x {height} ")
		return arr_img
	
	def display(self, array):
		plt.imshow(array)
		plt.axis('off')
		plt.show()


if __name__=="__main__":
	imp = ImageProcessor()
	file_path = '42AI.png'
	arr = imp.load(file_path)
	print(arr)
	imp.display(arr)
	# print(arr)






		# try :
		# 	if not os.path.exists(path):
		# 		raise FileNotFoundError(f"No such file or directory: '{path}'")
		# 	if self.is_file_empty(path):
		# 		raise FileNotFoundError(f"File is empty: '{path}'")
		# 	img = plt.imread(path)  # avec matplotlib
		# 	# img = Image.open(path) # avec PIL
		# 	# img = imageio.imread(path) # avec imageio
		# except FileNotFoundError as fnf_error:
		# 	print(fnf_error)
		# 	raise
		# except Exception as e:
		# 	print(f"An error occurred: {e}")
		# 	raise